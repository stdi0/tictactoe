from tkinter import *
from random import *
from time import *

WIDTH = 300
HEIGHT = 300
field = {(0,0,100,100): ' ', (100,0,200,100): ' ', (200,0,300,100): ' ',
         (0,100,100,200): ' ', (100,100,200,200): ' ', (200,100,300,200): ' ',
         (0,200,100,300): ' ', (100,200,200,300): ' ', (200,200,300,300): ' '}
figures = []
active_player = choice(['computer', 'human'])
end_of_the_game = False

def restart(event):
    global active_player, end_of_the_game
    if end_of_the_game and event.keysym == 'Return':
        for i in figures:
            canv.delete(i)
        for i in field:
            field[i] = ' '
        end_of_the_game = False
        active_player = choice(['computer', 'human'])    
        if active_player == "computer":
            go()


def end_of_the_game_check():
    global end_of_the_game
    free_space = False
    for i in field.values():
        if i == ' ':
            free_space = True
            break
    if not free_space:
        end_of_the_game = True
        return True
    return False    

def step(event):
    global active_player, end_of_the_game, figures
    if active_player == 'human':
        if end_of_the_game:
            pass
        elif end_of_the_game_check():
            figures.append(canv.create_text(150,150, text="Ничья", font="Verdana 20", justify=CENTER, fill="red"))
        else:
            for coords, mark in field.items():
                if coords[0] <= event.x <= coords[2] and coords[1] <= event.y <= coords[3] and mark == ' ' and field[coords] == ' ':
                    field[coords] = 'x'
                    if coords == (0,0,100,100):
                        figures.append(canv.create_line(10,10,90,90, width=1, fill="black"))
                        figures.append(canv.create_line(10,90,90,10, width=1, fill="black"))
                    elif coords == (100,0,200,100):
                        figures.append(canv.create_line(110,10,190,90, width=1, fill="black"))
                        figures.append(canv.create_line(110,90,190,10, width=1, fill="black"))
                    elif coords == (200,0,300,100):
                        figures.append(canv.create_line(210,10,290,90, width=1, fill="black"))
                        figures.append(canv.create_line(210,90,290,10, width=1, fill="black"))
                    elif coords == (0,100,100,200):
                        figures.append(canv.create_line(10,110,90,190, width=1, fill="black"))
                        figures.append(canv.create_line(10,190,90,110, width=1, fill="black"))
                    elif coords == (100,100,200,200):
                        figures.append(canv.create_line(110,110,190,190, width=1, fill="black"))
                        figures.append(canv.create_line(110,190,190,110, width=1, fill="black"))
                    elif coords == (200,100,300,200):
                        figures.append(canv.create_line(210,110,290,190, width=1, fill="black"))
                        figures.append(canv.create_line(210,190,290,110, width=1, fill="black"))
                    elif coords == (0,200,100,300):
                        figures.append(canv.create_line(10,210,90,290, width=1, fill="black"))
                        figures.append(canv.create_line(10,290,90,210, width=1, fill="black"))
                    elif coords == (100,200,200,300):
                        figures.append(canv.create_line(110,210,190,290, width=1, fill="black"))
                        figures.append(canv.create_line(110,290,190,210, width=1, fill="black"))
                    elif coords == (200,200,300,300):
                        figures.append(canv.create_line(210,210,290,290, width=1, fill="black"))
                        figures.append(canv.create_line(210,290,290,210, width=1, fill="black"))
                    break    
            else:
                return True
            if win_check('x'):
                end_of_the_game = True
                figures.append(canv.create_text(150,150, text="Вы победили", font="Verdana 20", justify=CENTER, fill="red"))
            active_player = "computer"  
            go()

def win_check(mark):
    if field[(0,0,100,100)] == mark and field[(100,0,200,100)] == mark and field[(200,0,300,100)] == mark:
        return True
    elif field[(0,100,100,200)] == mark and field[(100,100,200,200)] == mark and field[(200,100,300,200)] == mark:
        return True
    elif field[(0,200,100,300)] == mark and field[(100,200,200,300)] == mark and field[(200,200,300,300)] == mark:
        return True
    elif field[(0,0,100,100)] == mark and field[(0,100,100,200)] == mark and field[(0,200,100,300)] == mark:
        return True
    elif field[(100,0,200,100)] == mark and field[(100,100,200,200)] == mark and field[(100,200,200,300)] == mark:
        return True
    elif field[(200,0,300,100)] == mark and field[(200,100,300,200)] == mark and field[(200,200,300,300)] == mark:
        return True
    elif field[(0,0,100,100)] == mark and field[(100,100,200,200)] == mark and field[(200,200,300,300)] == mark:
        return True
    elif field[(0,200,100,300)] == mark and field[(100,100,200,200)] == mark and field[(200,0,300,100)] == mark:
        return True

def go():
    print('Call')
    global active_player, end_of_the_game, figures
    if end_of_the_game:
        pass
    elif end_of_the_game_check():
        figures.append(canv.create_text(150,150, text="Ничья", font="Verdana 20", justify=CENTER, fill="red"))
    else:
        while True:
            step = choice(list(field.keys()))
            if field[step] == 'x' or field[step] == 'o':
                continue
            else:
                field[step] = 'o'
                if step == (0,0,100,100):
                    figures.append(canv.create_oval([10,10],[90,90]))
                elif step == (100,0,200,100):
                    figures.append(canv.create_oval([110,10],[190,90]))
                elif step == (200,0,300,100):
                    figures.append(canv.create_oval([210,10],[290,90]))
                elif step == (0,100,100,200):
                    figures.append(canv.create_oval([10,110],[90,190]))
                elif step == (100,100,200,200):
                    figures.append(canv.create_oval([110,110],[190,190]))
                elif step == (200,100,300,200):
                    figures.append(canv.create_oval([210,110],[290,190]))
                elif step == (0,200,100,300):
                    figures.append(canv.create_oval([10,210],[90,290]))
                elif step == (100,200,200,300):
                    figures.append(canv.create_oval([110,210],[190,290]))
                elif step == (200,200,300,300):
                    figures.append(canv.create_oval([210,210],[290,290]))
                break
        if win_check('o'):
            end_of_the_game = True
            figures.append(canv.create_text(150,150, text="Компьютер победил", font="Verdana 20", justify=CENTER, fill="red"))
        active_player = "human"    
root = Tk()
canv = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canv.pack()

canv.create_line(100,0,100,300, width=1, fill="black")
canv.create_line(200,0,200,300, width=1, fill="black")
canv.create_line(0,100,300,100, width=1, fill="black")
canv.create_line(0,200,300,200, width=1, fill="black")

root.bind("<Button-1>", step)
root.bind("<KeyPress>", restart)

if active_player == "computer":
    go()

root.mainloop()

