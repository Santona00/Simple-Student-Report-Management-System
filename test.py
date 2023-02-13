import os
import re
import sys

import colorama
from colorama import Fore


def create_new_profile():

    name=input("Enter student name      :\t")
    if not re.match("^[A-Za-z]*$",name):
        print (Fore.RED+'\n\n              Error! Only letters a-z and dot is allowed!')
        sys.exit()
    gender=input("Enter Gender\n"
                 "(Male/Female/Others)    :\t")
    if not re.match("(Female)|(female)|(male)|(Male)|(Others)",gender) :
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        sys.exit()

    id = input("Enter student id        :\t")
    if not len(id)==9 and re.match("[0-9]*",id):
            print("Incorrect ID")
            print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
            print(Fore.RED + '\n\n            **Id must contain 9 digit only       ')
            sys.exit()

    Level=input("Enter Level            \n "
                "(1/2/3/4)              :\t")
    if not len(Level) == 1 and re.match("[1|2|3|4]", Level):
        print("Incorrect ID")
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        print(Fore.RED + '\n\n            **Level must contain 1 digit only    ')
        sys.exit()
    Term= input("Enter Term              \n   "
                "(1/2)                  :\t")
    if not len(Term) == 1 and re.match("[1|2]", Term):
        print("Incorrect ID")
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        print(Fore.RED + '\n\n              **Term must contain 1 digit only   ')
        sys.exit()
    phn = input("Enter phone no     :\t")

    if not len(phn) == 11 and re.match("(01)[1|2|3|4|5|6|7|8|9|0]*", phn):
        print("Incorrect ID")
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        print(Fore.RED + '\n\n       **Phone number must contain 11 digit only ')
        sys.exit()



    password = id
    L=[str(id),"\t",str(Level),"\t",str(Term),"\t",str(phn),"\t",gender,"\t",name]
    f = open("profiles.txt", "a")
    f.writelines(L)
    f.write("\n")
    f.close()


def view_profile(idd):
    y=idd
    f = open("profiles.txt","r")
    lines=f.readlines()
    print("ID--------Level-Term---Phone----Gender---Name")
    for line in lines:
        if line.find(y) != -1:
            print(line)

    f.close()

def delete_profile(del_id):


    with open("profiles.txt", "r") as inputs:
        with open("temp.txt", "w") as output:
            for line in inputs:
                if not line.strip("\n").startswith(str(del_id)):
                    output.write(line)
    os.replace('temp.txt', 'profiles.txt')

def update_profile(update_id):
    #update_id=input("Enter student id : \t")


    print("\n\n\n")
    print(Fore.LIGHTBLUE_EX + '       ┌──' + '────────────────────────────────────' + Fore.BLUE + '─┐')
    print(Fore.LIGHTBLUE_EX + '       │' + '                                      ' + Fore.BLUE + ' │')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '               UPDATE                  ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '                                       ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        1 >' + Fore.LIGHTYELLOW_EX + '   Name                     ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        2 >' + Fore.LIGHTYELLOW_EX + '   ID                       ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        3 >' + Fore.LIGHTYELLOW_EX + '   Gender                   ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        4 >' + Fore.LIGHTYELLOW_EX + '   Level                    ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        5 >' + Fore.LIGHTYELLOW_EX + '   Term                     ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        6 >' + Fore.LIGHTYELLOW_EX + '   Phone                    ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        7 >' + Fore.LIGHTYELLOW_EX + '   Result                   ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '   >>Select option (1/2/3/4/5/6/7)     ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '                                       ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       └──' + '────────────────────────────────────' + '─┘')

    view_profile(update_id)
    k=int(input("\n\n\t\t\t\tEnter :\t"))
    if k==1:
        p=input("Enter old name :\t")
        pp=input("Update name    :\t")
    elif k == 2:
        p=input("Enter old ID :\t")
        pp=input("Update ID    :\t")
    elif k == 3:
        p=input("Enter old gender :\t")
        pp=input("Update gender    :\t")
    elif k == 4:
        p=input("Enter old level :\t")
        pp=input("Update level    :\t")
    elif k == 5:
        p=input("Enter old term :\t")
        pp=input("Update term    :\t")
    elif k == 6:
        p=input("Enter old phone :\t")
        pp=input("Update phone    :\t")
    elif k == 7:
        p=input("Enter old result :\t")
        pp=input("Update result    :\t")


    f = open("profiles.txt","r")
    tmp=open("tempp.txt","w")
    tt=[]
    lines=f.readlines()
    for line in lines:
        if line.find(update_id) != -1:
            tt=line


    f.close()
    print(tt)

    tttt=tt.replace(str(p),str(pp))
    print(tttt)
    delete_profile(update_id)

    ff=open("profiles.txt","a")
    ff.writelines(tttt)







print("Create new profile")
create_new_profile()
print("view profile")
oo=input("enter id")
view_profile(oo)
print("delete profile")
xx=input("Enter id")
delete_profile(xx)
print("update profile")
up_id=input("Enter id")
update_profile(up_id)
