import mysql.connector
my_db=mysql.connector.connect(
    host="host_name",#change this to your host name
    user="root_user",#change this to your root user name 
    password="password"# change this password with your password
    )
mycursor=my_db.cursor()
mycursor.execute("create database vote;")
mycursor.execute("use vote;")
mycursor.execute("""CREATE TABLE VOTER (
    VID VARCHAR(11) PRIMARY KEY,
    NAME VARCHAR(25),
    ADDRESS VARCHAR(25),
    GENDER VARCHAR(7),
    HAS_VOTED TINYINT(1) DEFAULT 0,
    ADHAR_NO INT(12)
);
""")
mycursor.execute("""CREATE TABLE admin (
    user_name VARCHAR(25) PRIMARY KEY,
    password VARCHAR(25) UNIQUE
);""")
mycursor.execute("""CREATE TABLE candidates (
    sl_no VARCHAR(5) PRIMARY KEY,
    name VARCHAR(25) NOT NULL
);""")
mycursor.execute("""CREATE TABLE votes (
    sl_no VARCHAR(5),
    total_votes INT DEFAULT 0,
    FOREIGN KEY (sl_no) REFERENCES candidates(sl_no)
);""")
print("successful")
