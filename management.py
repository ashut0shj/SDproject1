import csv
import os

def display():
    file = open(x)
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)

    a='''          Welcome

        1 : Mess
        2 : Hostel
        3 : Library 
        4 : Academic
        5 : Ragging 
        6 : All          '''
    print(a)
    c=int(input("\n\n  Enter your choice : "))
    if c!=6:
        for i in range