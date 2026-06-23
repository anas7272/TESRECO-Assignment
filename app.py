import copy #for shallow or deep cpy
import time # for performance cal*
from abc import ABC , abstractmethod #for abstract class
from functools import reduce #for functional prog = reduce()
import csv , os #to save ,srch and del
import threading # for simultanous thread / process
import time 
from multiprocessing import Process # for multi processing
import logging

#Exception Handling
class InvalidEmailError(Exception):
    pass
class InvalidDurationError(Exception):
    pass


class Intern:
    def __init__(self, intern_id, name, email, domain, duration):

        #validation before registration
        if "@gmail.com" not in email:
            raise InvalidEmailError("Invalid email address.")
        if duration <= 0:
            raise InvalidDurationError("Duration must be a positive integer.")


        self.intern_id = intern_id #all in init => instance attribute
        self.name = name
        self.email = email
        self.domain = domain
        self.duration = duration


        #to save data in csv
        file_exists = os.path.exists("interns.csv")
        with open("interns.csv" , "a" , newline= "") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "intern_id",
                    "name",
                    "email",
                    "domain",
                    "duration"
                ])
            
            writer.writerow([
                self.intern_id,
                self.name,
                self.email,
                self.domain,
                self.duration

            ])


    
    def __str__(self): # we use this to print or return the object in a string format , if it is not present then it will return the object memory location.
        return f"""
        Intern ID: {self.intern_id},
        Name: {self.name},
        Email: {self.email}, 
        Domain: {self.domain}, 
        Duration: {self.duration}"""

    # Performance Calculator

    def greeting(fx):
        def wrapper(self, *args, **kwargs):
            start_time = time.time()
            result = fx(self, *args, **kwargs)
            end_time = time.time()

            print (f" Function Name: {fx.__name__}")
            print(f"Execution time: {end_time - start_time:.3f} seconds")
            print(f"Result : {result}")
            return result
        return wrapper

    @greeting
    def performance_calculator(self, task_score, attendance , in_house_projects ):
        result = (task_score * 0.5) + (attendance * 0.3) + (in_house_projects * 0.2) #MAm didnt mention formula so an example i wrote !
        return result

    
    counter = 1
    def __iter__(self):
        return self
    def __next__(self):
        intern_id = f"TES{Intern.counter:03d}"
        Intern.counter += 1
        return intern_id
    
    # Generator Function

    def certificate_gen(self,name):
        yield f"Certificate Generated for {name}"
    
    

# Shallow Copy vs Deep Copy


#Shallow Copy : shallow copy work good in 1D but if we got 2D,3D... 
#               it gets useless bcz after 1d it make operation on both 
#               copies.
anas_project = [ 
    ["Anas" , ["Python", "MCP","RAG","AI-agents"]]
    ]
rohan_project = copy.copy(anas_project) #Shallow Copy

rohan_project[0][1][0] = "Java"
# print(anas_project,rohan_project)

#operation will be affect on both =
#anas_project = [['Anas', ['Java', 'MCP', 'RAG', 'AI-agents']]] 
#rohan_project =  [['Anas', ['Java', 'MCP', 'RAG', 'AI-agents']]]



#Deep Copy = but the deep copy resolve the prob of
#            shallow copy for n-dimension 


anas_project = [ 
    ["Anas" , ["Python", "MCP","RAG","AI-agents"]]
    ]
rohan_project = copy.deepcopy(anas_project) #Shallow Copy

rohan_project[0][1][0] = "Java"
# print(anas_project,rohan_project)

#anas_project = [['Anas', ['Python', 'MCP', 'RAG', 'AI-agents']]] 
#rohan_project =  [['Anas', ['Java', 'MCP', 'RAG', 'AI-agents']]]


#Multiple Inheritance

class Person:
    pass
class Employee:
    pass
class Mentor:
    pass

class TESRECOMentor(Person,Employee,Mentor):
    pass

# print(TESRECOMentor.mro()) 
# it will show the whole heirarchy  that how he searches 
# for fxn and attribute in each parent claSS


