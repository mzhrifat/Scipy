import csv

"""
data=[
    ["Name","Salary","Post","Department","Location"],
    ["a",7000,"Soft e","IT","New york"],
    ["b",9000,"en","it","Delli"]
]

with open('new.csv','w')as file:
    csv_file=csv.writer(file)
    csv_file.writerows(data)
    print("created successfully")

"""
with open('new.csv','r')as file:
     content=csv.reader(file)
     for row in content:
         print(row)