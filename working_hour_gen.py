#!/usr/bin/python3
import csv
import time
import datetime
import random
import tkinter as tk

from tkinter.font import Font, nametofont
from screeninfo import get_monitors

time_range = 600
version = 'v0.2'

# new version center_win() without pyQt4! 
def center_win (toplevel):
    
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
    
    x = m.x + (m.width - win_width) /2
    y = m.y + (m.height - win_height) *1/4
    
    toplevel.geometry("+%d+%d" % (x, y))       
    toplevel.attributes("-alpha", 1)
    toplevel.update_idletasks()

def work_hour(year, month, day):

    try:
        start_time = datetime.datetime(year, month, day, 9, 0, 0)
        end_time = datetime.datetime(year, month, day, 18, 0, 0)
    except:
        return None, None

    start_time = start_time  + datetime.timedelta(0, random.randint(-1 * time_range, time_range) )
    end_time = end_time  + datetime.timedelta(0, random.randint(-1 * time_range, time_range) )

    ret = '%s - %s' % (start_time.time(), end_time.time())

    print (ret)

    return start_time.time(), end_time.time()

def gen_file(year, month):

    file_name = 'Work_Hour_' + str(year) + '_' + str(month)  + '.csv'   
    file_handle = open(file_name, 'w', buffering=True, newline='')
    csv_writer = csv.writer(file_handle)

    csv_columns = ['Date', 'Check In', 'Check Out']

    csv_writer.writerow(csv_columns)
      
    for i in range(1, 32) :

        try:
            date = datetime.datetime(year, month, i)
        except:
            break

        if date.weekday() < 5:
            print (date.date())
            start_time, end_time = work_hour(year, month, i)

            csv_writer.writerow([date.date(), start_time, end_time])
        else:
            csv_writer.writerow([date.date(), 'N/A', 'N/A'])


    file_handle.close()

def main():

    win = tk.Tk()

    # reset the font
    default_font = nametofont("TkDefaultFont")
    default_font.configure(size=12)
    text_font= nametofont("TkTextFont")
    text_font.configure(size=12)

    win.title('Working Hour ' + version)

    tk.Label(win, text='Year:').grid(row=1, column=1, padx=3, pady=3, sticky='w')
    year_entry = tk.Entry(win, width=4)
    year_entry.grid(row=1, column=2, padx=3, pady=3, sticky='w')

    tk.Label(win, text='Month:').grid(row=2, column=1, padx=3, pady=3, sticky='w')
    month_entry = tk.Entry(win, width=2)
    month_entry.grid(row=2, column=2, padx=3, pady=3, sticky='w')

    tk.Button(win, text='Generate', command=lambda:gen_file(int(year_entry.get()), int(month_entry.get()))
            ).grid(row=3, column=3, padx=3, pady=3, sticky='we')

    center_win(win)

    win.mainloop()

if __name__ == '__main__':    
    main()
