from tkinter import *
root = Tk()

title = Label(root, text="My Summer Plans")
title.pack()
root.geometry("600x500")
scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(root, width = 40, height=10, yscrollcommand=scrollbar.set)
    
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

frame = Frame(root)
frame.pack(pady=10)
    
Label(frame, text="Event").grid(row=0, column=0, padx=5, pady=5)
Label(frame, text="Date").grid(row=1, column=0, padx=5, pady=5)
Label(frame, text="Time").grid(row=2, column=0, padx=5, pady=5)
    
event = Entry(frame)
Date = Entry(frame)
Time = Entry(frame)
    
event.grid(row=0, column=1, padx=5, pady=5)
Date.grid(row=1, column=1, padx=5, pady=5)
Time.grid(row=2, column=1, padx=5, pady=5)

def AClick():
    event_text = event.get()
    date_text = Date.get()
    time_text = Time.get()
    global mylist
    mylist.insert(END, str(event_text) + ", " + str(date_text) + ", " + str(time_text))
#Parts of button code gotten from somewhere else!

def BClick():
    mylist.insert(END, "PLACEHOLDER")

button = Button(frame, text="Add an event!", command = AClick)
button.grid(row=3, column=0, columnspan=2, pady=20)

button2 = Button(frame, text="Remove Last Event!", command = BClick)
button2.grid(row=4, column=0, columnspan=2, pady=20)




root.mainloop()

