# создаю калькулятор
import tkinter as tk
window = tk.Tk()
# задал разрешение
window.geometry(f"240x260+100+200")
# задал цвет
window['bg'] = '#00FA9A'
# заголовок
window.title('Калькулятор')

calc = tk.Entry(window)
# окошко ввода:
calc.grid(row=0,column=0, columnspan=3)
# кнопки цифр с указанием места в гриде, растянутых на все 4 стороны с пространством между ними:
tk.Button(text='1',bd=5).grid(row=1,column=0,stick='wens',padx=5,pady=5)
tk.Button(text='2',bd=5).grid(row=1,column=1,stick='wens',padx=5,pady=5)
tk.Button(text='3',bd=5).grid(row=1,column=2,stick='wens',padx=5,pady=5)
tk.Button(text='4',bd=5).grid(row=2,column=0,stick='wens',padx=5,pady=5)
tk.Button(text='5',bd=5).grid(row=2,column=1,stick='wens',padx=5,pady=5)
tk.Button(text='6',bd=5).grid(row=2,column=2,stick='wens',padx=5,pady=5)
tk.Button(text='7',bd=5).grid(row=3,column=0,stick='wens',padx=5,pady=5)
tk.Button(text='8',bd=5).grid(row=3,column=1,stick='wens',padx=5,pady=5)
tk.Button(text='9',bd=5).grid(row=3,column=2,stick='wens',padx=5,pady=5)
tk.Button(text='0',bd=5).grid(row=4,column=0,stick='wens',padx=5,pady=5)
# задал размерность колонкам и рядам
window.grid_columnconfigure(0,minsize=60)
window.grid_columnconfigure(1,minsize=60)
window.grid_columnconfigure(2,minsize=60)

window.grid_rowconfigure(1,minsize=60)
window.grid_rowconfigure(2,minsize=60)
window.grid_rowconfigure(3,minsize=60)
window.grid_rowconfigure(4,minsize=60)




window.mainloop()