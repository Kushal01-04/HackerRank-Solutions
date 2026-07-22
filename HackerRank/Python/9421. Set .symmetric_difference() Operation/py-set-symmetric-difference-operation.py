# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
set1 = set(map(int,input().split()))
n = int(input())
print(len(set1.symmetric_difference(set(map(int,input().split())))))
