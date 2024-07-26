print("=================================================================================")
print(" \t ANDREW VIVAN.X \t 21BBTCS026 \t CUSTOMER ORDER DATABASE PROJECT")
print("=================================================================================")
print("\n")
import sqlite3
connection = sqlite3.connect('customer_order_andrewvivan.db')
cursor = connection.cursor()
print("  \t\t DATABASE CREATED SUCCESSFULLY \t\t ")
print("\n")
#========================= ORDERS TABLE =============================================================================================
cursor.execute("""
               CREATE TABLE orders(order_id  INTEGER NOT NULL PRIMARY KEY,
               user_id INTEGER,
               status varchar(225),
               created_at BLOB,
               FOREIGN KEY(user_id) REFERENCES users(user_id))
               """)
connection.commit()
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (101,201,'delivered'    ,'1/1/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (102,202,'delivered'    ,'2/2/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (103,203,'not delivered','3/3/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (104,204,'delivered'    ,'4/4/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (105,205,'not delivered','5/5/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (106,206,'delivered'    ,'6/6/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (107,207,'delivered'    ,'7/7/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (108,208,'not placed'   ,'8/8/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (109,209,'delivered'    ,'9/9/23')")
cursor.execute("INSERT INTO orders (order_id, user_id,  status, created_at) VALUES (110,210,'not placed'   ,'10/10/23')")
print("=> Values Inserted Into (orders) Table successfully")
print("\n")
connection.commit()
#========================== PRODUCTS TABLE ==========================================================================================
cursor.execute("""
               CREATE TABLE products(product_id INTEGER NOT NULL PRIMARY KEY,
               product_name varchar(225),
               merchants_id INTEGER,
               price INTEGER ,
               status varchar(225),
               created_at BLOB,
               FOREIGN KEY(merchants_id) REFERENCES merchants(merchants_id))
               """)
connection.commit()
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1001,1101,'soap',30, 'available','1/1/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1002,1102,'pen',10, 'available','1/1/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1003,1103,'book',40, 'available','1/1/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1004,1104,'gum',5, 'available','1/1/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1005,1105,'icecream',45, 'available','2/2/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1006,1106,'chocolate',50, 'available','2/2/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1007,1107,'cookies',15, 'available','2/2/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1008,1108,'brush',25, 'available','3/3/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1009,1109,'towel',60, 'available','3/3/23')")
cursor.execute("INSERT INTO products (product_id,merchants_id,product_name, price, status, created_at) VALUES (1010,1110,'shampo',20, 'available','3/3/23')")
print("=> Values Inserted Into (products) Table successfully")
print("\n")
connection.commit()
#============================ MERCHANTS TABLE =======================================================================================
cursor.execute("""
               CREATE TABLE merchants(merchants_id INTEGER,
               merchant_name varchar(225),admin_id INTEGER,country_code,
               created_at BLOB, FOREIGN KEY(admin_id) REFERENCES users(user_id),
               FOREIGN KEY(country_code)REFERENCES countries(country_code))
               """)
connection.commit()
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1101,'luffy',201,81,'1/1/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1102,'zoro',202,82,'2/2/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1103,'sanji',203,83,'3/2/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1104,'nami',204,84,'3/3/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1105,'usoop',205,85,'4/4/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1106,'chopper',206,86,'5/2/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1107,'robin',207,87,'6/1/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1108,'franky',208,88,'3/5/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1109,'brook',209,89,'7/6/19')")
cursor.execute("INSERT INTO merchants (merchants_id,merchant_name,admin_id,country_code,created_at) VALUES (1110,'jimbe',210,90,'1/4/19')")
print("=> Values Inserted Into (merchants) Table successfully")
print("\n")
connection.commit()
#============================= ORDER_ITEMS TABLE ====================================================================================
cursor.execute("""
               CREATE TABLE order_items (
               order_id INTEGER,product_id INTEGER,quantity varchar(225),
               FOREIGN KEY(order_id) REFERENCES orders(order_id),
               FOREIGN KEY(product_id) REFERENCES products(product_id)
               )            
               """)
connection.commit()
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (101,1101,1)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (102,1102,2)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (103,1103,2)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (104,1104,4)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (105,1105,3)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (106,1106,5)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (107,1107,5)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (108,1108,7)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (109,1109,3)")
cursor.execute("INSERT INTO order_items(order_id,product_id,quantity) VALUES (110,1110,8)")
print("=> Values Inserted Into (order_items) Table successfully")
print("\n")
connection.commit()
#============================== USERS TABLE =========================================================================================
cursor.execute("""
               CREATE TABLE users(user_id INTEGER PRIMARY KEY,
               name varchar(225),
               email BLOB,
               gender varchar(255),
               DOB BLOB,
               country_code INTEGER,
               created_at BLOB,FOREIGN KEY(country_code)REFERENCES countries(country_code))
               """)
connection.commit()
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (201,'shinchan','shinchan@gmail.com','MALE','1-1-04',81,'11-1-22')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (202,'himawari','himawari@gmail.com','FEMALE','2-2-05',82,'12-2-20')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (203,'kazama','kazama@gmail.com','MALE','3-3-04',83,'13-3-21')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (204,'nanichan','nanichan@gmail.com','FEMALE','4-4-04',84,'14-4-20')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (205,'masao','masao@gmail.com','MALE','5-5-05',85,'15-5-23')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (206,'bochan','bochan@gmail.com','MALE','6-6-06',86,'16-6-23')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (207,'doremon','doremon@gmail.com','MALE','29-2-04',87,'17-7-20')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (208,'doreme','doreme@gmail.com','FEMALE','26-5-03',88,'18-8-21')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (209,'nobita','nobita@gmail.com','MALE','9-9-04',89,'19-9-21')")
cursor.execute("INSERT INTO users(user_id,name,email,gender,DOB,country_code,created_at) VALUES (210,'sizuka','sizuka@gmail.com','FEMALE','10-10-06',90,'20-10-23')")
print("=> Values Inserted Into (users) Table successfully")
print("\n")
connection.commit()
#============================= COUNTRIES TABLE ======================================================================================
cursor.execute("""
               CREATE TABLE countries (country_code INTEGER PRIMARY KEY,
               country_name varchar(225),
               continent_name varchar(225))
               """)
connection.commit()
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (81,'japan','asia')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (82,'china','asia')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (83,'koria','asia')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (84,'nigeria','africa')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (85,'canada','north america')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (86,'mexico','north america')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (87,'brazil','south america')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (88,'india','asia')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (89,'pakistan','asia')")
cursor.execute("INSERT INTO countries (country_code, country_name,continent_name) VALUES (90,'sri lanka','asia')")
print("=> Values Inserted Into (countries) Table successfully")
print("\n")
connection.commit()

