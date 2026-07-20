# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int,input().split()))
for _ in range(int(input())):
    getattr(s,input().split()[0])(set(map(int,input().split())))
print(sum(s))
