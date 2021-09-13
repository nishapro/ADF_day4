
import mysql.connector
from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os
import platform
import json
import logging

logging.basicConfig(filename="Adf_database.txt", filemode='a+',
                        format='%(asctime)s %(levelname)s-%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def Database():
    cnx=mysql.connector.connect(user='root',password='Nisha123',host='localhost',database='database')
    Cursor=cnx.cursor()
    Cursor.execute("")
    Cursor.close()
    cnx.close()

def clrscreen():
    if platform.system()=="Windows":
        print(os.system("cls"))

def user_details():
    try:
        cnx=mysql.connector.connect(user='root',password='Nisha123',host='localhost',database='database')
        Cursor = cnx.cursor()
        id=int(input("Enter the starting of the id:"))
        FirstName=input("Enter the first name of the user:")
        MidName=input("Enter the second name of the user:")
        LastName=input("Enter the last name of the user:")
        print("Enter date_of_birth (Date/month and year separately):")
        dd=int(input("Enter date: "))
        mm=int(input("Enter month:"))
        yy=int(input("Enter year:"))
        Gender=input("Enter the gender of an user:")
        nationality=input("Enter the nationality of an user")
        CurrentCity=input("Enter the Current city:")
        State=input("Enter state:")
        Qualification=input("Enter qualification:")
        salary=input("Enter salary:")
        pan=input("Enter pan")
        Pincode = input("Enter pincode:")
        Qry=("INSERT INTO request_info VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data=(id,FirstName,MidName,LastName,date(yy,mm,dd),Gender,nationality,CurrentCity,State,Qualification,salary,pan,Pincode)
        Cursor.execute(Qry,data)
        logging.info("request of the user has been submitted to the database")
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Request inserted in request info .")
    except:
        print("some error occured")
    cnx.close()

def menu():
    while True:
        print("\t\tUser input\n")
        print("====================")
        print("1. More user")
        print("2. Exit")
        choice=int(input("Enter choice between 1 to 2--------->"))
        if choice == 1:
            user_details()
        elif choice==2:
            break
        else:
            print("Wrong choice........Enter your choice again")
            x=input("Press any key to continue")
    logging.info("iterations has been created for more user")

def State(stat):
    if stat=="Andhra Pradesh" or stat=="bihar":
        logging.info("state is checked")
        return True

def salary(sal):
    if sal>10000 and sal<90000:
        logging.info("salary is checked")
        return True

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
    logging.info("age has been checked")
    return age

def response_info(id,res):
    cnx = mysql.connector.connect(user='root', password='Nisha123', host='localhost', database='database')
    Cursor = cnx.cursor()
    Qry1=("INSERT INTO response_info VALUES (%s,%s)")
    data1=(id,res)
    Cursor.execute(Qry1, data1)
    cnx.commit()
    Cursor.close()
    cnx.close()
    print("Response inserted in response info .")
    logging.info("response has been saved to the database")

def response_fetch():
    cnx = mysql.connector.connect(user='root', password='Nisha123', host='localhost', database='database')
    Cursor = cnx.cursor()
    query = "select * from response_info"
    Cursor.execute(query)
    table = Cursor.fetchall()
    for row in table:
        print(row)
    Cursor.close()
    cnx.close()

def eligibility():
    cnx = mysql.connector.connect(user='root', password='Nisha123', host='localhost', database='database')
    Cursor = cnx.cursor()
    query = "select * from request_info"
    Cursor.execute(query)
    table = Cursor.fetchall()
    print('\n list of the User:')
    for row in table:
        if row[5].lower()=='male':
            if calculateAge(row[4]) >21:
                if row[6].lower()== 'indian' or row[6].lower()== 'american':
                    if State(row[8]):
                        if salary(row[10]):
                            print(json.dumps({'Response_id': row[0], 'Response': 'Success'}))
                        else:
                            print(json.dumps({'Response_id': row[0], 'Response': 'Validation error', 'reason': 'Salary is not as expected'}))
                    else:
                        print(json.dumps({'Response_id': row[0], 'Response': 'Validation error', 'reason': 'State is not as expected'}))
                else:
                    print(json.dumps({'Response_id': row[0], 'Response': 'Validation error', 'reason': 'Country is not as expected'}))
            else:
                print(json.dumps({'Response_id': row[0], 'Response': 'Validation error', 'reason': 'Age is not as expected'}))
        else:
            print(json.dumps({'Response_id':row[0], 'Response':'validation error','reason':'Gender as not expected'}))
        #response_info(row[0], res)
    logging.info("eligibility has been checked")
    Cursor.close()
    cnx.close()

if __name__ == "__main__":
    menu()
    eligibility()
    response_fetch()

























