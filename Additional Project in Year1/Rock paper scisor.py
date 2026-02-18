from tkinter import *
import random

options = ['Rock', 'Paper', 'Scissors']


# Initialize main window
win = Tk()
win.title("Rock Paper Scissors")
win.configure(bg='dark green')
win.geometry("650x600")

Label(win, text='Are You Ready?', font=("Cooper Black", 14), bg='dark green', fg='black').place(x=250,y=50)

# Game logic
def determine_winner(player_choice):
    computer_choice = random.choice(options)
    
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    result_label.config(text=f"You chose {player_choice}, Computer chose {computer_choice}. {result}")


# Create buttons
Button(win, text="Rock", command=lambda: determine_winner('Rock')).place(x=250, y=100, width=150, height=60)
Button(win, text="Paper", command=lambda: determine_winner('Paper')).place(x=250, y=200, width=150, height=60)
Button(win, text="Scissors", command=lambda: determine_winner('Scissors')).place(x=250, y=300, width=150, height=60)

# Result label
result_label = Label(win, text="", font=('Comic Sans MS', 15, 'bold'), bg='dark green', fg='white')
result_label.place(x=100,y=450)

win.mainloop()