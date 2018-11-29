def isPrime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
while True:
    try:
        n=eval(input("请输入整数:"))
    except:
        print("输入错误！请再次输入:")
        continue
    if n==-1:
        break
    if isPrime(n):
        print("{}是质数".format(n))
    else:
        print("{}不是质数".format(n))
