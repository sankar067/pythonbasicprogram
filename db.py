# importing the module
#import MySQLdb
import cx_Oracle
# opening a database connection
#db = MySQLdb.connect  ("localhost","testprog","stud","PYDB")

#if needed, place an 'r' before any parameter in order to address any special character such as '\'.
dsn_tns = cx_Oracle.makedsn('SANPC', '1521', service_name='XE')

# if needed, place an 'r' before any parameter in order to address any special character such as '\'.
# For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
conn = cx_Oracle.connect(user=r'sankar', password='sankar', dsn=dsn_tns)

# define a cursor object
c = conn.cursor()

#Query
sql = 'select * from STUDENT'
c.execute(sql) # use triple quotes if you want to spread your query across multiple lines

for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()

# close object
c.close()

# close connection
conn.close()