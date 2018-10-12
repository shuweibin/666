from turtle import*
pensize(1)
pencolor("green")
i=1
while(i<=100):
    seth(90)
    fd(i)
    seth(180)
    fd(i+1)
    seth(-90)
    fd(i+2)
    seth(0)
    fd(i+3)
    i=i+4
    
