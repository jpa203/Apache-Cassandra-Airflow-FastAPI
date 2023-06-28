"""
util file usually contains a collection of utility functions or helper functions that are used across an application or a specific component of a program. 

small, reusable code snippetes that provide common functionality or perform specific tasks that are frequently needed in multiple parts of a program. 

"""

import datetime

def uuid1_time_to_datetime(time:int):
    return datetime.datetime(1582, 10, 15) + datetime.timedelta(microseconds= time//10)


"""

parsing datae time from the UUID field

"""