def fact(n):
    if n ==1:
        return 1
    elif n==2:
        return 1
    else:
        return fact(n-1)+fact(n-2)
num=eval(input("请输入一个整数:"))
print(fact(num))
