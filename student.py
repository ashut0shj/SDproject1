import csv
import os 
from prettytable import PrettyTable
import pandas as pd


x='complaints.csv'
def complaintreg():
    a='''          Welcome

        1 : Mess complaint
        2 : Hostel complaint
        3 : Library complaint
        4 : Academic complaint
        5 : Ragging related'''
    print(a)
    c=int(input("\n\n  Enter your choice : "))
    os.system('cls')
    return c

def display(id):
    cc=[]
    t=['','Mess','Hostel',"Library",'Academic','Ragging']
    table=PrettyTable(["Uid",'Category','Complaint','Status'])
    file = open('complaints.csv')
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    cc.pop(0)
    for i in cc:
        try:
            if int(id)==int(float(i[1])):
                table.add_row([i[0],t[(int(i[2]))],i[3],i[4]])
        except:
            aaaaa=4
            print(".")
    print(table)

def approve(id):
    display(id)
    df=pd.read_csv('complaints.csv')
    cn=(int(input("\nEnter the Uid of complaint to be approved : \n")))
    df.loc[cn, 'status'] = '+s'
    df.to_csv("complaints.csv", index=False)
    print(" \n!!! Approved !!!")


def stud(id):
    cond='y'
    while(cond=='y'):
        os.system('cls')
        cc=[]
        file = open(x)
        reader = csv.reader(file)
        for line in reader:
            cc.append(line)

        cred=open(x,mode='a',newline='')
        writer=csv.writer(cred)
        #writer.writerow([id,password])
        a='''          Welcome

                1 : Register new complaint
                2 : View previous complaints
                3 : Approve a complaint'''
        print(a)
        c=int(input("\n\n Enter your choice : "))
        os.system('cls')
        if c==1:
            s=complaintreg()
            comp=input('\n\n   Enter your complaint : \n\n   ')
            writer.writerow([str(int(cc[-1][0])+1),id,s,comp,''])
            print('\n\nComplaint registered !!!')
        elif c==2:
            display(id)
            cond=input('''\n\nDo you want to return back to home page ? dis (y/n)''').strip()
        elif c==3:
            approve(id)




