def Student(Math,Python,OS):
    total = (Math+Python+OS)
    return (total/300)*100

m = int(input("Enter Maths Marks: "))
p = int(input("Enter Python Marks: "))
o = int(input("Enter OS Marks: "))

print("Student Score: ",Student(m,p,o))
