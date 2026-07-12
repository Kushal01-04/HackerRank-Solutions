# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
print(*(list(product(*[list(map(int,input().split())),list(map(int,input().split()))]))))


