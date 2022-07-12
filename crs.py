import admin
import student

print("\n**********************************************************COLLEGE REGISTRATION SYSTEM*****************************************************************".center(100))


str = "LOGIN"

print(str.center(145))
print("1.ADMIN LOGIN\n2.STUDENT LOGIN\n3.EXIT\n\n")

pswd = "ADMIN"
std_pswd = "STUDENT"
ch = int(input("Enter your choice"))

if ch == 1:
    while True:
        password = input("Enter password")
        if password == pswd:
            print("Login successful ")
            break
        else:
            print("Incorrect password..Try again")

    admin.admin()
if ch == 2:
    while True:
        password = input("Enter password")
        if password == std_pswd:
            print("Login successful ")
            break
        else:
            print("Incorrect password..Try again")
    student.student()
if ch == 3:
    exit()