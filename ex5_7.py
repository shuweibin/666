def move(n,a,b,c):
    if n==1:
        print("移动{}:{}-->{}".format(n,a,c))
    else:
        move(n-1,a,c,b)
        print("移动{}:{}-->{}".format(n,b,c))
        move(n-1,b,a,c)
move(3,'a','b','c')
