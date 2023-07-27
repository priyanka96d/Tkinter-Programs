print("""
Task 4: The credit plan in a computer store specifies 20% down payment and 12 % annual interest. Monthly payments are 5% of the listed price minus down payment. Write a program that takes purchase price as input and display the life time payment in tabular form. The table headers are
Month # starts from 1 , Current total balance owed, interest owed for that month, amount of principle owed for that month, the payment for that month, the balance remaining after payment.

""")
input("Press Enter to execute program: ")
def main():
    
#amount= intial user amount/price
#down_payment= 20% of amount paid upfront
#loan_amount = amount - down_payment (finance amount)
#interest= 12%of amount per year i.e. 1% per month 
    amount = input("Enter the purchase price: ")
    amount=float(amount)
    month = 1
    down_payment=0.2* (amount)
    loan_amount=amount- float(down_payment)
    current_Bal = float(loan_amount)
    monthly_pay = float(loan_amount) * .05
    print('Month | Current total balance owed | interest(monthly) |amount of principle(monthly) |  the payment(monthly)  |   the balance remaining after payment')

    while current_Bal >= monthly_pay:
        interest = current_Bal * .01
        Principal = (monthly_pay - interest)
        EndingBalance = (current_Bal - monthly_pay)
        print('{:<10}'.format("{:2.0f}".format(month)), '{:<30}'.format("{:6.2f}".format(current_Bal)), '{:<30}'.format("{:6.2f}".format(round(interest,2))), '{:<15}'.format("{:6.2f}".format(Principal)), '{:<25}'.format("{:6.2f}".format(monthly_pay)), format("{:6.2f}".format(EndingBalance)))
        month += 1
        current_Bal = EndingBalance
main()
