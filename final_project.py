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
        #최종결과 메세지 띄우기
        tkinter.messagebox.showinfo("결과",result)
        self.game.destroy()