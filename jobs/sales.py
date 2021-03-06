#!/usr/bin/python3
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from typing import Callable, Optional
import sys
import re
import os
import json
import logging

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = f"{project_dir}/logs/job-{os.path.basename(__file__)}.log"
LOG_FORMAT = f"%(asctime)s - LINE:%(lineno)d - %(name)s - %(levelname)s - %(funcName)s - %(message)s"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger('py4j')

sys.path.insert(1, project_dir)
from classes import class_pyspark