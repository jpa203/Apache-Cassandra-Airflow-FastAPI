# Apache-Cassandra-Airflow-FastAPI
A NoSQL project using Apache Cassandra, Python, FastAPI, Redis, Selenium and Celery. 

This project was an exercise in understanding the Apache Cassandra NoSQL database and its properties, as well as integration with the FastAPI framework, webscraping and task scheduling using Celery and Selenium.

This project touches on a number of data engineering principles, including Data Modeling via ORM, in-memory caching with Redis, NoSQL and denormalized data design with Cassandra, Astra DB and CQL, 
web scraping and automation using Celery and Selenium.

The main exercise of this project was understanding how to enforce data validation and schema-on-write using the Pydanitc library - an extension of Python's typing libray. With Pydantic, you are able to enforce 
and change a schema quickly according to the structure of your data. This allows some flexibility with relational data and works. wellwith Cassandta, a column-oriented database optimized for fast queries and forgiving 
toward redundancy and BASE properties. 

This project also implemented views via FastAPI - a modern web framework for building APIs with Python that natively incorporates Pydantic. 

Celery was also implemented for asynchronous task handling. In production, the NosSQL solution will be able to handle hundreds of automated data entries per second - and meets the criteria for scalability in terms of big data.

A few screenshots of the final prject are shared below, including the web interface, Celery automation and database.
<img width="1416" alt="Screenshot 2023-06-28 at 9 25 57 AM" src="https://github.com/jpa203/Apache-Cassandra-Airflow-FastAPI/assets/104007355/77a4dddb-1a7d-4467-aa3c-30385e437c4c">

Example of data entry into AstraDB - highlighting how some web scrapes may yield different results and even return nulls for certain columns.
<img width="1018" alt="Screenshot 2023-06-28 at 9 28 47 AM" src="https://github.com/jpa203/Apache-Cassandra-Airflow-FastAPI/assets/104007355/b5888d40-b653-4d60-adbe-5d4e3b874891">

An example of the Celery worker running.

![Screenshot 2023-06-28 at 9 29 49 AM](https://github.com/jpa203/Apache-Cassandra-Airflow-FastAPI/assets/104007355/46cf8060-b60d-4900-8f70-f50725711d69)
