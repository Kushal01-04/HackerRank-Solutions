# Enter your code here. Read input from STDIN. Print output to STDOUT
number = int(input(""))
lis = []
for _ in range(number):
    distint = input("")
    lis.append(distint)
convert = set(lis)

print(len(convert))
