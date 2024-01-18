##** Select, Update, Manipulate **##

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", 
)

print(mydb)

mycursor = mydb.cursor(buffered=True)

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

mycursor.execute("USE barath")

# mycursor.execute("SELECT * FROM diabetes ")
# out=mycursor.fetchall()
# from tabulate import tabulate
# # print(mycursor.description)
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## For Limiting the cells ##

# mycursor.execute("SELECT * FROM diabetes limit 20 ")
# out=mycursor.fetchall()
# from tabulate import tabulate
# # print(mycursor.description)
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## For selecting the Limited Coloumns ##

# mycursor.execute("SELECT age,bmi FROM diabetes limit 20 ")
# out=mycursor.fetchall()
# from tabulate import tabulate
# # print(mycursor.description)
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## Applying the condition for Coloumns using Math funtion ##

# mycursor.execute("SELECT age,bmi,outcome FROM diabetes WHERE outcome=1 limit 10")
# mycursor.execute("SELECT pregnancies,glucose FROM diabetes WHERE pregnancies=7")
# mycursor.execute("SELECT count(*) FROM diabetes WHERE pregnancies=2")
# mycursor.execute("SELECT count(*) FROM diabetes WHERE pregnancies IN (1,5,6)")
# mycursor.execute("SELECT count(*) FROM diabetes WHERE pregnancies NOT IN (1,5,6)")
# mycursor.execute("SELECT concat(outcome,'-',bmi) as Whole_Count FROM diabetes WHERE pregnancies IN (1,5,6)")
# mycursor.execute("SELECT max(pregnancies) FROM diabetes")
# mycursor.execute("SELECT min(bloodpressure) FROM diabetes")
# mycursor.execute("SELECT power(4,4)")
# mycursor.execute("SELECT greatest(4,4,2,9)")
# mycursor.execute("SELECT least(4,4,2,9)")
# mycursor.execute("SELECT sum(4+4)")
# mycursor.execute("SELECT floor(4.858)")

## Between Query ##

# mycursor.execute("SELECT COUNT(Pregnancies) FROM diabetes WHERE Outcome = 0 AND BloodPressure > 41 AND Bloodpressure < 91")
# mycursor.execute("SELECT COUNT(Pregnancies) FROM diabetes WHERE BloodPressure BETWEEN 40 AND 90 AND outcome = 0")

## Sub Query (or) Nested Query

# mycursor.execute("SELECT COUNT(Pregnancies) FROM diabetes WHERE Outcome = 0 AND BloodPressure IN (SELECT bloodpressure FROM diabetes WHERE bloodpressure > 40 AND bloodpressure < 90)")
# mycursor.execute("SELECT age,insulin FROM diabetes WHERE age > 40 AND age IN (SELECT age FROM diabetes WHERE bmi > 30) ")
# out=mycursor.fetchall()
# from tabulate import tabulate
# # print(mycursor.description)
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## Window Function using Partitions ##

# mycursor.execute("""
#     SELECT Age, Pregnancies, COUNT(*) OVER (PARTITION BY Pregnancies ORDER BY Age DESC) as Countw
#     FROM diabetes
# """)
# mycursor.execute("""
#     SELECT DISTINCT(Pregnancies), COUNT(*) OVER (PARTITION BY Pregnancies ORDER BY Pregnancies DESC) as Countw
#     FROM diabetes
# """)
# mycursor.execute("""SELECT DISTINCT(Pregnancies),avg(Age) OVER (PARTITION BY pregnancies ORDER by pregnancies DESC ) as Countw FROM  diabetes """)
# out=mycursor.fetchall()
# from tabulate import tabulate
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## Rank Function ##

# mycursor.execute("""
#     SELECT Age, Pregnancies, BloodPressure, 
#            RANK() OVER (PARTITION BY Pregnancies ORDER BY BloodPressure DESC) as Rank
#     FROM diabetes
# """)
# out=mycursor.fetchall()
# from tabulate import tabulate
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

# mycursor.execute("""
#     SELECT Age, Pregnancies, BloodPressure, 
#            DENSE_RANK() OVER (PARTITION BY Pregnancies ORDER BY BloodPressure DESC) as DenseRank
#     FROM diabetes
# """)
# out=mycursor.fetchall()
# from tabulate import tabulate
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## GroupBy Function ## (Used for Aggregation funtion )

# mycursor.execute("SELECT Age,pregnancies,outcome,count(*) FROM diabetes GROUP BY Age,pregnancies ")
# #mycursor.execute("select count(*) from diabetes where pregnancies=16")
# out=mycursor.fetchall()
# from tabulate import tabulate
# print(tabulate(out,headers=[i[0] for i in mycursor.description],showindex="always",  tablefmt='psql'))

