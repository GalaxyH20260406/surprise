n=input("暗号：\n归去来兮，请息交以绝游\n如果正确，请输入“yes”，输入后请按回车键")
if n != "yes":
    print("请重新输入")

import turtle
def draw_heart(size):
    turtle.color('red','pink')
    turtle.pensize(2)
    turtle.pendown()
    turtle.seth(150)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.circle(size*-3.745,45)
    turtle.circle(size*-1.431,165)
    turtle.left(120)
    turtle.circle(size*-1.431,165)
    turtle.circle(size*-3.745,45)
    turtle.fd(size)
    turtle.end_fill()
draw_heart(30)

# 设置画布和画笔
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("skyblue")  # 背景色，可根据喜好调整
screen.title("生日快乐")

pen = turtle.Turtle()
pen.speed(5)
pen.pensize(2)
pen.color("red")
pen.penup()

# 起始位置
start_x = -170
start_y = -100

# 要写的文字（包括感叹号）
texts = ["生", "日", "快", "乐", "!"]

# 每个字的偏移量（横向间距，可调）
offsets = [0, 80, 160, 240, 320]  # 相对于起始点的 x 偏移

# 写字
for i, word in enumerate(texts):
    x = start_x + offsets[i]
    y = start_y
    pen.goto(x, y)
    pen.pendown()   # 落笔，移动时会留下痕迹（移动至文字位置）
    pen.write(word, font=("楷体", 48, "bold"))
    pen.penup()     # 写完抬起，避免连接下一个字

# 装饰：画星星（画笔移动轨迹）
pen.color("gold")
pen.speed(6)
star_positions = [(-250, 150), (-100, 180), (50, 170), (200, 160), (300, 140)]

def draw_star(x, y, size):
    """在指定位置画一个五角星"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    angle = 144
    for _ in range(5):
        pen.forward(size)
        pen.right(angle)
        pen.forward(size)
        pen.right(72 - angle)  # 调整角度形成五角星
    pen.penup()

for pos in star_positions:
    draw_star(pos[0], pos[1], 20)

# 装饰：画烟花效果（小圆点组成的轨迹）
pen.color("orange", "yellow")
pen.speed(8)
firework_positions = [(-280, -50), (-50, -20), (180, -40), (320, -80)]

def draw_firework(x, y):
    """在指定位置画一个小烟花（多个小点）"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for _ in range(12):
        pen.dot(8)
        pen.forward(25)
        pen.backward(25)
        pen.right(30)
    pen.penup()

for pos in firework_positions:
    draw_firework(pos[0], pos[1])

pen.color("black")               # 设置颜色为黑色
pen.penup()                      # 移动时不留痕迹
pen.goto(-100, -200)             # 移动到指定位置
pen.pendown()                    # 可选，表示落笔（write 不需要，但为了逻辑完整）
pen.write("致你的19岁青春年华", font=("楷体", 24, "normal"))
pen.penup()

# 隐藏画笔，显示最终效果
pen.hideturtle()
turtle.done()