#Abstract Class


class Report(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class AttendanceReport(Report):

    def generate_report(self): #bcz of abstract method child has to be create that class tooo , it can inherit from parent
        print("Attendance Report Generated")


class PerformanceReport(Report):

    def generate_report(self):
        print("Performance Report Generated")


# Lambda & Functional Programming

score = [78, 90, 65, 88, 95]

#Analysis

#map() : Applies a function/operat*  to every element.
cgpa = list(map(lambda x: x/10 , score))

#filter() : if condition true then only stores
passfail = list(filter(lambda x : (x/10) >= 7.0 , score))

# reduce() : reduces the list values to a single valu
total = reduce(lambda a,b : a+b , score)


# File Handling

def search(column , value):
    with open("interns.csv" , "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row[column] == value:
                print("Rcored Found: ")
                print(row)
                return
        print("Record Not Found")

def delete(column , value):
    rows = []

    with open("interns.csv" , "r") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames#to store field name
        for row in reader:
            if row[column] != value:
                rows.append(row)
    with open("interns.csv" , "w" , newline="") as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)
    print("Record Deleted !")


#Multithreading

def Attendance_Processing():
    for i in range(5):
        print(f"Student {i} is Present.")
        time.sleep(1)
     

def Certificate_Generation():
    for i in range(5):
        print(f"Certificate for intern {i} is Completed.")
        time.sleep(1)
     
t1 = threading.Thread(target=Attendance_Processing)
t2 = threading.Thread(target=Certificate_Generation)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Finish")



#Multiprocessing



def ai_intern(attendance , tasks_completed , task_score):
    for i in range(5):
        score = ( attendance * 0.3 + tasks_completed * 0.3 + task_score * 0.4 )
        print(f"For {i} AI Intern Score is {score}.")
        time.sleep(2)
    
def java_intern(attendance , tasks_completed , task_score):
    for i in range(5):
        score = ( attendance * 0.3 + tasks_completed * 0.3 + task_score * 0.4 )
        print(f"For {i} JAVA Intern Score is {score}.")
        time.sleep(2)

if __name__ == "__main__":

    p1 = Process(target=ai_intern,args=(90, 8, 85))
    p2 = Process(target=java_intern,args=(40, 8, 55))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()
    # print("finish")


#logging files

logging.basicConfig(
    filename="tesreco.log",
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#login events
def login(username):
    logging.info(
    f"User {username} logged in."
    )
    print("Login Successful")

#Error logging

try :
    result = 10/0
except Exception as e:
    logging.error(
        f"Error Occurred: {e}"
    )

#Report Genration 

def generate_report():
    logging.info(
        "Attandence Report Genration"
    )

    print("Report Genrated")


#SQLite Integration

import sqlite3

conn = sqlite3.connect("interns.db")
cursor = conn.cursor()


cursor.executescript("""
CREATE TABLE IF NOT EXISTS Interns(
    intern_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    domain TEXT
);

CREATE TABLE IF NOT EXISTS Mentors(
    mentor_id INTEGER PRIMARY KEY,
    name TEXT,
    specialization TEXT
);
""")

conn.commit()
conn.close()


#CRUD operations

#Create

conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

cursor.execute("""
               INSERT INTO Interns
               values (?, ?, ?, ?)
               """,
               (101, "Anas", "anas@gmail.com", "AI/ML"))

conn.commit()
conn.close()

#read
import sqlite3
conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM Interns"
)

records = cursor.fetchall()

for row in records:
    print(row)

conn.close()

#update
import sqlite3
conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

cursor.execute(
    """
UPDATE Interns
SET domain=?
WHERE intern_id=? """,
("Data Science" , 101)
)

conn.commit()
conn.close()

#delete
import sqlite3
conn = sqlite3.connect("interns.db")
cursor = conn.cursor()

cursor.execute("""
        DELETE FROM Interns
        WHERE intern_id=? """,
        (101,))

conn.commit()
conn.close()


# Project Structure

