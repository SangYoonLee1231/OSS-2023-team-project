from tkinter.ttk import *
from tkinter import *
import tkinter.messagebox
import time
import random

class boardgame:
    def __init__(self):
        self.root = Tk()
        self.root.title("������� ����")
        self.root.geometry("400x400")
        self.choice = StringVar()
        self.choice.set("")
        label = Label(self.root, text="���ϴ� ������ �����ϼ���:")
        label.pack()
        button1 = Radiobutton(self.root, text="����ã��", variable=self.choice, value="����ã��")
        button1.pack()
        button2 = Radiobutton(self.root, text="ƽ����", variable=self.choice, value="ƽ����")
        button2.pack()
        button3 = Radiobutton(self.root, text="����", variable=self.choice, value="����")
        button3.pack()
        button4 = Button(self.root, text="���� Ȯ��", command=self.start)
        button4.pack()
        self.root.mainloop()
        

        
    def start(self):
        game = self.choice.get()
        self.root.destroy()  
        if game == "ƽ����":
            tic_tac_toe_game = TicTacToe()
            tic_tac_toe_game.game.mainloop()
        elif game == "����ã��":
            minegame = Mineset()
            minegame.game.mainloop()
        elif game == "����":
            fivestone = Fivestone()
            fivestone.game.mainloop()
        self.root.quit()
