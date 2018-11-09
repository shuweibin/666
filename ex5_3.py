def isNum(s):
    try:
        n=eval(s)
    except:
        return False
    return True
s=input("请输入一个字符串:")
if isNum(s):
    print("{}是一个数".format(n))
else:
    print("{}不是一个数".format(n))