## Constraints ##

#NOT NULL
# mycursor.execute("CREATE TABLE stu1 (no INTEGER,name TEXT NOT NULL,school VARCHAR(20)) ")

# a=input()
# b=input()
# c=input()
# query="INSERT INTO stu1 (no,name,school) VALUES (%s,%s,%s)"
# mycursor.execute(query,(a,b,c))
# mydb.commit()


## Unique AND Check Constrain ##
# mycursor.execute("CREATE TABLE u (no INTEGER,name TEXT UNIQUE,school VARCHAR(20),age INT CHECK(age<18))")

# a=input()
# b=input()
# c=input()
# d=input()
# query="INSERT INTO u (no,name,school,age) VALUES (%s,%s,%s,%s)"
# mycursor.execute(query,(a,b,c,d))
# mydb.commit()
# duplicate entry error

## Primary Key and Foreign Key Constrains##

## Primary Key ##

# mycursor.execute("CREATE TABLE aadhardetails (name VARCHAR(30),ADDRESS VARCHAR(20),AADHARID INTEGER PRIMARY KEY)")
# mycursor.execute("INSERT INTO aadhardetails (name,address,aadharid) VALUES('Imam','Chennai',57941188)")
# mydb.commit()

## Foreign Key ##

# mycursor.execute("CREATE TABLE bankacc(name VARCHAR(20),type VARCHAR(2),accno INT PRIMARY KEY,aadhar INT ,FOREIGN KEY (aadhar)REFERENCES aadhardetails(aadharid))")
# mycursor.execute("INSERT INTO bankacc (name,type,accno,aadhar) VALUES('Imam','SB',1236847,57941188)")
# mydb.commit()

# mycursor.execute("CREATE TABLE pancard(name VARCHAR(20),dob INT,panid VARCHAR(16),aadhar INT ,FOREIGN KEY(aadhar) REFERENCES aadhardetails(aadharid),PRIMARY KEY(panid,aadhar))")
# mydb.commit()
# mycursor.execute("INSERT INTO pancard(name,dob,panid,aadhar) VALUES('nethaji',123,'BABPN78',2345678)")
# mydb.commit()

## Joins ##

# mycursor.execute("CREATE TABLE student(ID INT PRIMARY KEY,NAME VARCHAR(20),PH INT) ")
# mycursor.execute("INSERT INTO student (ID,NAME,PH) VALUES(1,'nethaji',12345)")
# mycursor.execute("INSERT INTO student (ID,NAME,PH) VALUES(2,'nirmal',123456)")
# mydb.commit()
# mycursor.execute("CREATE TABLE marks(ID INT ,maths int,phy INT,chem INT) ")
# mydb.commit()
# mycursor.execute("INSERT INTO marks (ID,maths,phy,chem) VALUES(2,91,81,50)")
# mydb.commit()

## INNER JOIN ##

# mycursor.execute("SELECT student.ID,marks.maths,marks.phy \
# FROM student \
# INNER JOIN marks ON student.ID = marks.ID")
# out=mycursor.fetchall()
# from tabulate import tabulate
# print(tabulate(out,  tablefmt='psql'))
# mydb.commit()



## Task 1 ##

# mycursor.execute("SELECT age,bmi,bloodpressure,outcome FROM diabetes WHERE outcome=1 AND age<=35 ")
# out=mycursor.fetchall()
# from tabulate import tabulate
# # print(mycursor.description)
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## Task 2 ##

# mycursor.execute("SELECT AVG(bloodpressure) as Avg_BP, COUNT(*) as Full_Count FROM diabetes WHERE outcome=1 AND pregnancies IN (12,13,17)")
# out=mycursor.fetchall()
# from tabulate import tabulate
# # print(mycursor.description)
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## Task 3 ##

# mycursor.execute("SELECT age, Bloodpressure, Insulin, outcome FROM diabetes WHERE Bloodpressure > 100 AND age in (SELECT age FROM diabetes WHERE Insulin BETWEEN 80 AND 120 AND outcome = 1)") 
# out=mycursor.fetchall()
# from tabulate import tabulate
# # print(mycursor.description)
# print(tabulate(out,headers=[i[0] for i in mycursor.description],  tablefmt='psql'))

## Task 4 ##

# mycursor.execute("SELECT COUNT(*) as count, pregnancies,outcome FROM diabetes WHERE pregnancies = 3 AND outcome = 0 GROUP BY pregnancies,outcome ")
# out=mycursor.fetchall()
# from tabulate import tabulate
# print(tabulate(out,headers=[i[0] for i in mycursor.description],showindex="always",  tablefmt='psql'))

