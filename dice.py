from tkinter import*
from PIL import ImageTk,Image
import random
root=Tk()
root.title("endless   dice")
root.geometry("600x400")
root.configure(background="#000000")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1=Label(root,text="player 1",bg="white",fg="black");
player1.place(relx=0.1,rely=0.3,anchor=CENTER)


player2=Label(root,text="player 2",bg="white",fg="black");
player2.place(relx=0.9,rely=0.3,anchor=CENTER)


player1score=Label(root,bg="white",fg="black");
player1score.place(relx=0.1,rely=0.4,anchor=CENTER)


player2score=Label(root,bg="white",fg="black");
player2score.place(relx=0.9,rely=0.4,anchor=CENTER)


playerscore=Label(root,bg="white",fg="red");
playerscore.place(relx=0.5,rely=0.4,anchor=CENTER)


player1_score=0
def player1():
    global player1_score
    randomnumber=random.randint(1,6)
    playerscore["text"]="player 1 dice number :  "+str(randomnumber)
    player1_score=player1_score+randomnumber
    player1score["text"]=str(player1_score)

player1btn=Button(root,image=img,command=player1)
player1btn.place(relx=0.1,rely=0.6,anchor=CENTER)

player2_score=0
def player2():
    global player2_score
    randomnumber=random.randint(1,6)
    playerscore["text"]="player 1 dice number :  "+str(randomnumber)
    player2_score=player2_score+randomnumber
    player2score["text"]=str(player2_score)

player2btn=Button(root,image=img,command=player2)
player2btn.place(relx=0.9,rely=0.6,anchor=CENTER)


root.mainloop()





















