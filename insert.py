import sqlite3


conn = sqlite3.connect('test.db')
print("Successfully connected to database")


conn.execute("INSERT INTO TEACHERS VALUES (1,'James','Kariuki',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (2,'General','Mathenge',40,34000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (3,'Adams','Malaya',48,40000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (4,'Denzel','Gichobi',42,50000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (5,'Cindy','Mutisya',35,54000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (6,'Jude','Sasha',37,70000.00)")

conn.commit()
print("Successfully Inserted data")
conn.close()
