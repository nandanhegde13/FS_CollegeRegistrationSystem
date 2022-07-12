import json
import time



def menu():
    print(
        "\n\n\t\t\t1.ADD EMPLOYEES\t\t2.SEARCH EMPLOYEE\t\t3.UPDATE EMPLOYEES\t\t4.DISPLAY EMPLOYEE DETAILS\t\t5.DELETE EMPLOYEE\t\t\n\t\t\t6.ADD STUDENT\t\t7.SEARCH STUDENT\t\t8.UPDATE STUDENT\t\t9.DISPLAY STUDENT DETAILS\t\t10.DELETE STUDENT\t\t11/.EXIT")


def admin():
    while True:
        menu()
        admin_ch = int(input("Enter your choice"))

        if admin_ch == 1:

            print("Enter employee details")

            ssn = input("enter employee ssn")

            name = input("enter employee name")
            salary = int(input("enter employee salary"))

            new_data = {
                ssn: {
                    "Name": name,
                    "Salary": salary,
                }
            }

            try:
                with open("employee.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("employee.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("employee.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

        if admin_ch == 2:
            ch = input("Search employee by SSN")
            try:
                with open("employee.json", "r") as data_file:
                    data = json.load(data_file)
                    if ch in data:
                        print(f"Name: {data[ch]['Name']}\nSalary: {data[ch]['Salary']}")
                    else:
                        print("data not found")

            except FileNotFoundError:
                print("file not found")

        if admin_ch == 3:
            ch = input("Enter employee SSN to be updated")
            print()
            field_ch = input("enter field to be updated")
            field_ch = field_ch.lower()
            if field_ch == "name":
                name = input("Enter new name")
            elif field_ch == "salary":
                salary = input("Enter new salary")
            try:
                with open('employee.json', "r")as data_file:
                    data = json.load(data_file)
                    if field_ch == "name":
                        data[ch]['Name'] = name
                    elif field_ch == "salary":
                        data[ch]['Salary'] = salary
                with open('employee.json', "w")as data_file:
                    json.dump(data, data_file)

            except FileNotFoundError:
                print("File not found")

        if admin_ch == 4:
            try:
                with open("employee.json", "r") as file:
                    data = json.load(file)
                print("{:<8} {:<15} {:<10} ".format("SSN", "NAME", "SALARY").center(120))
                print("___________________________________".center(120))
                for key in data:
                    print("{:<8} {:<15} {:<10} ".format(key, data[key]["Name"], data[key]["Salary"]).center(120))
                print("___________________________________".center(120))
            except FileNotFoundError:
                print("file not found")

        if admin_ch == 5:
            choice = input("enter ssn to be deleted")
            try:
                with open("employee.json", "r") as data_file:
                    data = json.load(data_file)

                    if choice in data:
                        del data[choice]
                with open("employee.json", "w")as file:
                    json.dump(data, file)
                    print("deleted successfully")

            except FileNotFoundError:
                print("file not found")

        if admin_ch == 6:

            print("Enter student details type menu to go back")

            usn = input("enter student usn")

            name = input("enter student name")
            branch = input("enter student branch")
            marks = int(input("enter student marks"))
            new_data = {
                usn: {
                    "Name": name,
                    "Branch": branch,
                    "Marks": marks
                }
            }

            try:
                with open("student.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("student.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("student.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

        if admin_ch == 7:
            ch = input("Search student by USN")
            try:
                with open("student.json", "r") as data_file:
                    data = json.load(data_file)
                    if ch in data:
                        print(f"Name: {data[ch]['Name']}\nBranch: {data[ch]['Branch']}\nMarks: {data[ch]['Marks']}")
                    else:
                        print("data not found")

            except FileNotFoundError:
                print("file not found")

        if admin_ch == 8:
            ch = input("Enter student USN to be updated")
            print()
            field_ch = input("enter field to be updated")
            field_ch = field_ch.lower()
            if field_ch == "name":
                name = input("Enter new name")
            elif field_ch == "branch":
                branch = input("Enter new branch")
            elif field_ch == "marks":
                marks = input("Enter new marks")
            try:
                with open('student.json', "r")as data_file:
                    data = json.load(data_file)
                    if field_ch == "name":
                        data[ch]['Name'] = name
                    elif field_ch == "branch":
                        data[ch]['Branch'] = branch
                    elif field_ch == "marks":
                        data[ch]['Marks'] = marks
                with open('student.json', "w")as data_file:
                    json.dump(data, data_file)

            except FileNotFoundError:
                print("File not found")

        if admin_ch == 9:
            try:
                with open("student.json", "r") as file:
                    data = json.load(file)
                print("{:<8} {:<15} {:<10} {:<10} ".format("USN", "NAME", "BRANCH","MARKS").center(120))
                print("_____________________________________________________".center(120))
                for key in data:
                    print("{:<8} {:<15} {:<10} {:<10}".format(key, data[key]["Name"], data[key]["Branch"], data[key]["Marks"]).center(120))
                print("_____________________________________________________".center(120))
            except FileNotFoundError:
                print("file not found")

        if admin_ch == 10:
            choice = input("enter usn to be deleted")
            try:
                with open("student.json", "r") as data_file:
                    data = json.load(data_file)

                    if choice in data:
                        del data[choice]
                with open("student.json", "w")as file:
                    json.dump(data, file)

            except FileNotFoundError:
                print("file not found")

        if admin_ch == 11:
            print("Loging out...")
            time.sleep(5)
            print("Loged out successfully ")
            exit()
