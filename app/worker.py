from celery import Celery
from celery.schedules import crontab 
from celery.signals import beat_init, worker_process_init # beat_init for scheduling, worker_process for
from . import config, db, models, scraper, schema, crud # import redis config setting
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

celery_app = Celery(__name__) # call celery app
settings = config.get_settings()

REDIS_URL = settings.redis_url

celery_app.conf.broker_url = REDIS_URL
celery_app.conf.result_backend = REDIS_URL

Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

def celery_on_startup(*arg, **kwargs): # startup task , setting up connection with Cassandra
    if connection.cluster is not None:
        connection.cluster.session.shutdown()
    if connection.session is not None:
        connection.session.shutdown()
    cluster = db.get_cluster()
    session = cluster.connect()
    connection.register_connection(str(session), session = session)
    connection.set_default_connection(str(session))
    sync_table(Product)
    sync_table(ProductScrapeEvent)

beat_init.connect(celery_on_startup)
worker_process_init.connect(celery_on_startup)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, *args, **kwargs):
    sender.add_periodic_task(crontab(minute="*/1"), scrape_products.s())

# @celery_app.task
# def list_products():
#     q = Product.objects().all().values_list("asin", flat = True)
#     print(list(q))

@celery_app.task
def scrape_asin(asin):
    print(asin)
    s = scraper.Scraper(asin = asin, endless_scroll = True)
    dataset = s.scrape()
    print(dataset)
    try: 
        validated_data = schema.ProductListSchema(**dataset)
    
    except:
         validated_data = None 

    if validated_data is not None:
        crud.add_scrape_event(validated_data.dict())
        #print(validated_data.dict())
        return asin, True
    
    return asin, False


@celery_app.task
def scrape_products():
    print ('Scraping')
    q = Product.objects().all().values_list("asin", flat = True)
    for asin in q:
        scrape_asin.delay(asin)
