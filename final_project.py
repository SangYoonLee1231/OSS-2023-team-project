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
    def start(self):
        width = self.width.get()
        bomb = self.bomb.get()

        start = time.time() #게임시간 코드(시작)

        minegame = Mine(width,bomb)
        minegame.start()

        end = time.time() #게임시간 코드(끝)
        times = "{:.1f}".format(end - start)
        tkinter.messagebox.showinfo("게임 작동 시간",f"지뢰찾기에 걸린 시간: {times}초 입니다.")
        
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
        
        for x in range(width): #마우스 왼클릭 우클릭 for문
            dig_click = []
            for y in range(width):
                click = Button(self.game, width=4, height=2)
                click.grid(row=x, column=y)
                click.bind('<Button-1>', lambda event, x=x, y=y: self.Mine(x, y))
                click.bind('<Button-3>', lambda event, x=x, y=y: self.sign(x, y))
                dig_click.append(click)
            self.click.append(dig_click) #마우스 왼클릭,우클릭 설정
        self.create_random_bomb()
        self.calculate()
        
    

    def create_random_bomb(self): #랜덤위치에 원하는 갯수만큼 폭탄생성
        bomb = 0
        while bomb < self.bomb:
            x = random.randint(0,self.width -1)
            y = random.randint(0,self.width -1)
            if self.board[x][y] == "B":
                continue
            self.board[x][y] = "B"
            bomb += 1           

    def calculate(self): #주변 지뢰 갯수 측정해 숫자 띄우기
        for x in range(self.width):
            for y in range(self.width):
                if self.board[x][y] != "B":        
                    count = 0
                    for x1 in range(max(0, x - 1), min(self.width, x+ 2)):
                        for y1 in range(max(0, y - 1), min(self.width, y + 2)):
                            if self.board[x1][y1] == "B":
                                count += 1
                    self.board[x][y] = count     
                       
    def Mine(self,x,y):
        if (x,y) not in self.dg and self.click[x][y] != "?":
            self.dg.add((x,y))
            if self.board[x][y] == "B":
                self.lose()
            else:
                self.click[x][y]["text"] = str(self.board[x][y])
                if self.board[x][y] == 0:
                    self.click[x][y].config(bg = "yellow")
                elif self.board[x][y] == 1:
                    self.click[x][y].config(bg = "blue")
                elif self.board[x][y] == 2:
                    self.click[x][y].config(bg = "green")
                else:
                    self.click[x][y].config(bg = "red")
                if len(self.dg) == self.width ** 2 - self.bomb:
                    tkinter.messagebox.showinfo("게임 종료", "지뢰찾기에서 승리하였습니다.")
                    self.game.quit()
        #땅 파서 지뢰일시 lose()함수 실행 아닐시 승리 메세지 띄우기
        #숫자별 색깔 설정

    def sign(self,x,y):
        #마우스 우클릭 설정
        pass
    
    
    def lose(self):
         for x in range(self.width):
            for y in range(self.width):
                if self.board[x][y] == 'B':
                    self.click[x][y].config(text="B",state = "disabled")
                    
                else:
                    self.click[x][y].config(text=str(self.board[x][y]),state = "disabled")
                    
         tkinter.messagebox.showinfo("게임 종료", "지뢰찾기에서 패배하였습니다.")
         self.game.quit()

    
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
        for x in range(10):
            width = []
            for y in range(10):
                board_button = Button(self.game,width=5,height=2,command=lambda x=x,y=y:self.mark(x,y))
                board_button.grid(row=x,column=y)
                width.append(board_button)
            self.board.append(width)
    

    def is_draw(self):
        is_draw = True
        for row in self.board:
            for button in row:
                if button["text"] == "":
                    is_draw =  False
        return is_draw

    def mark(self,x,y):
        button = self.board[x][y]
        if button["text"] == "":
            
            if self.player == 'O':
                button["text"] = self.player
                button.config(fg="black")
            else:
                button["text"] = self.player
                button.config(fg="red")
            
            if self.is_win(x,y) == True:
                self.result("{} won!".format(self.player))
            elif self.is_draw() == True:
                self.result("Draw!")
            else:
                self.switch()

    def is_win(self,i,j):
        is_win = False
        player = self.player
        direction = [(1,0),(0,1),(1,1),(1,-1)]
        for direct in direction:
            count = 1
            x,y = direct 
            width,height = x + i,y+j
            while 0 <= width < 10 and 0 <= height < 10 and self.board[width][height]["text"] == player:
                count += 1
                width += x
                height += y
            x, y = -x, -y
            width,height = x + i,y+j
            while 0 <= width < 10 and 0 <= height < 10 and self.board[width][height]["text"] == player:
                count += 1
                width += x
                height += y
            if count == 5:
                is_win = True
        return is_win

    def switch(self):
        if self.player == 'O':
            self.player = 'o'
        else:
            self.player = 'O'
        pass
    def result(self,result):
        tkinter.messagebox.showinfo("결과",result)


