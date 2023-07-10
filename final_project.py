from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox
import time
import random

class boardgame:
    def __init__(self):
        self.root = Tk()
        self.root.title("보드게임 선택")
        self.root.geometry("400x400")
        self.choice = StringVar()
        self.choice.set("")
        label = Label(self.root, text="원하는 게임을 선택하세요:")
        label.pack()
        button1 = Radiobutton(self.root, text="지뢰찾기", variable=self.choice, value="지뢰찾기")
        button1.pack()
        button2 = Radiobutton(self.root, text="틱택토", variable=self.choice, value="틱택토")
        button2.pack()
        button3 = Radiobutton(self.root, text="오목", variable=self.choice, value="오목")
        button3.pack()
        button4 = Button(self.root, text="선택 확정", command=self.start)
        button4.pack()
        self.root.mainloop()
        ##

        
    def start(self):
        game = self.choice.get()
        self.root.destroy()  
        if game == "틱택토":
            tic_tac_toe_game = TicTacToe()
            tic_tac_toe_game.game.mainloop()
        elif game == "지뢰찾기":
            minegame = Mineset()
            minegame.game.mainloop()
        elif game == "오목":
            fivestone = Fivestone()
            fivestone.game.mainloop()
        self.root.quit()

class Mineset:
    def __init__(self):
        self.game = Tk()
        self.game.title("지뢰찾기 설정")

        self.width = IntVar()
        self.bomb = IntVar()

        width = Label(self.game,text="지뢰밭의 가로 혹은 높이 크기")
        width.pack()
        width2 = Entry(self.game,textvariable=self.width)
        width2.pack()
        bomb = Label(self.game,text="지뢰의 개수:")
        bomb.pack()
        bomb2 = Entry(self.game,textvariable=self.bomb)
        bomb2.pack()

        start = Button(self.game,text="게임 시작",command=self.start,bg="yellow")
        start.pack()
    def start(self):#게임시간 추가
        width = self.width.get()
        bomb = self.bomb.get()

        

        minegame = Mine(width,bomb)
        minegame.start()

        
        
        self.game.destroy()
        minegame.destroy()
class Mine:
    def __init__(self,width,bomb):
        self.width = width
        self.bomb = bomb
        self.board = [[None for _ in range(width)] for _ in range(width)]
        self.dg = set()

        self.game =Tk()
        self.game.title("지뢰찾기")
        self.game.geometry("400x400")
        self.click = []
        #마우스 왼클릭,우클릭 설정
        self.create_random_bomb()
        self.calculate()
        
    

    def create_random_bomb(self):
        #랜덤위치에 원하는 갯수만큼 폭탄생성
        pass
    def calculate(self):
        #주변 지뢰 갯수 측정해 숫자 띄우기
        pass
    def Mine(self,x,y):
        #땅 파서 지뢰일시 lose()함수 실행 아닐시 승리 메세지 띄우기
        #숫자별 색깔 설정
        pass
    def sign(self,x,y):
        #마우스 우클릭 설정
        pass
    
    
    def lose(self):
        #패배 조건 생성
        pass

    
    def destroy(self):
        #게임 종료시 창 닫는 기능
        pass
    
    def start(self):
        self.game.mainloop()



class Fivestone:
    def __init__(self):
        self.game = Tk()
        self.game.title("10x10 오목")
        self.board = []
        self.player = 'O'
        self.create_board()
        self.game.mainloop()
        

    def create_board(self):
        #판만들기
        pass
    

    def is_draw(self):
        #비기는 조건 샹성
        pass

    def mark(self,x,y):
        #판에 O와 o를 표시 
        #O,o의 색깔 변경
        #O,o를 번갈아 하기
        #승리,비길시 메세지 띄우기
        pass

    def is_win(self,i,j):
        #승리조건 생성
        pass

    def switch(self):
        #'O'와 'o'를 번갈아 가면 실행
        pass
    def result(self,result):
        tkinter.messagebox.showinfo("결과",result)
        self.game.destroy()