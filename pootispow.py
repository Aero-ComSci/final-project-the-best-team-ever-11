from tkinter import *
root = Tk()
dminor = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Dates = {
  "Jan": 31,
  "Feb": 29,
  "Mar": 31,
  "Apr": 30,
  "May": 31,
  "Jun": 30,
  "Jul": 31,
  "Aug": 31,
  "Sep": 30,
  "Oct": 31,
  "Nov": 30,
  "Dec": 31,
}
SuperDates = []
eoeo = ""
for x in range(0, 12):
    for y in range(1, Dates[dminor[x]]+1):
        z=(f"{dminor[x]}{" "}{y}")
        z = str(z)
        SuperDates.append(z)

SuperTimes = []
for a in range(0, 24):
    for b in range(0, 60):
        time_str = f"{str(a).zfill(2)}:{str(b).zfill(2)}"
        SuperTimes.append(time_str)




print(SuperDates)
print(SuperTimes)
title = Label(root, text="My Summer Plans")
title.pack()
root.geometry("600x500")
scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT, fill=Y)
activities = Listbox(root, width = 40, height=10, yscrollcommand=scrollbar.set)
    
activities.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=activities.yview)

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

labelerror = Label(frame, text="...")
labelerror.grid(row=6, column=1, padx=5, pady=5)

def AClick():
    event_text = event.get()
    date_text = Date.get()
    time_text = Time.get()
    
    event_text = str(event_text)
    date_text = str(date_text)
    time_text = str(time_text)
    
    
    if date_text in SuperDates:
        if time_text in SuperTimes:
            if len(event_text) > 0:
                activities.insert(END, f"{event_text}{', '}{date_text}{', '}{time_text}{'.'}")
                labelerror.config(text=f"{'Added'}{' '}{activities.get('end')}",fg="green")
                root.after(3000, lambda: [labelerror.config(text='...'), labelerror.config(fg="black")])
                event.delete(0, END)
                Date.delete(0, END)
                Time.delete(0, END)
            else:
                labelerror.config(text = 'Nothing in Event Category!', fg="red")
                root.after(3000, lambda: [labelerror.config(text='...'), labelerror.config(fg="black")])
        else:
            labelerror.config(text = 'Time not valid. In this system, military time is used. Please put a time like "03:06", "12:37", or "19:00 ."', fg="red")
            root.after(3000, lambda: [labelerror.config(text='...'), labelerror.config(fg="black")])
    else:
        labelerror.config(text = 'Date not valid. Please put a date like "Jan 1", "Sep 12", or "Jun 3."', fg="red")
        root.after(3000, lambda: [labelerror.config(text='...'), labelerror.config(fg="black")])
    


def BClick():
    labelerror.config(text=f"{'Removed'}{' '}{activities.get('end')}",fg="green")
    activities.delete("end")
    root.after(3000, lambda: [labelerror.config(text='...'), labelerror.config(fg="black")])

button = Button(frame, text= "Add an event", command = AClick)
button.grid(row=3, column=0, columnspan=2, pady=20)

button2 = Button(frame, text= "Remove Last Event", command = BClick)
button2.grid(row=4, column=0, columnspan=2, pady=20)




root.mainloop()

