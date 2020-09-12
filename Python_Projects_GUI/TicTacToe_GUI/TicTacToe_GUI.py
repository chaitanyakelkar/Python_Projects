from tkinter import *

# Defining root window
root = Tk()
root.title("TicTacToe Game")

turn = 'X'
count = 0
game_running = True
c0, c1, c2, r3, r1, r2 = 0, 1, 2, 3, 1, 2

checkerboard = [" " for i in range(10)]

def button_click(place, no):
    global turn, c0, c1, c2, r3, r1, r2, checkerboard, game_running, count
    if game_running:
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
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            warn_label = Label(text="The Place is already Filled!")
            warn_label.grid(columnspan=3, row=0)
        head1_label = Label(text="It is " + turn + "'s Turn")
        head1_label.grid(columnspan=3, row=4)
        if checkerboard[1] == checkerboard[2] == checkerboard[3] != ' ':
            warn_label = Label(text="********** " + checkerboard[1] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[1] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
        if checkerboard[4] == checkerboard[5] == checkerboard[6] != ' ':
            warn_label = Label(text="********** " + checkerboard[4] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[4] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
        if checkerboard[7] == checkerboard[8] == checkerboard[9] != ' ':
            warn_label = Label(text="********** " + checkerboard[7] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[7] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False

        if checkerboard[1] == checkerboard[4] == checkerboard[7] != ' ':
            warn_label = Label(text="********** " + checkerboard[1] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[1] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
        if checkerboard[2] == checkerboard[5] == checkerboard[8] != ' ':
            warn_label = Label(text="********** " + checkerboard[2] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[2] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
        if checkerboard[3] == checkerboard[6] == checkerboard[9] != ' ':
            warn_label = Label(text="********** " + checkerboard[3] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[3] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False

        if checkerboard[1] == checkerboard[5] == checkerboard[9] != ' ':
            warn_label = Label(text="********** " + checkerboard[1] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[1] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
        if checkerboard[3] == checkerboard[5] == checkerboard[7] != ' ':
            warn_label = Label(text="********** " + checkerboard[3] + " won" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + checkerboard[3] + " won" + " **********")
            head1_label.grid(columnspan=3, row=4)
            game_running = False
        if count >= 9:
            warn_label = Label(text="********** " + "It's a Tie" + " **********")
            warn_label.grid(columnspan=3, row=0)
            head1_label = Label(text="********** " + "It's a Tie" + " **********")
            head1_label.grid(columnspan=3, row=4)
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
head_label = Label(text="It is X's Turn")

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
