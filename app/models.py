"""
Classes that we want to turn into columns and tables in our AstraDB database 

These are our Cassandra data models, essentially tables and columns that we define under the keyspace "scraper_app" - the equivalent of a schema in a relational database

We see similarity with traditional RDBMs including primary key attributes and schema on write definitions 

"""
from cassandra.cqlengine import columns # official ORM for Cassandra/Python
from cassandra.cqlengine.models import Model # ORM 

class Product(Model): # turns it into a Cassandra model (table)
    __keyspace__ = "scraper_app"
    asin = columns.Text(primary_key = True, required = True) # asin is a uuid for Amazon, hence PK
    title = columns.Text()
    price_str = columns.Text()
    rating_str = columns.Text()


class ProductScrapeEvent(Model):
    __keyspace__ = "scraper_app"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index = True) # asin is unique in Amazon, hence PK
    title = columns.Text()
    price_str = columns.Text()
    #rating_str = columns.Text()
    #country_of_origion = columns.Text()



