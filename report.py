#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

try:
   # Setup up database
   conn = mdb.connect('localhost', 'ngopal', 'test123', 'testdb');

   cursor = conn.cursor()
   cursor.execute("SELECT * FROM Writers")

   # Fetch data
   rows = cursor.fetchall()

   for row in rows:
       print row

   cursor.close()
   conn.close()

except mdb.Error, e:
   print "Error %d: %s" % (e.args[0],e.args[1])
   sys.exit(1)
