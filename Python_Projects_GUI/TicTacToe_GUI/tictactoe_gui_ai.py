from tkinter import *
import random

# Defining root window
root = Tk()
root.title("TicTacToe Game")
turn = 'X'
count = 0
game_running = True
c0, c1, c2, r3, r1, r2 = 0, 1, 2, 3, 1, 2

checkerboard = [" " for i in range(10)]
def win(bo,turn):
    return (bo[1] == bo[2] and bo[2] == bo[3] and bo[3] == turn) or \
            (bo[4] == bo[5] and bo[5] == bo[6] and bo[6] == turn) or \
            (bo[7] == bo[8] and bo[8] == bo[9] and bo[9] == turn) or \
            (bo[1] == bo[4] and bo[4] == bo[7] and bo[7] == turn) or \
            (bo[2] == bo[5] and bo[5] == bo[8] and bo[8] == turn) or \
            (bo[3] == bo[6] and bo[6] == bo[9] and bo[9] == turn) or \
            (bo[1] == bo[5] and bo[5] == bo[9] and bo[9] == turn) or \
            (bo[3] == bo[5] and bo[5] == bo[7] and bo[7] == turn)

def compmove():
    place = {1:button_1,2:button_2,3:button_3,4:button_4,5:button_5,6:button_6,7:button_7,8:button_8,9:button_9}
    mov = 0
    possibilities = [x for x,y in enumerate(checkerboard) if y == " " and x != 0]
    copyboard = checkerboard[:]
    for i in ["O","X"]:
        for j in possibilities:
            copyboard[j] = i
            if win(copyboard,i):
                mov = j
                return place[mov],mov
            else:
                copyboard[j] = " "
    if 5 in possibilities:
        mov = 5
        return place[mov],mov
    for i in [1,3,7,9]:
        if i in possibilities:
            mov  = i
            return place[mov],mov
    if not win(copyboard,i):
        move = possibilities[random.randrange(0,len(possibilities))]
        return place[mov],mov
    return place[mov],mov
def logic(place,no,turn):
    global c0, c1, c2, r3, r1, r2, checkerboard, game_running, count
    if place['text'] == ' ':
        count += 1
        if place == button_1:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 1))
            place.grid(column=c0, row=r1)
            checkerboard[no] = turn
        elif place == button_2:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 2))
            place.grid(column=c1, row=r1)
            checkerboard[no] = turn
        elif place == button_3:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 3))
            place.grid(column=c2, row=r1)
            checkerboard[no] = turn

        elif place == button_4:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 4))
            place.grid(column=c0, row=r2)
            checkerboard[no] = turn
        elif place == button_5:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 5))
            place.grid(column=c1, row=r2)
            checkerboard[no] = turn
        elif place == button_6:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 6))
            place.grid(column=c2, row=r2)
            checkerboard[no] = turn

        elif place == button_7:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 7))
            place.grid(column=c0, row=r3)
            checkerboard[no] = turn
        elif place == button_8:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 8))
            place.grid(column=c1, row=r3)
            checkerboard[no] = turn
        elif place == button_9:
            place = Button(height=5, width=11, text=turn, command=lambda: button_click(place, 9))
            place.grid(column=c2, row=r3)
            checkerboard[no] = turn
    else:
        warn_label = Label(text="The Place is already Filled!")
        warn_label.grid(columnspan=3, row=0)
def wincheck(turn):
    global game_running
    if win(checkerboard,turn):
            warn_label = Label(text="********** " + turn + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + turn + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
    if count >= 9:
            warn_label = Label(text="********** " + "It's a Tie" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + "It's a Tie" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
def button_click(place,no):
    global turn, c0, c1, c2, r3, r1, r2, checkerboard, game_running, count
    if game_running:
        turn = "X"
        logic(place,no,"X")
        wincheck(turn)
        turn = "O"
        place,no = compmove()[0],compmove()[1]
        if no > 0:
            logic(place,no,"O")
        wincheck(turn)
        
    else:
        warn_label = Label(text="The Game is over!")
        warn_label.grid(columnspan=3, row=0)
        head1_label = Label(text="The Game is over!")
        head1_label.grid(columnspan=3, row=4)
        b1 = Button(height=5, width=11, text=checkerboard[1], state='disabled').grid(column=0, row=1)
        b2 = Button(height=5, width=11, text=checkerboard[2], state='disabled').grid(column=1, row=1)
        b3 = Button(height=5, width=11, text=checkerboard[3], state='disabled').grid(column=2, row=1)

        b4 = Button(height=5, width=11, text=checkerboard[4], state='disabled').grid(column=0, row=2)
        b5 = Button(height=5, width=11, text=checkerboard[5], state='disabled').grid(column=1, row=2)
        b6 = Button(height=5, width=11, text=checkerboard[6], state='disabled').grid(column=2, row=2)

        b7 = Button(height=5, width=11, text=checkerboard[7], state='disabled').grid(column=0, row=3)
        b8 = Button(height=5, width=11, text=checkerboard[8], state='disabled').grid(column=1, row=3)
        b9 = Button(height=5, width=11, text=checkerboard[9], state='disabled').grid(column=2, row=3)

# defining ui design
head_label = Label(text="")

head_label.grid(columnspan=3, row=4)

button_1 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_1, 1))
button_2 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_2, 2))
button_3 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_3, 3))

button_4 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_4, 4))
button_5 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_5, 5))
button_6 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_6, 6))

button_7 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_7, 7))
button_8 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_8, 8))
button_9 = Button(height=5, width=11, text=' ', command=lambda: button_click(button_9, 9))
button_exit = Button(width=11, text='Exit the Game', command=root.quit)

button_1.grid(column=0, row=1)
button_2.grid(column=1, row=1)
button_3.grid(column=2, row=1)

button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)

button_7.grid(column=0, row=3)
button_8.grid(column=1, row=3)
button_9.grid(column=2, row=3)
button_exit.grid(columnspan=3, row=6, pady=5)

root.mainloop()