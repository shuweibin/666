from turtle import*
setup(650,350,200,200)
penup()
pendown()
pensize(6)
pencolor("purple")
seth(-90)
fd(30)
penup()
fd(30)
seth(0)
for i in (0,90,180):
    seth(i)
    fd(30)
    pendown()
    fd(60)
    penup()
    fd(30)
seth(-90)
fd(30)
pendown()
fd(60)
