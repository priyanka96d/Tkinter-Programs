print("""Task 2: \nWrite a program that takes Kilometers as input and produces corresponding number of nautical miles. """)

input("Press Enter to execute Program:")

#km is kilometer,NMI is mautical miles
def main():

  #Function for convert kilometer to nautical miles(NMI)
    def calculate(km):
        conv_fact = 0.539956804 #conversion factor
        nmi=km*conv_fact    #Formula for converting kilometer to NMI
        return nmi  #return value of nmi to calling function

    kilo_m=float(input("Enter kilometer which you want to convert:"))
    conversion=calculate(kilo_m)
    print("Equivalent conversion of kilometer into Nautical miles:",conversion)

     
main()
