
import mysql.connector
import logging
# from __future__ import print_function
from datetime import date, datetime, timedelta
import configparser
import io
import json


# get and set DB configs
config = configparser.ConfigParser()
config.read('Configs/DBconfigs.ini')
  
DB_username = config.get('mysql','user')
DB_password = config.get('mysql','password')
DB_host = config.get('mysql','host')
DB_name = config.get('mysql','database')

cnx = mysql.connector.connect(user=DB_username, password=DB_password,
                              host=DB_host, database=DB_name)
cursor = cnx.cursor()


# load in json file





tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO Users "
               "(FirstName, LastName, EmailAddress, UserPassword) "
               "VALUES (%s, %s, %s, %s)")
# add_salary = ("INSERT INTO salaries "
#               "(emp_no, salary, from_date, to_date) "
#               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ('Geert', 'Vanderkelen', 'kk@aol.com', 'Pword')

# Insert new employee
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

# Insert salary information
# data_salary = {
#   'emp_no': emp_no,
#   'salary': 50000,
#   'from_date': tomorrow,
#   'to_date': date(9999, 1, 1),
# }
# cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()