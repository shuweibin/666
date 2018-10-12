from turtle import*
setup(650,350,200,200)
pensize(6)
pencolor("green")
for i in (270,210,150,90,30,-30):
    seth(i)
    fd(60)
    seth(i-120)
    fd(60)
    seth(i-240)
    fd(120)
