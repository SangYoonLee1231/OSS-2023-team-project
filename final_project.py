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
