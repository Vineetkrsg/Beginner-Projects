from tkinter import *
import random
guess = random.randint(1, 100)
def check_guess():
    user_input = a_input.get()
    if user_input == "":
        a_label.config(text="Please enter a number!")
    elif not user_input.isdigit():
        a_label.config(text="Please enter a valid number!")
    elif int(user_input) < 1 or int(user_input) > 100:
        a_label.config(text="Please enter a number between 1 and 100!")
    elif int(user_input) > guess:
        a_label.config(text="Too high! Try again.")
    elif int(user_input) < guess:
        a_label.config(text="Too low! Try again.")  
    else:
        a_label.config(text="Congratulations! You guessed the number!")
def reset_game():
    global guess
    guess = random.randint(1, 100)
    a_input.delete(0, END)
    a_label.config(text="Guess the number!")
a = Tk()
a.title("Guess the number")
a.geometry("400x410")
a.minsize(400, 300)
a_label = Label(a, text="Guess the number!", font=("Arial", 15))
a_label1 = Label(a,text="I have choosen a number from 1 to 100", font=("Arial", 10))
a_label2 = Label(a,text="Enter your guess below", font=("Arial", 10))
a_input = Entry(a, width=40, font=("Arial", 10), borderwidth=1, relief="solid")
a_button = Button(a, text="Check", font=("Arial", 10),bg = "#6257F1", fg = "white", borderwidth=0, relief="solid", width=7, height=2, command = check_guess)
a_button1 = Button(a, text="Reset", font=("Arial", 10),bg = "#BCB6BF", fg = "black", borderwidth=0, relief="solid", width=7, height=2, command = reset_game)
a_button2 = Button(a, text="Quit", font=("Arial", 10),bg = "#B337E8", fg = "white", borderwidth=0, relief="solid", width=7, height=2, command = a.destroy)
a_label.pack(pady=20)
a_label1.pack(pady=0.1)
a_label2.pack(pady=30)
a_input.pack(ipady = 5,pady=(0, 20))
a_button.pack(pady=10)
a_button1.pack(pady=10)
a_button2.pack(pady=10)

a.mainloop()
