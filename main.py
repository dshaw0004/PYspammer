import time
from tkinter import *

import pyautogui as gui

bgColor = "#bfeefe"
entryBgColor = "#dfffff"


def spam(message, initdelay, delay, number):
    time.sleep(initdelay)
    for i in range(0, number):
        gui.typewrite(message)
        gui.press("enter")
        time.sleep(delay)


def start():
    mes = inputMessage.get()
    inide = initDelayVal.get()
    de = delayVal.get()
    no = timesVal.get()
    spam(message=mes, initdelay=inide, delay=de, number=no)


def help():
    pass


def about():
    pass


root = Tk()
root.resizable(0, 0)
root.geometry("500x310")
root.title("Spammer")
root.configure(bg=bgColor)

# menu bar
menu = Menu(root)
menu.configure(bg="red")
menu.add_command(label="about", command=about)
menu.add_command(label="help", command=help)
root.config(menu=menu)
# ---------


# a frame to place every input items and button
mainFrame = Frame(root, height=260, width=500)
mainFrame.configure(bg=bgColor)
mainFrame.pack(fill=BOTH)
# ---------

# frame for message input
inputFrame = Frame(mainFrame, bg=bgColor, height=100, padx=10)
inputFrame.pack(fill=X)

# message input
Label(inputFrame, text="Enter your message here", bg=bgColor, fg="#654321", font="lucida 16 bold", pady=10).place(
    relx=0.5, rely=0.2, anchor=CENTER, relheight=0.4, relwidth=1.0)
inputMessage = StringVar()
Entry(inputFrame, textvariable=inputMessage, bg=entryBgColor, fg="#456789", font="lucida 10 bold").place(
    relx=0.5, rely=0.6, anchor="c", relheight=0.4, relwidth=1.0)
# ---------
# ---------


# frame for initial delay input
initDelayFrame = Frame(mainFrame, bg=bgColor, height=50, padx=20)
initDelayFrame.pack(fill=X)
initDelayFrame.columnconfigure(0, weight=2)
initDelayFrame.columnconfigure(1, weight=2)

# message input
Label(initDelayFrame, text="Enter initial delay   : ", bg=bgColor,
      fg="#654321", font="lucida 14 bold", pady=10).grid(row=0, column=0, sticky=W)

Button(initDelayFrame, text="i", bg=bgColor, height=1, relief=FLAT).place(
    relx=0.45, anchor=N, rely=0.0)

initDelayVal = IntVar()
Entry(initDelayFrame, textvariable=initDelayVal, bg=entryBgColor, width=25,
      fg="#456789", font="lucida 10 bold").grid(row=0, column=1, sticky=E)
# ---------
# ---------


# frame for delay input
delayFrame = Frame(mainFrame, bg=bgColor, height=50, padx=20)
delayFrame.pack(fill=X)
delayFrame.columnconfigure(0, weight=2)
delayFrame.columnconfigure(1, weight=2)

# message input
Label(delayFrame, text="Enter delay   : ", bg=bgColor,
      fg="#654321", font="lucida 14 bold", pady=10).grid(row=0, column=0, sticky=W)

Button(delayFrame, text="i", bg=bgColor, height=1, relief=FLAT).place(
    relx=0.3, anchor=N, rely=0.0)

delayVal = IntVar()
Entry(delayFrame, textvariable=delayVal, bg=entryBgColor, width=25,
      fg="#456789", font="lucida 10 bold").grid(row=0, column=1, sticky=E)
# ---------
# ---------


# frame for times input
timesFrame = Frame(mainFrame, bg=bgColor, height=50, padx=20)
timesFrame.pack(fill=X)
timesFrame.columnconfigure(0, weight=2)
timesFrame.columnconfigure(1, weight=2)

# message input
Label(timesFrame, text="Number of  times   : ", bg=bgColor,
      fg="#654321", font="lucida 14 bold", pady=10).grid(row=0, column=0, sticky=W)

Button(timesFrame, text="i", bg=bgColor, height=1, relief=FLAT).place(
    relx=0.44, anchor=N, rely=0.0)

timesVal = IntVar()
Entry(timesFrame, textvariable=timesVal, bg=entryBgColor, width=25,
      fg="#456789", font="lucida 10 bold").grid(row=0, column=1, sticky=E)
# ---------
# ---------


# button for starting the spamming process

Button(mainFrame, text="Start", relief=RAISED, fg="#295876", bg="#faebd7",
       width=10, height=1, font="sarif 14 bold", command=start).pack()

# ---------

root.mainloop()
