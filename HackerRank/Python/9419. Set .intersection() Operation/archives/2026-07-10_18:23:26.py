# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
a = set(map(int, input().split()))
input()
print(len(a & set(map(int, input().split()))))
