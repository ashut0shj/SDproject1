import csv
import os 

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
    t=['','Mess','Hostel',"Library",'Academic','Ragging']
    print(t[int(i[1])],'  :  ',i[2])

def display(id):
    cc=[]
    file = open(x)
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    for i in cc:
        try:
            if id==int(i[0]):
                printer(i)
        except:
            ppppp=00000
def stud(id):
    cond='y'
    while(cond=='y'):
        os.system('sys')
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
            os.system('cls')
            comp=input('\n\n   Enter your complaint : \n\n   ')
            writer.writerow([id,s,comp])
            print('\n\nComplaint registered !!!')
        elif c==2:
            display(id)



