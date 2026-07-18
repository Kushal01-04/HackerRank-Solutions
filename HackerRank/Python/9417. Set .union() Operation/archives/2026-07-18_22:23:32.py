# Enter your code here. Read input from STDIN. Print output to STDOUT
n  = int(input(""))
set1 = set(map(int,input().split()))
n1  = int(input(""))
print(len(set1.union( set(map(int,input().split())))))