class TicTacToe:
    def __init__(self):
        self.game = Tk()
        self.game.title("5X5 틱백토 game")
        self.player = 'O'
        self.board = []
        self.create_board()
        self.game.mainloop()

    def create_board(self):
        #노란색의 5*5틱택토 판 만들기
        for i in range(5):
            width = []
            for j in range(5):
                board_button = Button(self.game, width=5, height=2, command=lambda i=i, j=j: self.mark(i, j),bg="yellow")
                board_button.grid(row=i, column=j)
                width.append(board_button)
            self.board.append(width)

    def is_win(self):
        #5*5틱택토의 승리조건
        is_win = False
        for x in range(5):
            if self.board[x][0]["text"] == self.board[x][1]["text"] == self.board[x][2]["text"] == self.board[x][3]["text"] != "" or self.board[x][1]["text"] == self.board[x][2]["text"]  == self.board[x][3]["text"] == self.board[x][4]["text"] != "":
                is_win = True
            if self.board[0][x]["text"] == self.board[1][x]["text"] == self.board[2][x]["text"] == self.board[3][x]["text"] != "" or self.board[1][x]["text"] ==  self.board[2][x]["text"] == self.board[3][x]["text"] == self.board[4][x]["text"] != "":
                is_win = True
        if self.board[0][0]["text"] == self.board[1][1]["text"] == self.board[2][2]["text"] == self.board[3][3]["text"] != "" or self.board[1][1]["text"] == self.board[2][2]["text"] == self.board[3][3]["text"] == self.board[4][4]["text"] != "":
            is_win = True
        if self.board[0][4]["text"] == self.board[1][3]["text"] == self.board[2][2]["text"] == self.board[3][1]["text"] != "" or self.board[1][3]["text"] == self.board[2][2]["text"] == self.board[3][1]["text"] == self.board[4][0]["text"] != "":
            is_win = True
        if self.board[1][4]["text"] == self.board[2][3]["text"] == self.board[3][2]["text"] == self.board[4][1]["text"] != "" or self.board[3][0]["text"] == self.board[2][1]["text" ] == self.board[1][2]["text"] == self.board[0][3]["text"] != "":
            is_win = True
        if self.board[3][4]["text"] == self.board[2][3]["text"] == self.board[1][2]["text"] == self.board[0][1]["text"] != "" or self.board[1][0]["text"] == self.board[2][1]["text" ] == self.board[3][2]["text"] == self.board[4][3]["text"] != "":
            return True
        return is_win

    def is_draw(self):
        is_draw = True
        for row in self.board:
            for button in row:
                if button["text"] == "":
                    is_draw =  False
        return is_draw
    
    def mark(self,x,y):
        button = self.board[x][y]
        if button["text"] == "":
            #O,X의 색깔 변경
            #gui로 승리,비김 메세지 띄우기
            if self.player == 'O':
                button["text"] = self.player
                button.config(fg="blue")
            else:
                button["text"] = self.player
                button.config(fg="red")
            
            if self.is_win() == True:
                self.resultmessage("{} won!".format(self.player))
            elif self.is_draw() == True:
                self.resultmessage("Draw!")
            else:
                self.switch()   

    def switch(self):
        if self.player == 'O':
            self.player = 'x'
        else:
            self.player = 'O'
    
    def resultmessage(self,result):
        tkinter.messagebox.showinfo("결과",result)
        self.game.destroy()

game = boardgame() 
