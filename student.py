import json
import time

def student():
    while True:
        print("\n\n\t\t\t1.VIEW\t2.SEARCH\t3.EXIT")
        std_ch = int(input("Enter your choice"))
        if std_ch == 1:
            try:
                with open("student.json", "r")as file:
                    data = json.load(file)
                print("{:<8} {:<15} {:<10} {:<10} ".format("USN", "NAME", "BRANCH", "MARKS").center(120))
                print("_____________________________________________________".center(120))
                for key in data:
                    print("{:<8} {:<15} {:<10} {:<10}".format(key, data[key]["Name"], data[key]["Branch"],
                                                              data[key]["Marks"]).center(120))
                print("_____________________________________________________".center(120))

            except:
                print("File not found")

        if std_ch == 2:
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

        if std_ch == 3:
            print("Loging out...")
            time.sleep(5)
            print("Loged out successfully ")
            exit()
