""""
The .py file represents the schema that will be enforced on our data as it ingested and placed into  CassandraDB 

With the use of Pydantic, we are able define and enforce data models and validate input data by extending the use of type hints 

Built-in validators include Field, validate or constr - which allow you to define rules and constraints for each field

Root validation goes beyond field-level validation and performs a comprehensive validation of the entire data object

Pydantic is a common library used with the FastAPI web framework. 
"""

from pydantic import BaseModel, root_validator # to enforce data validation 
from uuid import UUID # to create a synthetic primary key 
from typing import Any, Optional # to assist with data validation
from . import utils # for timedate function

class ProductSchema(BaseModel): # a simple schema design with asin and title columns 
    asin: str
    title: Optional[str] 
    price_str : Optional[str]

class ProductListSchema(BaseModel): # schemas help with data validation 
    asin : str
    title: Optional[str]
    price_str: Optional[str]
    rating_str: Optional[str]
    
class ProductScrapeEventDetailSchema(BaseModel):
    asin: str
    title: Optional[str]
    price_str: Optional[str]
    created: Optional[Any] = None # timestamp
    brand: Optional[str]
    country_of_origin: Optional[str]

    @root_validator(pre = True) # root validation for the time stamp - root validation carries out validation before the main validation, hence pre = True
    def extra_create_time_from_uuid(cls, values): #'cls' refers to the class not the object 
        values['created'] = utils.uuid1_time_to_datetime(values['uuid'].time) # remove timestamp
        return values
    
