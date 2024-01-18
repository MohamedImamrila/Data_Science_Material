##**Building the connection to server to python**##

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="", 
# )

# print(mydb)

# mycursor = mydb.cursor(buffered=True)


# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


## Creating the database using python ##
  
# mycursor.execute("CREATE DATABASE barath")
# mycursor.execute("DROP DATABASE barath")

## Creating a table by using python code ##

# mycursor.execute("USE barath")
# mycursor.execute("CREATE TABLE guvi (student VARCHAR(20),course VARCHAR(20))")
# mycursor.execute("CREATE TABLE barath.lucky (salary INT(6), Weight DECIMAL(5,3), Insurance BOOLEAN)")
# mydb.commit()

## Inserting a data into table ##

# mycursor.execute("INSERT INTO barath.lucky (salary,Weight,Insurance) VALUES(1323,1.064712,1)")
# mydb.commit()

## Altering (or) adding a column in existing table ##

# mycursor.execute("ALTER TABLE barath.lucky ADD covid VARCHAR(5) FIRST") 
# mydb.commit()
# mycursor.execute("ALTER TABLE barath.lucky ADD covid_status VARCHAR(5) AFTER covid") 
# mydb.commit()

## DROP COLUMN EXAMPLE ##

# mycursor.execute("ALTER TABLE barath.lucky DROP COLUMN covid_status")
# mydb.rollback()

## UPDATE THE COLUMN IN TABLE ##

# mycursor.execute("UPDATE barath.lucky SET covid = 'Yes' WHERE insurance = 1")
# mydb.commit()

## Modifying the existing table ##

# mycursor.execute('ALTER TABLE barath.lucky MODIFY covid INT')
# mydb.commit()

## Rename Column ##

# mycursor.execute('ALTER TABLE barath.lucky CHANGE COLUMN covid covidnew INT')
# mydb.commit()

## Show tables ##

# mycursor.execute('SHOW TABLES FROM barath')

# for x in mycursor:
#     print(x)

## DELETING A WHOLE ROW IN A TABLE ##

# mycursor.execute("DELETE FROM barath.lucky WHERE covid is NULL")
# mydb.commit()

## Rename table name we can use this command for changeing the database from one to another ## 

# mycursor.execute('RENAME TABLE barath.lucky TO barath.vikram')
# mydb.commit()

#truncate(delete all elements without deleting the table structure)

# mycursor.execute("TRUNCATE vikram")
# mydb.commit

# mycursor.execute("CREATE TABLE date (datein DATE)")

#mycursor.execute("INSERT INTO date (datein) VALUES ( CURDATE())")
# mycursor.execute("INSERT INTO date (datein) VALUES ( CURDATE())")
# mycursor.execute("INSERT INTO date (datein) VALUES ( CURRENT_DATE())")
# mycursor.execute("INSERT INTO date (datein) VALUES (CURTIME())")
# mycursor.execute("INSERT INTO date (datein) VALUES (CURRENT_TIMESTAMP())")
# mycursor.execute("INSERT INTO date (datein) VALUES (CURRENT_TIME())")
# mycursor.execute("INSERT INTO date (datein) VALUES (NOW())")
# mydb.commit()

#whatever date format given into DATE datatypw will consider in the sameway

# mycursor.execute("CREATE TABLE datestrin (datein VARCHAR(255))")

# mycursor.execute("INSERT INTO datestrin (datein) VALUES ( CURDATE())")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES ( CURRENT_DATE())")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (CURTIME())")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (CURRENT_TIMESTAMP())")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (CURRENT_TIME())")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (NOW())")#date and time
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (MONTHNAME(NOW()))")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (DAYNAME(NOW()))")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (HOUR(NOW()))")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (MINUTE(NOW()))")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (DATE_ADD(NOW(),INTERVAL -10 DAY))")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (DATE_FORMAT(NOW(),'%W %D %M %Y %T %H'))")
# mycursor.execute("INSERT INTO datestrin (datein) VALUES (UTC_DATE())")#UTC_TIME,UTC_TIMESTAMP
# mydb.commit()
