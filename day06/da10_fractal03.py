# 전체 프랙탈 원 그리기
from tkinter import*
import random

# 클래스와 함수 선언 부분 ##
def drawCircle(x,y,r):
    canvas.create_oval(x-r, y-r,x+r,y+r, width = 2, outline =random.choice(colors))
    if r>=5:
        drawCircle(x+r//2, y , r//2)
        drawCircle(x-r//2, y , r//2)

# 전역 변수
colors = ["red", "green", "blue", "black", "orange","indigo", "violet", "pink"]
wSize = 1000
radius = 400

# 메인 코드
root = Tk()
root.title("원 모양의 프랙탈")
canvas = Canvas(root, heigh = wSize, width=wSize, bg = "white")
drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
root.mainloop()