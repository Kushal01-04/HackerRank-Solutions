# Enter your code here. Read input from STDIN. Print output to STDOUT

T  = int(input())
for _ in range(T):
    num = input("")
    num1 = num.split()
    
    
    try:
        div = int(num1[0])//int(num1[1])
        print(div)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print(f'Error Code: {e}')
