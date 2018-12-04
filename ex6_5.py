from datetime import datetime
from random import*
def generateSamples1(n:int):
    birthdays=[]
    days=[30,28,31,30,31,30,31,31,30,31,30,31]
    year=randint(1950,2000)
    for i in range(n):
        month=randint(1,12)
        if (year%400==0)and(year%4==0)and(year%100!=0):
            days[1]=29
        else:
            days[1]=28
            day=randint(1,days[month-1])
            someday=(month,day)
            birthday.append(someday)
    return birthdays
def calSamBirthdayProb(n:int):
    num=0
    for i in range(n):
        people=generateSamples1(23)
        pset=set(people)
        if len(pset)!=len(people):
            num+=1
    return num/n
def main():
    while True:
        n=int(input("请输入一个重复的次数:"))
        if n<0:
            break
        print("重复{}次，23个人中至少有两个人生日相同".format(n,calSamBirthdayProb(n)))
main()


        
    
        
