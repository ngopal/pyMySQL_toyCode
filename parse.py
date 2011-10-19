#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

try:
   # Setup up database
   conn = mdb.connect('localhost', 'ngopal', 'test123', 'testdb');

   cursor = conn.cursor()

   # Populate database
   cursor.execute("CREATE TABLE IF NOT EXISTS \
       Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
   cursor.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
   cursor.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
   cursor.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
   cursor.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
   cursor.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
   cursor.execute("SELECT VERSION()")

   # Save changes
   conn.commit()

   # Fetch data
   data = cursor.fetchone()

   # Close connections
   cursor.close()
   conn.close()

except mdb.Error, e:
   print "Error %d: %s" % (e.args[0],e.args[1])
   sys.exit(1)

print "Database version : %s " % data
