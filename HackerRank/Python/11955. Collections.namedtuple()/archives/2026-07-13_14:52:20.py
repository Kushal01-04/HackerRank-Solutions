# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input(""))
student = namedtuple("student",input().split())
print(sum(int(student(*input().split()).MARKS) for _ in range(n))/n)  
