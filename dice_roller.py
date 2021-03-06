from tkinter import *

App = Tk()
App.title("Dice Roller")

# Diccionario
Dice = {
    0 : 'ð²',
    1 : 'â',
    2 : 'â',
    3 : 'â',
    4 : 'â',
    5 : 'â',
    6 : 'â'
}


lbl = Label(App, text=Dice[0], font=('Times', 100))
lbl.grid(row=0, column=0, padx=40)


# Escoge un nÃºmero entre 1 y 6 al azar
def roll():
    from random import randint
    dice_choice = randint(1, 6)

    dice_lbl = Label(App, text=Dice[dice_choice], font=('Times', 100), width=2)
    dice_lbl.grid(row=0, column=0, padx=40)


# Boton Roll
roll_button = Button(App, text='Roll', command=roll)
roll_button.grid()

App.mainloop()