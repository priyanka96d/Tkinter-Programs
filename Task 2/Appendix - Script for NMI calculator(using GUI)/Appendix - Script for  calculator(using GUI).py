print("""Task 2: \nWrite a program that takes Kilometers as input and produces corresponding number of nautical miles. """)

#km is kilometer,NMI is mautical miles
#Graphical User Interface package
from tkinter import *

def main():
    
    #Function called after pressing convert button used for convert kilometer to nautical miles(NMI)
    def calculate():
        conv_fact = 0.539956804 #conversion factor
        km=E1.get() # get kilometer value from Entry widget E1
        km=float(km)
        nmi=km*conv_fact    #Formula for converting kilometer to NMI
        value_nmi.set(nmi)  #set value of nmi to thrid Entry widget E3

    #Function called after pressing Reset button
    #set all valuse zero for another operation
    def reset_value():
        value_km.set(0)
        value_nmi.set(0)

    #Tk class is used to create a root window
    top = Tk()
    top.title("coversion")

    #Using StringVar() class to entry widgets to track changes to the entered value
    value_km=StringVar()
    value_nmi=StringVar()

    #The Label widget is used to display a text
    L1 = Label( top, text="kilometer")
    L1.grid(row=0,column=0,padx=5,pady=5,sticky=W+N)
    L2 = Label( top, text="NMI")
    L2.grid(row=1,column=0,padx=10,pady=10,sticky=S+W)

    #The Entry widget used to enter text from user(E1 for kilometer ,E2 for nautical miles)
    E1 = Entry( top, bd =5,textvariable= value_km)
    E1.grid(row=0,column=1,padx=5,pady=5,sticky=N+E)
    E2 = Entry( top, bd =5,textvariable= value_nmi)
    E2.grid(row=1,column=1,padx=5,pady=5,sticky=S+E)

    #Button for calculating KE by calling calculate function.
    convert=Button( top, text="calculate", fg="Green",width="12",command=calculate)
    convert.grid(row=2,column=1,padx=5,pady=5,sticky = S+E)

    #Button for reset values from all entry widget so that new set of data would enter 
    reset=Button( top, text="Reset", fg="red",width="12",command=reset_value)
    reset.grid(row=2,column=0,padx=5,pady=5,sticky = S+W)

    top.mainloop()    
  
main()
