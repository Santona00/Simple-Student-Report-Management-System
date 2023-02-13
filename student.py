import colorama
from colorama import Fore
import os
import re
import sys



def select():
    print("\n\n\n")
    print(Fore.LIGHTBLUE_EX + '       ┌──' + '────────────────────────────────────────────' + Fore.BLUE + '─┐')
    print(Fore.LIGHTBLUE_EX + '       │' + '                                              ' + Fore.BLUE + ' │')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        Student Report Management System       ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '                                               ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        1 >' + Fore.LIGHTYELLOW_EX + '         Admin                      ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTGREEN_EX + '        2 >' + Fore.LIGHTYELLOW_EX + '         Student                    ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '───────────────────────────────────────────────' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '              >>Select option (1/2)            ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '                                               ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       └──' + '────────────────────────────────────────────' + '─┘')
    x = int(input("\n\n\t\t\t\tEnter :\t"))
    try:
        if x == 1:
            admin_Panel()
        else:
            std_Panel()
        print("\n\n\n")
    except:
        print(Fore.LIGHTRED_EX+"Invalid or incorrect input!!")


def admin_Panel():
    print("\n\n\n")
    print(
        Fore.LIGHTBLUE_EX + '       ┌──' + '=========================================================' + Fore.BLUE + '─┐')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '                                                            ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                       Admin Section                        ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '                                                            ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  1 >  Create New Student Profile           ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  2 >  View Student Profile                 ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  3 >  Update Student Result                ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  4 >  Delete Student Profile               ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  5 >  View All Profile                     ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  6 >  LogOut                               ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                >>Select option (1/2/3/4/5/6)               ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '                                                            ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '============================================================' + '│')
    print(
        Fore.LIGHTBLUE_EX + '       └──' + '─────────────────────────────────────────────────────────' + '─┘')
    call_admin()


def call_admin():
    std_choice = int(input("\n\n\t\t\t\tEnter :\t"))
    try:
        while True:
            if std_choice == 1:
                create_new_profile()
                print(Fore.LIGHTGREEN_EX + '\n\n                                      New Profile created!')
                print(Fore.LIGHTBLUE_EX + '\n\n>>     Choose another option : ')
                admin_Panel()
            elif std_choice == 2:
                yy = input("Enter student ID :\t")
                view_profile(yy)
                print(Fore.LIGHTBLUE_EX + '\n\n>>       Choose another option :  ')
                admin_Panel()
            elif std_choice == 3:

                up_profile()
                print(Fore.LIGHTGREEN_EX + '\n\n                                      Profile Updated!')
                print(Fore.LIGHTBLUE_EX + '\n\n>>     Choose another option : ')
                admin_Panel()
            elif std_choice == 4:
                del__id = input("Enter student id : \t")
                delete_profile(del__id)
                #print(Fore.LIGHTRED_EX + '\n\n                                      Profile Deleted!')
                print(Fore.LIGHTBLUE_EX + '\n\n>>     Choose another option : ')
                admin_Panel()
            elif std_choice == 5:
                view_all_profile()
                print(Fore.LIGHTBLUE_EX + '\n\n>>       Choose another option :  ')
                admin_Panel()
            elif std_choice == 6:
                print(Fore.RED + 'Logged Out!')
                break
        select()
    except:
        print(Fore.LIGHTRED_EX+"Invalid or incorrect input!!")



