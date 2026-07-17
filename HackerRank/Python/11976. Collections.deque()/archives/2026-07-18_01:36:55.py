# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N = int(input(""))
d=deque()
for _ in range(N):
    method = input().split()
    if method[0]=="append":
        d.append(int(method[1]))
    elif method[0]=="pop":
        d.pop()
    elif method[0]=="popleft":
        d.popleft()
    elif method[0]=="appendleft":
        d.appendleft(int(method[1]))
print(*d)     
