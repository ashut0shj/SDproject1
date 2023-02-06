import csv
import os 
from prettytable import PrettyTable

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
def printer(i):
    print('lllll')
    t=['','Mess','Hostel',"Library",'Academic','Ragging']
    print(t[int(i[1])],'  :  ',i[2])
    

def display(id):
    cc=[]
    t=['','Mess','Hostel',"Library",'Academic','Ragging']
    table=PrettyTable(['Category','Complaint'])
    file = open('complaints.csv')
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    for i in cc:
        table.add_row([t[(int(i[1]))],i[2]])
    print(table)

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
                2 : View previous complaints'''
        print(a)
        c=int(input("\n\n Enter your choice : "))
        os.system('cls')
        if c==1:
            s=complaintreg()
            comp=input('\n\n   Enter your complaint : \n\n   ')
            writer.writerow([id,s,comp])
            print('\n\nComplaint registered !!!')
        elif c==2:
            display(id)
            cond=input('''\n\nDo you want to return back to home page ? dis (y/n)''').strip()



