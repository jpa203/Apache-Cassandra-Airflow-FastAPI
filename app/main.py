"""
In our main file, we define the FastAPI web intereface, including a start up event that syncs (updates) our data models.

We have created a number of views, each with a different grain of the ingested data 

"""


from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table
from . import config, db, models, schema, crud
from typing import List

settings = config.get_settings()  # import environment settings 

Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent


app = FastAPI() #@app

session = None

@app.on_event("startup") # gets the session and updates the tables
def on_startup():
    global session
    session = db.get_session()
    sync_table(Product)
    sync_table(ProductScrapeEvent)


@app.get("/") #
def read_index():
    return 'My Project: Apache Cassandra - Redis - FastAPI - Selenium - Celery'

@app.get("/products", response_model= List[schema.ProductListSchema]) # response model for data validation 
def products_list_view():
    return list(Product.objects.all())


@app.post("/events/scrape") # scrape page
def events_scrape_create_view(data: schema.ProductListSchema): # conforms to the schema
    product, _ = crud.add_scrape_event(data.dict()) # returns product and scrape_object
    return product

@app.get("/products/{asin}") # view for an individual product
def product_detail_view(asin):
    data = dict(Product.objects.get(asin = asin))
    events = list(ProductScrapeEvent.objects().filter(asin = asin)) # can add a limit to this filter
    events = [schema.ProductScrapeEventDetailSchema(**x) for x in events]  
    data['events'] = events
    return data

@app.get("/products/{asin}/events", response_model = List[schema.ProductScrapeEventDetailSchema]) # adds timestamp
def product_scrapes_list_view(asin):
    return list(ProductScrapeEvent.objects().filter(asin = asin))