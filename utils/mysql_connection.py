import pymysql

from configuration import config


connection = pymysql.connect(**config)
