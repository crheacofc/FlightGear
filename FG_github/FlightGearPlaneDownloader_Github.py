##Application for downloading FlightGear planes from github
import urllib
import zipfile
import os
from bs4 import BeautifulSoup



from tkinter import *


def apply():
    family = e1.get()
    print("Values applied")


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get()))

master = Tk()
L1 = Label(master, text="Please type the github address",font=("Helvetica", 16)).grid(row=0)
e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Apply', command=apply).grid(row=3, column=2, sticky=W, pady=4)

master.title("Flight Gear Aircraft Installer")

mainloop( )

git_page = e1.get()



os.chdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/")
#check is directory already exists
os.system("git clone " + git_page)