def create_new_profile():

    name=input("Enter student name      :\t")
    if not re.match("^[a-zA-Z ]*$",name):
        print (Fore.RED+'\n\n              Error! Only letters A-Z and dot is allowed!')
        sys.exit(create_new_profile())
    gender=input("Enter Gender\n"
                 "(Male/Female/Others)    :\t")
    if not re.match("(Female)|(female)|(male)|(Male)|(Others)",gender) :
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        sys.exit(Fore.LIGHTYELLOW_EX+create_new_profile())

    id = input("Enter student id        :\t")
    if not len(id)==9 and re.match("[0-9]*",id):
            print("Incorrect ID")
            print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
            print(Fore.RED + '\n\n            **Id must contain 9 digit only       ')
            sys.exit(Fore.LIGHTYELLOW_EX +create_new_profile())
    f = open("profiles.txt", "r")
    lines = f.readlines()
    for line in lines:
        if line.find(id) != -1:
            print(Fore.LIGHTRED_EX + "This id already exists!!\n\nGive a new ID!")
            quit(Fore.LIGHTYELLOW_EX+create_new_profile())
            break

    f.close()


    Level=input("Enter Level            \n "
                "(1/2/3/4)              :\t")
    if not re.match("(1)|(2)|(3)|(4)", Level):
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        print(Fore.RED + '\n\n            **Level must contain 1 digit only    ')
        sys.exit(Fore.LIGHTYELLOW_EX +create_new_profile())

    Term=input("Enter Term              \n   "
                "(1/2)                :\t")
    if not re.match("(1)|(2)", Term):
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        print(Fore.RED + '\n\n              **Term must contain 1 digit only   ')
        sys.exit(Fore.LIGHTYELLOW_EX +create_new_profile())

    phn =input("Enter phone no          :\t")
    if not len(phn) == 11 and re.match("(01)[0-9]*", phn):
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        print(Fore.RED + '\n\n       **Phone number must contain 11 digit only ')
        sys.exit(Fore.LIGHTYELLOW_EX +create_new_profile())

    Result =input("Enter Result            :\t")
    float_res=float(Result)
    if not len(Result) == 4 and float_res>4.00 :
        print(Fore.RED + '\n\n              Error! Invalid or Incorrect input !')
        print(Fore.RED + '\n\n            **Result must contain 4 digit only   ')
        sys.exit(Fore.LIGHTYELLOW_EX +create_new_profile())



    L=[str(id),"\t",str(Level),"\t",str(Term),"\t",str(phn),"\t",gender,"\t",Result,"\t",name]
    f = open("profiles.txt", "a")
    f.writelines(L)
    f.write("\n")
    f.close()
    admin_Panel()



def view_profile(y):

    f = open("profiles.txt", "r")
    lines = f.readlines()
    for line in lines:
        if line.find(y) != -1:
            print(Fore.LIGHTWHITE_EX + '\n\nID--------Level-Term---Phone----Gender--Result---Name')
            print(Fore.LIGHTYELLOW_EX+line)
            quit(admin_Panel())
    f.close()
    print(Fore.LIGHTRED_EX+"\n\n                          There is no profile associated with ID "+y+"!!")
    id_again=input("\n\nEnter student ID :\t")
    view_profile(id_again)


def view_Update_profile(y):

    f = open("profiles.txt", "r")
    lines = f.readlines()
    for line in lines:
        if line.find(y) != -1:
            print(Fore.LIGHTWHITE_EX + '\n\nID--------Level-Term---Phone----Gender--Result---Name')
            print(Fore.LIGHTYELLOW_EX+line)
            return 1

    f.close()

def view_all_profile():
    print(Fore.LIGHTYELLOW_EX+'-------------------------------------ALL STUDENT PROFILE--------------------------------------')
    f = open("profiles.txt", "r")
    lines = f.readlines()
    print(Fore.LIGHTWHITE_EX +'\n\n-----------'+ 'ID-----Level-Term---Phone----Gender--Result-------Name')

    for line in lines:
        print(Fore.LIGHTYELLOW_EX+str(lines.index(line)+1)+'       '+line)

    f.close()



def up_profile():

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

    up_id = input("Enter student id : \t")
    update_profile(up_id)


def delete_up_profile(del_id):


    with open("profiles.txt", "r") as inputs:
        with open("temp.txt", "w") as output:
            for line in inputs:
                if not line.strip("\n").startswith(str(del_id)):
                    output.write(line)
    if os.path.getsize('temp.txt')==0:
        print(os.path.getsize('temp.txt'))
        print(Fore.LIGHTRED_EX+"                      ID "+del_id+" does not exist!!")
    else:
        print(os.path.getsize('temp.txt'))

    os.replace('temp.txt', 'profiles.txt')







