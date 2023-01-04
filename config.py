""" File: cfg.py / config.py """
""" To collect and parse data from config files (config.ini and notifications.ini) """

import configparser

#cfg = configparser.ConfigParser()


#print("Reading config files...")
# Parsing configuration from config.cfg
#cfg.read("mysql.cfg")
# MySQL Configuration
HOST = "localhost"
PORT = int(3306)
USER = "root"
PASSWORD = "12345678"
DATABASE = "HotelManagementSystem"
