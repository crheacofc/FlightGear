##Application for downloading FlightGear planes and associated liveries

import urllib
import zipfile
import os
from bs4 import BeautifulSoup



from tkinter import *


def apply():
    family = e1.get()
    name = e2.get()
    print("Values applied")


def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
L1 = Label(master, text="Please type the name of the aircraft (i.e. A320-family) you would like to install",font=("Helvetica", 16)).grid(row=0)
L2 = Label(master, text="Please type the name of the aircraft livery (i.e. Airbus A320) you would like to install",font=("Helvetica", 16)).grid(row=1)
e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Apply', command=apply).grid(row=3, column=2, sticky=W, pady=4)

master.title("Flight Gear Aircraft Installer")

mainloop( )

family = e1.get()
name = e2.get()



os.chdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/")
#check is directory already exists
if os.path.isdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/"+family):
    pass
else:
    os.mkdir(family)


##Create folder to store new plane zip in

zip_ = urllib.urlretrieve ("http://mirrors.ibiblio.org/flightgear/ftp/Aircraft/"+family+".zip", "plane.zip")
zip_ref = zipfile.ZipFile("plane.zip", 'r')
zip_ref.extractall("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/")
zip_ref.close()

# Step 0: Get name of aircraft
# 1 - parse webpage and pick out liveries for our plane of interest
if (name != ""):
    planes = urllib.urlopen("http://liveries.flightgear.org/liveries.php")
    soups = BeautifulSoup(planes, "html.parser")
    data = soups.findAll('a',attrs={'class':'thumbnail'})
    count = 0

    for ind in data:
        type_ = ind.findAll('div',text=name) ##only getting plane livery of interest
        if (type_!=[]):
            #print(ind)
            #now to go to where the name of the zip
            plane = urllib.urlopen("http://liveries.flightgear.org/"+str(ind['href']))
            soup = BeautifulSoup(plane, "html.parser")
            ## now grabbing link for download
            for link in soup.find_all('a', href=True, text = 'DOWNLOAD'):
                print(link['href'])
                #print(link)
                #os.chdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/"+name)
                #os.mkdir(str(count))
                zip_ = urllib.urlretrieve ("http://liveries.flightgear.org/"+str(link['href']), "plane_liv.zip")
                zip_ref = zipfile.ZipFile("plane_liv.zip", 'r')
                zip_ref.extractall("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/"+family+"/Models/Liveries/"+name+"/")
                zip_ref.close()
                #check if there were three or two directories created...
                if (os.path.isdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/"+family+"/Models/Liveries/"+name+"/Models/Liveries/"+name)):
                    os.chdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/"+family+"/Models/Liveries/"+name+"/Models/Liveries/"+name)
                    os.system("cp *.xml ../../..")
                    os.system("cp *.png ../../../..")
                else:
                    os.chdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/"+family+"/Models/Liveries/"+name+"/Models/Liveries/")
                    os.system("cp *.xml ../..")
                    os.system("cp *.png ../../..")
                os.chdir("/Applications/FlightGear.app/Contents/Resources/data/Aircraft/"+family+"/Models/Liveries/"+name)
                #now need to only leave .xml file here...
        count +=1
    os.system("rm -rf Models")
    #os.system("rm -r plane.zip")
    os.system("rm -r plane_liv.zip")