def update_profile(update_id):
    if (view_Update_profile(update_id))!=1:
        print(Fore.LIGHTRED_EX + "\n\n                          There is no profile associated with ID " + update_id + "!!")
        up___id = input(Fore.LIGHTYELLOW_EX+'\n\nEnter student id again : \t')
        update_profile(up___id)

    k=int(input("\n\n\t\t\t\tUpdate  :\t"))
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
    delete_up_profile(update_id)

    ff=open("profiles.txt","a")
    ff.writelines(tttt)



def delete_profile(del_id):

    with open("profiles.txt", "r") as inputs:
        with open("temp.txt", "w") as output:
            for line in inputs:
                if not line.strip("\n").startswith(str(del_id)):
                    output.write(line)

    print(Fore.LIGHTRED_EX + '\n\n                                      Profile Deleted!')
    os.replace('temp.txt', 'profiles.txt')




def std_Panel():
    print("\n\n\n")
    print(
        Fore.LIGHTBLUE_EX + '       ┌──' + '=========================================================' + Fore.BLUE + '─┐')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '                                                            ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                       Student Report                       ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '                                                            ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  1 >  View Profile                         ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  2 >  View Assigned Courses                ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                  3 >  LogOut                               ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '────────────────────────────────────────────────────────────' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + Fore.LIGHTYELLOW_EX + '                >>Select option (1/2/3)                     ' + Fore.BLUE + '│')
    print(
        Fore.LIGHTBLUE_EX + '       │' + '                                                            ' + Fore.BLUE + '│')
    print(Fore.LIGHTBLUE_EX + '       │' + '============================================================' + '│')
    print(Fore.LIGHTBLUE_EX + '       └──' + '─────────────────────────────────────────────────────────' + '─┘')
    call_student()

def assigned_courses(level):
    print("\n\n---------------------Assigned Courses--------------------")
    if level==1:
        print("     1 .Discrete Mathematics")
        print("     2 .C programming")
        print("     3 .Physics")
        print("     4 .Chemistry")
    if level==2:
        print("     1 .Data Structure and Algorithm I")
        print("     2 .Object Oriented programming")
        print("     3 .Data Structure and Algorithm II")
        print("     4 .Digital Logic Design")
    if level==3:
        print("     1 .Compiler")
        print("     2 .Concrete Mathematics")
        print("     3 .Networking")
        print("     4 .Software Engineering")
    if level==4:
        print("     1 .Machine Learning")
        print("     2 .Integrated Design Project")
        print("     3 .AI")
        print("     4 .Engineering Economics")



def call_student():
    std_choice = int(input("\n\n\t\t\t\tEnter :\t"))
    if std_choice == 1:
        yy = input("Enter student ID :\t")

        f = open("profiles.txt", "r")
        lines = f.readlines()
        for line in lines:
            if line.find(yy) != -1:
                print(Fore.LIGHTWHITE_EX + '\n\nID--------Level-Term---Phone----Gender--Result---Name')
                print(Fore.LIGHTYELLOW_EX + line)
                quit(std_Panel())
        f.close()
        print(Fore.LIGHTRED_EX + "\n\n                          There is no profile associated with ID " + y + "!!")
        print(Fore.LIGHTBLUE_EX + '\n\n>>       Choose another option :  ')
        std_Panel()
    elif std_choice == 2:
        l = int(input("Enter level : "))
        assigned_courses(l)
        print(Fore.LIGHTBLUE_EX + '\n\n>>       Choose another option :  ')
        std_Panel()
    elif std_choice == 3:
        print(Fore.RED + 'Logged Out!')
        print(Fore.LIGHTBLUE_EX + '\n\n>>       Choose another option :  ')
        select()
    print("\n\n\n")





select()
