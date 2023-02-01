import csv
import stdiomask
import os 

def login(x):
    cc=[]
    file = open(x)
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    id=input("\nEnter your Acc number : \n").strip()
    password=stdiomask.getpass()
    if list([id,password]) in cc:
        return 1
        #edit
    else:
        os.system('cls')
        print("!!!  INCORRECT CREDENTIALS  !!!\n          try again \n")
        login(x)

def new(x):

    cc=[]
    file = open(x)
    reader = csv.reader(file)
    for line in reader:
        cc.append(line)
    
    cred=open(x,mode='a',newline='')
    writer=csv.writer(cred)
    id=input("Enter your Roll num : ").strip()
    s=1
    for i in cc:
        if id in i:
            s=0
            break
    if s==1:
        password=input("Enter your password : ")
        password2=input("Enter your password again : ")
        if password==password2:
            writer.writerow([id,password])
            print("!!! Account created successfully !!!") 
            os.system('cls')
            login(x)

    else:
        print("Account already exists !!!")
        new(x)



