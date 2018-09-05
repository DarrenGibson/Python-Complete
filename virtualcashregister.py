#==================================================================
#			             Virtual cash register
#==================================================================

''' 
Date    : Tue 04 Sep 2018 10:46:15 PM PDT 
Subject : python
Title   : virtual cash register
Source  : https://www.youtube.com/watch?v=sHa827pDvnw&t=70s
''' 

#

'''
NOTES:

'''

# 

from tkinter import*
import random 
import time;
import datetime

register = Tk()
register.geometry('1350x650+0+0')
register.title('billing systems')

top_frame = Frame(register, width = 1350, height = 100, bd=8, relief='raise')
top_frame.pack(side=TOP)

frame_1 = Frame(register, width = 900, height = 650, bd = 8, relief = 'raise')
frame_1.pack(side=LEFT)
frame_a = Frame(frame_1, width = 900, height =330, bd = 8, relief = 'raise')
frame_a.pack(side=TOP)
frame_b = Frame(frame_1, width = 900, height =320, bd = 8, relief = 'raise')
frame_b.pack(side=BOTTOM)

frame_b = Frame(register, width = 440, height =650, bd = 8, relief = 'raise')
frame_b.pack(side=LEFT)






register.mainloop()










































