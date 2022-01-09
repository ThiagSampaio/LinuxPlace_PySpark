#!/usr/bin/python3

import json
import os
import re
import sys
from typing import Callable, Optional
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession


class Sparkclass:

    # referenciando a classe em si.
    def __init__(self, config: dict):
        self.config = config

    def sparkStart(self, kwargs: dict) -> SparkSession:
        print(self.config)
