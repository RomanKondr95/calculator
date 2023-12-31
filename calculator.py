# создаю калькулятор
import tkinter as tk

def add_digit(digit):
    """
    функция добавляет цифру

    """
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)
    calc['state'] = tk.DISABLED

def add_operation(operation):
    """
    функция добавляет операцию

    """
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED

def calculate():
    """
    функция вычисления

    """
    value = calc.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))
    calc['state'] = tk.DISABLED

def clear():
    """
    функция очистки

    """
    value = calc.get()
    if value != '0':
        new_value = value[:-1]
    calc['state'] = tk.NORMAL
    if len(value) != 1:
        calc.delete(0, tk.END)
        calc.insert(0, new_value)
    else:
        calc.delete(0, tk.END)
        calc.insert(0,'0')
    calc['state'] = tk.DISABLED
    

def make_digit_button(digit):
    """
    функция для создания кнопки цифры
    
    """
    return tk.Button(text=digit,bd=10,font=('Arial',13),command=lambda:add_digit(digit))

def make_operation_button(operation):
    """
    функция для создания кнопки операции
    
    """
    return tk.Button(text=operation,bd=5,font=('Arial',13),command=lambda:add_operation(operation),fg='red')

def make_calc_button(operation):
    """
    функция для создания кнопки вычисления
    
    """
    return tk.Button(text=operation,bd=5,font=('Arial',13),command=calculate,fg='red')

def make_clear_button(operation):
    """
    функция для создания кнопки очистки
    
    """
    return tk.Button(text=operation,bd=5,font=('Arial',13),command=clear,fg='red')

def press_key(event):
    """
    функция привязывает кнопки к клавиатуре

    """
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\b':
        clear()


def make_clear_button(operation):
    """
    функция для создания кнопки очистки
    
    """
    return tk.Button(text=operation,bd=5,font=('Arial',13),command=clear,fg='red')

def press_key(event):
    """
    функция привязывает кнопки к клавиатуре

    """
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\b':
        clear()

window = tk.Tk()
# задал разрешение
window.geometry(f"240x270+100+200")
# задал цвет
window['bg'] = '#00FA9A'
# заголовок
window.title('Калькулятор')
# привязка к клавиатуре
window.bind('<Key>',press_key)

calc = tk.Entry(window,justify=tk.RIGHT,font=('Arial',15),width=15)
# по умолчанию стоит 0
calc.insert(0,'0')
# окошко ввода:
calc.grid(row=0,column=0, columnspan=4,stick = 'we',padx=5)
calc['state'] = tk.DISABLED
# кнопки цифр с указанием места в гриде, растянутых на все 4 стороны с пространством между ними:
make_digit_button('1').grid(row=1,column=0,stick='wens',padx=5,pady=5)
make_digit_button('2').grid(row=1,column=1,stick='wens',padx=5,pady=5)
make_digit_button('3').grid(row=1,column=2,stick='wens',padx=5,pady=5)
make_digit_button('4').grid(row=2,column=0,stick='wens',padx=5,pady=5)
make_digit_button('5').grid(row=2,column=1,stick='wens',padx=5,pady=5)
make_digit_button('6').grid(row=2,column=2,stick='wens',padx=5,pady=5)
make_digit_button('7').grid(row=3,column=0,stick='wens',padx=5,pady=5)
make_digit_button('8').grid(row=3,column=1,stick='wens',padx=5,pady=5)
make_digit_button('9').grid(row=3,column=2,stick='wens',padx=5,pady=5)
make_digit_button('0').grid(row=4,column=0,stick='wens',padx=5,pady=5)
# кнопки операций
make_operation_button('+').grid(row=1,column=3,stick='wens',padx=5,pady=5)
make_operation_button('-').grid(row=2,column=3,stick='wens',padx=5,pady=5)
make_operation_button('*').grid(row=3,column=3,stick='wens',padx=5,pady=5)
make_operation_button('/').grid(row=4,column=3,stick='wens',padx=5,pady=5)
# кнопка вычислений
make_calc_button('=').grid(row=4,column=2,stick='wens',padx=5,pady=5)
# кнопка очистки
make_clear_button('C').grid(row=4,column=1,stick='wens',padx=5,pady=5)

# задал размерность колонкам и рядам
window.grid_columnconfigure(0,minsize=60)
window.grid_columnconfigure(1,minsize=60)
window.grid_columnconfigure(2,minsize=60)
window.grid_columnconfigure(3,minsize=60)

window.grid_rowconfigure(1,minsize=60)
window.grid_rowconfigure(2,minsize=60)
window.grid_rowconfigure(3,minsize=60)
window.grid_rowconfigure(4,minsize=60)

window.mainloop()