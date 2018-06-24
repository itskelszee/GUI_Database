import table
from tkinter import *

win = Tk()
counter = 0
count = 1

#Create a label for each of the column names from the col_list
for i in table.col_list:
    lbl = Label(win, text = i, bg = 'light blue')
    lbl.grid(row = 0, column = counter)
    counter +=1
#Insert line after row of column names for table design
for i in range(len(table.col_list)):
    line = Label(win, text = '-------------------', bg = 'light blue')
    line.grid(row = 1, column = i)

#Create new cursor object that points to the result set
cursorObj = table.tbl.retrieveAll()
cursorObj.execute('SELECT * FROM {tn}'.format(tn = table.table_name))

count_r = 2     #counter for rows
count_c = 0     #counter for columns
for i in cursorObj:                         #i is tuple
    for j in range(len(i)):                 #range is 0-2
        #Create label for individual elements from tuple
        lbl = Label(win, text = i[j], bg = 'light blue')
        lbl.grid(row = count_r, column = count_c)
        count_c+=1
        if count_c == len(table.col_list):
            count_c = 0
            count_r +=1

win.title('Student Records')
win.configure(background = 'light blue')

win.mainloop()
