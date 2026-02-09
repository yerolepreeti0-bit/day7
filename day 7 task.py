# Personal Logger using append mode

name = input("Enter your name: ")
goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily Goal: {goal}\n")

print("Your goal has been saved!")


import csv

with open("data_source.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])


filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Oops! That file doesn’t exist yet.")
