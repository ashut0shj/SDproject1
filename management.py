import csv
import os
from prettytable import PrettyTable

def display(id):
    cc=[]
    file = open('complaints.csv')
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    cond='y'
    while(cond=='y'):
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
        table=PrettyTable(['Acc no.','Complaints'])
        for i in cc:
            if c==int(i[1]):
                table.title= 'Mess'
                table.add_row([i[0],i[2]])
            elif c==int(i[1]):
                table.title= 'Hostel'
                table.add_row([i[0],i[2]])
            elif c==int(i[1]):
                table.title= 'Library'
                table.add_row([i[0],i[2]])
            elif c==int(i[1]):
                table.title= 'Academic'
                table.add_row([i[0],i[2]])
            elif c==int(i[1]):
                table.title= 'Ragging'
                table.add_row([i[0],i[2]])
        print(table)
        cond=input('''\n\nDo you want to return back  ? (y/n)''').strip()

