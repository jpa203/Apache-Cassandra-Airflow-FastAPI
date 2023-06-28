"""
C - Create
R - Read
U - Update
D - Delete

We define our crud operations that will create an instance of the data, as defined by the models, and put it into the database. 

"""

import uuid
import copy # for deep copy
from .models import Product, ProductScrapeEvent # importing tables from models


def create_entry(data:dict): # specifying hint types 
    return Product.create(**data) #kwargs  .create() from Cassandra CQL

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1() # creating a uuid field to pass to our data dict (includes timestamp)
    return ProductScrapeEvent.create(**data)  # create is part of CQL - creates an instance of the model in the database

def add_scrape_event(data:dict, fresh = False): # function adds both metadata + data 
    if fresh: # if data is fresh 
        data = copy.deepcopy(data) # do a deep copy
    product = create_entry(data) # call function
    scrape_object = create_scrape_entry(data) # call function

    return product, scrape_object