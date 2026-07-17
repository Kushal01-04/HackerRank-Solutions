# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()
for _ in range(int(input())):
    cmd = input().split()
    getattr(d, cmd[0])(*(map(int, cmd[1:])))
print(*d)
