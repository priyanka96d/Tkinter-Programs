print("""Task 1:
The kinetic energy of a moving object is given by the formula   KE=(1/2)mv**2.  Where m is object’s mass  and v is the velocity.
Write a program that reads the input values from the KB and
display the KE of an object in Joules.
""")
print("1 joules=1kg*m2/s2")
input("Press Enter to execute Program:")

def main():
    
    #Function called for calculate kinetic energy
    def kinetic_energy(m,v):
        
        # The formula for kinetic energy.
        KE = 0.5 * (m * (v**2))
        return KE  #return value of KE to calling function


    mass=float(input("Enter Mass(Kg):"))
    velocity=float(input("Enter Velocity(m/s):"))
    KE = kinetic_energy(mass,velocity)
    print("Kinectic Energy(joules):",KE)
              
main()
