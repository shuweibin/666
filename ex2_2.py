Money=input("请输入带符号的金钱数目:")
if Money[-1] in ['Y','y']:
    M=eval(Money[:-1]/6)
    print("兑换后的金钱是{:.2f}D".format(M))
elif Money[-1] in ['D','d']:
    M=6*eval(Money[:-1])
    print("兑换后的金钱是{:.2f}Y".format(M))
else:
    print("输入格式错误")
           
