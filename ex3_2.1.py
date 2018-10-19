dayup,dayfactor=1,0.01
for i in range(365):
    if i in[50,100,150,200,250,300,350]:
        dayup=dayup
    else:
        dayup=dayup*(1+dayfactor)
print("努力的结果:{:.2f}".format(dayup))
