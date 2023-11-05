import turtle

# 터틀 그래픽 창을 엽니다
window = turtle.Screen()
window.title("간단한 선 그래프 예제")


# 터틀 객체를 생성합니다
pen1= turtle.Turtle()
pen2 = turtle.Turtle()
bpen = turtle.Turtle()
rpen = turtle.Turtle()
gpen = turtle.Turtle()

bpen.color("blue")
rpen.color("red")
gpen.color("green")

pen2.speed(0)  # 최대 속도로 설정
bpen.speed(0)
pen1.speed(0)
rpen.speed(0)
gpen.speed(0)

#그래프1
pen1.penup()
pen1.goto(0-20, 0)
pen1.pendown()
pen1.goto(-300-20, 0)
pen1.penup()
pen1.goto(-300-20, 0)
pen1.pendown()
pen1.goto(-300-20, 300)
pen1.penup()
pen1.goto(-300-20, 300)
pen1.write("기여도", align="center")
pen1.goto(0-20, 0)
pen1.write("직원번호", align="center")
rpen.penup()
rpen.goto(-320,300)
rpen.pendown()
rpen.goto(-20,300)
rpen.write("100%")

# 그래프 2
pen2.penup()
pen2.goto(0+20, 0)
pen2.pendown()
pen2.goto(300+20, 0)
pen2.penup()
pen2.goto(0+20, 0)
pen2.pendown()
pen2.goto(0+20, 300)
pen2.penup()
pen2.goto(300+20, 0)
pen2.write("부서번호", align="center")
pen2.goto(0+20, 300)
pen2.write("기여도", align="center")
rpen.penup()
rpen.goto(20,300)
rpen.pendown()
rpen.goto(320,300)
rpen.write("100%")


for i in range(0-320,0-20,int(300/k)):
    bpen.penup()
    bpen.goto(i, -20)
    bpen.pendown()
    bpen.write(str(int((i+320)/300*k)))

for j in range(0+20,320,int(300/13)):
    bpen.penup()
    bpen.goto(j, -20)
    bpen.pendown()
    bpen.write(str(int((j-20)/300*13)))

# 그래프를 그리기 위한 데이터를 정의합니다
data = [(0, 0), (50, 100), (100, 40), (150, 200), (200, 0)]
bpen.penup()
bpen.goto(data[0][0], data[0][1])
bpen.pendown()

for x, y in data:
    bpen.goto(x, y)
    bpen.dot(5)  # 데이터 포인트를 점으로 표시
    bpen.write(f'({x}, {y})', align='left')
# 그래프를 그립니다


# 데이터 포인트를 점으로 표시

# 그래프 그리기 완료


# 창을 닫습니다
turtle.exitonclick()
