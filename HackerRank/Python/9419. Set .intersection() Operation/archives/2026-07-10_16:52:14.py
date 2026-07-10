# Enter your code here. Read input from STDIN. Print output to STDOUT

n_num = int(input())
n=set(map(int,input().split()))
b_num = int(input())
b=set(map(int,input().split()))
print(len(n.intersection(b)))
