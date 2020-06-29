from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# First window for asking first and end node

st = [12, 5] 
ed = [3, 6]
def first_window():
    def onsubmit():
        global st
        global ed
        st = [int(_) for _ in startBox.get().split(',')]
        ed = [int(_) for _ in endBox.get().split(',')]
        print(st, ed)
        window.quit()
        window.destroy()

    window = Tk()
    label_start_node = Label(window, text='Start(x,y): ')
    startBox = Entry(window)
    label_end_node = Label(window, text='End(x,y): ')
    endBox = Entry(window)
    var = IntVar()
    showPath = ttk.Checkbutton(window, text='Show Steps :', onvalue=1, offvalue=0, variable=var)
    submit = Button(window, text='Submit', command=onsubmit)

    label_start_node.grid(row=0, pady=3)
    startBox.grid(row=0, column=1, pady=3)
    label_end_node.grid(row=1, pady=3)
    endBox.grid(row=1, column=1, pady=3)
    showPath.grid(columnspan=2, row=2)
    submit.grid(columnspan=2, row=3)

    window.update()
    mainloop()
    return var, st, ed
