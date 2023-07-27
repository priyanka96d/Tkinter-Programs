print(""" Task 6: 
A simple text file contains pay roll info as follows <last name> <hourly wage><hours worked>.
Write a program that takes the input file name from the user, reads the file, calculates the pay and prints a report. Assume the file is available in .txt format.
\n""")

input("Press Enter to Execute Program:")

def main():
       
       #CSV is a simple file format used to store tabular data, such as a spreadsheet or database
       import csv
       Datafile=input("Enter your FileName:") #taking file name from user
       with open(Datafile,'r') as csv_file:   #opening file in read mode as csv file
              csv_reader=csv.reader(csv_file)    #using reader() method of csv , parsing file data 
              print("   PayRoll Report      ")
              next(csv_file) #skip first sentence in data file(first sentence is column introduction)
       #iterate sentences of file
              for line in csv_reader: 
                     print("\nLast Name: ",line[0], "\nHourly wages:",line[1],"\nHours Worked:",line[2],"\nTotal Pay:",(int(line[1]))*(int(line[2])))
                     print(".................................\n")
main()
    
#line = sentence in data file
#line[0]= First element in sentence(line)
#line[1]= Second element in sentence(line)
#line[2]= Thrid element in sentence(line)
