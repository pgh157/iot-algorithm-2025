# 시에르핀스키 삼각형

from tkinter import*

## 클래스와 함수 선언 부분 ##
def drawTriangle(x,y,size):
    if size >=30: # 
        drawTriangle(x,y,size/2)  # 왼쪽 아래 작은 삼각형
        drawTriangle(x+size/2,y,size/2)  # 오른쪽 아래 작은 삼각형
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2) # 위쪽 작은 삼각형
        
    else:
        canvas.create_polygon(x,y,x+size,y , x+size/2, y-size*(3**0.5)/2, fill="green", outline="red")

## 전역변수
wSize = 1000
radius = 400

## 메인코드 
root = Tk()
root.title("시에르핀스키 삼각형")
canvas = Canvas(root, width=wSize, height=wSize,bg="white")

drawTriangle(wSize/5,wSize/5*4,wSize*2/3)

canvas.pack()
root.mainloop()