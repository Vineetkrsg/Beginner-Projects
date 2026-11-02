from tkinter import *
import random
import math

first=second=operator=None

def get_digit(digit):
    current = text['text']
    if digit == '.' and '.' in current:
        return
    if current == 'Error':
        current = ''
    new_text = current + str(digit)
    text.config(text = new_text)

def clear_text():
    global first, second, operator
    first = second = operator = None
    text.config(text = '')

def get_operator(op):
    global first, second, operator

    if op == 'pi':
        text.config(text = str(round(math.pi, 2)))
        return
    elif op == 'e':
        text.config(text = str(round(math.e, 2)))
        return

    first = text['text']
    operator = op
    text.config(text = '')

def result():
    global first, second, operator

    try:
        if first is None or first == '':
            return

        unary = ['sin', 'cos', 'tan', 'x^2', 'x^3',
                 'sqrt', 'cbrt', 'log', 'ln', '1/x',
                 'n!', 'e^x']

        if operator in unary:
            x = float(first)

            if operator == 'sin':
                res = round(math.sin(math.radians(x)), 2)
            elif operator == 'cos':
                res = round(math.cos(math.radians(x)), 2)
            elif operator == 'tan':
                if math.isclose(x % 180, 90, abs_tol=1e-10):
                    raise ValueError
                res = round(math.tan(math.radians(x)), 2)
            elif operator == 'x^2':
                res = round(x ** 2, 2)
            elif operator == 'x^3':
                res = round(x ** 3, 2)
            elif operator == 'sqrt':
                res = round(math.sqrt(x), 2)
            elif operator == 'cbrt':
                res = round(math.copysign(abs(x) ** (1/3), x), 2)
            elif operator == 'log':
                res = round(math.log10(x), 2)
            elif operator == 'ln':
                res = round(math.log(x), 2)
            elif operator == '1/x':
                res = round(1 / x, 2)
            elif operator == 'n!':
                if x < 0 or not x.is_integer():
                    raise ValueError
                res = math.factorial(int(x))
            elif operator == 'e^x':
                res = round(math.exp(x), 2)

        else:
            second = text['text']

            if second == '':
                return

            x = float(first)
            y = float(second)

            if operator == '+':
                res = x + y
            elif operator == '-':
                res = x - y
            elif operator == '*':
                res = x * y
            elif operator == '/':
                res = round(x / y, 2)
            elif operator == 'x^y':
                res = round(x ** y, 2)
            else:
                res = 'Error'

        if isinstance(res, float) and not math.isfinite(res):
            raise ValueError

        text.config(text = str(res))
        first = None
        second = None
        operator = None

    except (ValueError, ZeroDivisionError, OverflowError):
        text.config(text = 'Error')
        first = second = operator = None

def delete_last():
    current = text['text']
    new_text = current[:-1]
    text.config(text = new_text)

a = Tk()
a.title("Scientific Calculator")
a.geometry("381x543")
a.resizable(False, False)
a.configure(bg="#b1b0b0")

text = Label(a, text='', font="Arial 30", bg="#b1b0b0", fg="white")
text.grid(row = 0, column = 0, pady = (25,25), padx = (1,10), columnspan = 5, sticky='w')

btn1 = Button(a, text="sin", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('sin'))
btn1.grid(row = 1, column = 0)
btn2 = Button(a, text="cos", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('cos'))
btn2.grid(row = 1, column = 1)
btn3 = Button(a, text="tan", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('tan'))
btn3.grid(row = 1, column = 2)
btn4 = Button(a, text="π", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('pi'))
btn4.grid(row = 1, column = 3)
btn5 = Button(a, text="e", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('e'))
btn5.grid(row = 1, column = 4)

btn6 = Button(a, text="x^2", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('x^2'))
btn6.grid(row = 2, column = 0)
btn7 = Button(a, text="x^3", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('x^3'))
btn7.grid(row = 2, column = 1)
btn8 = Button(a, text="x^y", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('x^y'))
btn8.grid(row = 2, column = 2)
btn9 = Button(a, text="√", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('sqrt'))
btn9.grid(row = 2, column = 3)
btn10 = Button(a, text="∛", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('cbrt'))
btn10.grid(row = 2, column = 4)

btn11 = Button(a, text="log", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('log'))
btn11.grid(row = 3, column = 0)
btn12 = Button(a, text="ln", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('ln'))
btn12.grid(row = 3, column = 1)
btn13 = Button(a, text="1/x", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('1/x'))
btn13.grid(row = 3, column = 2)
btn14 = Button(a, text="n!", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('n!'))
btn14.grid(row = 3, column = 3)
btn15 = Button(a, text="e^x", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('e^x'))
btn15.grid(row = 3, column = 4)

btn16 = Button(a, text="7", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(7))
btn16.grid(row = 4, column = 0)
btn17 = Button(a, text="8", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(8))
btn17.grid(row = 4, column = 1)
btn18 = Button(a, text="9", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(9))
btn18.grid(row = 4, column = 2)
btn19 = Button(a, text="/", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('/'))
btn19.grid(row = 4, column = 3)

btn20 = Button(a, text="4", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(4))
btn20.grid(row = 5, column = 0)
btn21 = Button(a, text="5", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(5))
btn21.grid(row = 5, column = 1)
btn22 = Button(a, text="6", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(6))
btn22.grid(row = 5, column = 2)
btn23 = Button(a, text="*", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('*'))
btn23.grid(row = 5, column = 3)

btn24 = Button(a, text="1", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(1))
btn24.grid(row = 6, column = 0)
btn25 = Button(a, text="2", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(2))
btn25.grid(row = 6, column = 1)
btn26 = Button(a, text="3", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(3))
btn26.grid(row = 6, column = 2)
btn27 = Button(a, text="-", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('-'))
btn27.grid(row = 6, column = 3)

btn28 = Button(a, text="0", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit(0))
btn28.grid(row = 7, column = 0)
btn29 = Button(a, text=".", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_digit('.'))
btn29.grid(row = 7, column = 1)
btn30 = Button(a, text="=", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command=result)
btn30.grid(row = 7, column = 2)
btn31 = Button(a, text="+", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command = lambda: get_operator('+'))
btn31.grid(row = 7, column = 3)

btn32 = Button(a, text="AC", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command=clear_text)
btn32.grid(row = 4, column = 4, rowspan=2, sticky=N+S)
btn33 = Button(a, text="DEL", font="Arial 15", width=6, height=2, bg = "#5a5858", fg = "black", command=delete_last)
btn33.grid(row = 6, column = 4, rowspan=2, sticky=N+S)

a.mainloop()
