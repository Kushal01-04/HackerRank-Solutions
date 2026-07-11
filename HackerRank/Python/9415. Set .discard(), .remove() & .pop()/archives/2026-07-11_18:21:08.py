n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, *arg = input().split()
    if cmd == "pop":
        s.pop()
    elif cmd == "remove":
        s.remove(int(arg[0]))
    else:
        s.discard(int(arg[0]))

print(sum(s))
        
