import pymysql

from utils.configuration import config


connection = pymysql.connect(**config)
