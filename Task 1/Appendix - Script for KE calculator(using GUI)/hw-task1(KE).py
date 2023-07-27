print("""Task 1:
The kinetic energy of a moving object is given by the formula   KE=(1/2)mv**2.  Where m is object’s mass  and v is the velocity.
Write a program that reads the input values from the KB and
display the KE of an object in Joules.
""")
print("1 joules=1kg*m2/s2")


#Graphical User Interface package
from tkinter import *

def main():
    #Tk class is used to create a root window
    top = Tk()
    top.title("Kinetic Energy")
    

    #Function called after pressing calculate button
    def kinetic_energy():
        m=float(E1.get()) # get value of mass in kg from Entry widget E1
        v=float(E2.get()) # get value of velocity(m/s) from Entry widget E2
        # The formula for kinetic energy.
        KE = 0.5 * (m * (v**2))
        value_ke.set(KE)  #set value of KE to thrid Entry widget E3

    #Function called after pressing Reset button
    #set all valuse zero for another operation
    def reset_value():
        value_mass.set(0) 
        value_velo.set(0)
        value_ke.set(0)

    
    

    #Using StringVar() class to entry widgets to track changes to the entered value
    value_mass=StringVar()
    value_velo=StringVar()
    value_ke=StringVar()

    #The Label widget is used to display a text 
    L1 = Label( top, text="Enter Mass(kg)")
    L1.grid(row=0,column=0,padx=5,pady=5,sticky=W+N)
    L2 = Label( top, text="Enter Velocity(m\s)")
    L2.grid(row=1,column=0,padx=5,pady=5,sticky=W+N)
    L3 = Label( top, text="Kinetic Energy(Joules)")
    L3.grid(row=2,column=0,padx=5,pady=5,sticky=W+N)

    #The Entry widget used to enter text from user(E1 for mass,E2 for velocity,E3 for KE)
    E1 = Entry( top, bd =5,textvariable= value_mass)
    E1.grid(row=0,column=1,padx=5,pady=5,sticky=N+E)
    E2 = Entry( top, bd =5,textvariable= value_velo)
    E2.grid(row=1,column=1,padx=5,pady=5,sticky=N+E)
    E3 = Entry( top, bd =5,textvariable= value_ke)
    E3.grid(row=2,column=1,padx=5,pady=5,sticky=N+E)
    
    #Button for calculating KE by calling kinetic_energy function.
    calculate=Button( top, text="calculate", fg="Green",width="12",command=kinetic_energy)
    calculate.grid(row=3,column=1,padx=5,pady=5,sticky = S+E)
    
    #Button for reset values from all entry widget so that new set of data would enter 
    reset=Button( top, text="Reset", fg="red",width="12",command=reset_value)
    reset.grid(row=3,column=0,padx=5,pady=5,sticky = S+W)

    top.mainloop()    
  
main()
