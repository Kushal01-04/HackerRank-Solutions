# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

num = int(input(""))
student = namedtuple("student",input().split())
students = [student(*input().split()) for _ in range(num)]
sum = 0
for  s in students:
    sum = sum + int(s.MARKS)
print(sum/len(students))   
