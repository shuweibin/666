from turtle import*
setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("pink")
seth(-40)
for i in range(5):
    circle(40,80)
    pencolor("yellow")
    circle(-40,80)
pencolor("green")
circle(40,40)
fd(40)
circle(16,120)
fd(30)