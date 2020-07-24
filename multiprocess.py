from screeninfo import get_monitors
from tkinter.font import Font, nametofont
from tkinter import ttk
import tkinter as tk

import time

from multiprocessing import Process, Pipe, freeze_support

'''
this file is about multiprocessing


@author Ta-Ju
@version 2020-07-08
'''

#tk ui center
def center_win(toplevel):

    toplevel.attributes("-alpha", 0)
    toplevel.update_idletasks()

    win_width = toplevel.winfo_width()
    win_height = toplevel.winfo_height()
    win_x = toplevel.winfo_x()
    win_y = toplevel.winfo_y()

    for m in get_monitors():
        if win_x >= m.x and win_x <= m.x+m.width and win_y >= m.y and win_y <= m.y+m.height:
            break
    #print(m.x, m.y, m.width, m.height, win_x, win_y)

    x = m.x + (m.width - win_width) / 2
    y = m.y + (m.height - win_height) * 1/4

    toplevel.geometry("+%d+%d" % (x, y))
    toplevel.attributes("-alpha", 1)
    toplevel.update_idletasks()
##tk ui set
def main():
    
    win = tk.Tk()

    # reset the font
    default_font = nametofont("TkDefaultFont")
    default_font.configure(size=12)
    text_font = nametofont("TkTextFont")
    text_font.configure(size=12)

    win.title('multiprocessing')

    port_list_frame = tk.Frame(win)
    port_list_frame.grid(row=1, column=1, padx=3, pady=3)
  
    ttk.Button(port_list_frame, text="Strat Process", command= lambda:stratprocess()).grid(
        column=1, row=99, padx=3, pady=3, stick='ne')
    ttk.Button(port_list_frame, text="Only Strat One New Process", command= lambda:click()).grid(
        column=2, row=99, padx=3, pady=3, stick='ne')

    center_win(win)
    win.mainloop()
    #close process
    if p.is_alive:
            # stop a process gracefully
            p.terminate()
            print('stop process')
            p.join()

#create new process and close previous process
i, p = 0, None
def click():
    
    global i, p 
    #parent_conn.send(1)
    if i >0 :
        if p.is_alive:
            # stop a process gracefully
            p.terminate()
            print('stop process')
            p.join()
    
    p = Process(target=testprocess)
    p.start()
    i = i+1

#create new process
def stratprocess():
    p = Process(target=testprocess)
    p.start()

# test function
def testprocess():
    for i in range(0, 10):
        print(i)
        time.sleep(1)
    
    

if __name__ == '__main__':

    #use multiprecess in pyinstaller must use freeze_support() before 
    freeze_support()
    main()