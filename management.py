import csv
import os
from prettytable import PrettyTable
import pandas as pd

def display(id):
    cond='y'
    while(cond=='y'):
        cc=[]
        file = open('complaints.csv')
        reader = csv.reader(file)
        for line in reader:
            cc.append(line)
        cc.pop(0)
    
        os.system('cls')
        a='''          Welcome

            1 : Mess
            2 : Hostel
            3 : Library 
            4 : Academic
            5 : Ragging 
            6 : All          '''
        print(a)
        c=int(input("\n\n  Enter your choice : "))
        table=PrettyTable(['Uid','Acc no.','Complaints','Status'])
        for i in cc:
            if c==int(i[2]):
                table.title= 'Mess'
                table.add_row([i[0],i[1],i[3],i[4]])
            elif c==int(i[2]):
                table.title= 'Hostel'
                table.add_row([i[0],i[1],i[3],i[4]])
            elif c==int(i[2]):
                table.title= 'Library'
                table.add_row([i[0],i[1],i[3],i[4]])
            elif c==int(i[2]):
                table.title= 'Academic'
                table.add_row([i[0],i[1],i[3],i[4]])
            elif c==int(i[2]):
                table.title= 'Ragging'
                table.add_row([i[0],i[1],i[3],i[4]])
        print(table)
        c2=input("\nDo you want to approve any complaints ? (y/n)\n")
        if c2=='y':
            approve(id)
        cond=input('''\n\nDo you want to return back  ? (y/n)''').strip()

def approve(id):
    df=pd.read_csv('complaints.csv')
    cn=(int(input("\nEnter the Uid of complaint to be approved : \n")))
    df.loc[cn, 'status'] = '+'
    df.to_csv("complaints.csv", index=False)
    print(" \n!!! Approved !!!")

