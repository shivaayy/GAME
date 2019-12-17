from tkinter import *
import sys

w=Tk()
w.title("Tic Tac Toe GAME")
w.configure(bg="black")

# w.wm_iconbitmap(r'tic_tac.ico')

def callback(r,c):
    global player,a,stop_game,status,winner
    if player=='X' and stop_game==False and status[r][c]==0:
        a[r][c].configure(text='X',fg="black",bg="white")
        player='O'
        status[r][c]='X'
        win_check()
        if stop_game==True:
            winner.insert(END,"*********************  HURRAY !     X  won")
            
    elif player=='O' and stop_game==False and status[r][c]==0:
        a[r][c].configure(text='O',fg="black",bg="gray")
        player='X'
        status[r][c]='O'
        win_check()
        if stop_game==True:
            winner.insert(END,"*********************  HURRAY !     O  won")
    


def win_check():
    global stop_game,a,status,win
    for i in range(3):
        if status[i][0]==status[i][1]==status[i][2]!=0 and stop_game==False:
            stop_game=True
            win=status[i][0]
            a[i][0].configure(bg="green")
            a[i][1].configure(bg="green")
            a[i][2].configure(bg="green")
    for i in range(3):
        if status[0][i]==status[1][i]==status[2][i]!=0 and stop_game==False:
            stop_game=True
            win=status[0][i]
            a[0][i].configure(bg="green")
            a[1][i].configure(bg="green")
            a[2][i].configure(bg="green")

    if status[0][0]==status[1][1]==status[2][2]!=0 and stop_game==False:
        stop_game=True
        win=status[1][1]
        a[0][0].configure(bg="green")
        a[1][1].configure(bg="green")
        a[2][2].configure(bg="green")
    elif status[2][0]==status[1][1]==status[0][2]!=0 and stop_game==False:
        stop_game=True
        win=status[1][1]
        a[2][0].configure(bg="green")
        a[1][1].configure(bg="green")
        a[0][2].configure(bg="green")
    


a=[[0,0,0],
    [0,0,0],
    [0,0,0]]

status=[[0,0,0],
        [0,0,0],
        [0,0,0]]
player="X"
stop_game=False
winner=''


def stop():
    w.destroy()
    sys.exit()

    

def main():
    global a,status,player,stop_game,w,winner
    a=[[0,0,0],
    [0,0,0],
    [0,0,0]]

    status=[[0,0,0],
            [0,0,0],
            [0,0,0]]
    player="X"
    stop_game=False
    win=''
    for i in range(3):
        for j in range(3):
            a[i][j]=Button(w,font=('Arial',60),width=5,bg="powder blue", command=lambda r=i,c=j:callback(r,c))
            a[i][j].grid(row=i,column=j)
    Button(w,font=('Times New Roman',15),text="QUIT",width=8,command=stop).grid(row=3,column=0)
    Button(w,font=('Times New Roman',15),text="REPLAY",width=12,command=main).grid(row=3,column=1)
    output=Text(w,font=('Times New Roman',15),fg="green",height=2,width=65,bg="black")
    output.grid(row=4,column=0,columnspan=3,sticky='w')
    winner=output

if __name__ == "__main__":
    main()

w.mainloop()
