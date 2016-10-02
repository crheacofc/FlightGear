import numpy as np
from Tkinter import *
fields = ('Altitude', 'Descent Rate', 'Angle of Descent', 'Distance in NM')


def dist(entries):
    a = (float(entries['Altitude'].get()))
    a_p = (float(entries['Descent Rate'].get()))
    alpha = (float(entries['Angle of Descent'].get()))
    gamma = 90-alpha
    S1=0 #speed of first leg
    n = 100
    for i in range(0,n):
        h = (a-i*((a-1600)/n)) #altitude
        S1 += .69*(340-(140/120000)*h) #using speed of sound calculations given altitude and mach speed
    S1 = S1/n #averaging for leg 1
    S2 = 0
    for i in range(0,n):
        S2+= 25317
    S2 = S2/n
    x_p=S1+S2
    ang_val = (np.cos(gamma*(np.pi/180.)))**2
    x = ((a*a_p)/x_p)*(1/ang_val-1)*0.000164579
    entries['Distance in NM'].delete(0,END)
    entries['Distance in NM'].insert(0, x )
    #print("Distance in NM: %f" % float(x))
    
def makeform(root, fields):
    entries = {}
    vals=[35000,1800,3,0]
    count = 0 
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(vals[count],str(vals[count]))
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
        count +=1
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    #root.bind('', (lambda event, e=ents: fetch(e)))   
    b2 = Button(root, text='Distance',
          command=(lambda e=ents: dist(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
