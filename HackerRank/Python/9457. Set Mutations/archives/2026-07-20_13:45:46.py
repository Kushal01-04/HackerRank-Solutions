# Enter your code here. Read input from STDIN. Print output to STDOUT
num1 = int(input())
set1 = set(map(int,input().split()))
num2 = int(input())
for _ in range(num2):
    cmd = input().split()
    set2 = set(map(int,input().split()))
    if cmd[0] == "intersection_update":
        set1.intersection_update(set2)
    elif cmd[0] == "update":
        set1.update(set2)
    elif cmd[0] == "difference_update":
        set1.difference_update(set2)
    else:
        set1.symmetric_difference_update(set2)
print(sum(set1))
