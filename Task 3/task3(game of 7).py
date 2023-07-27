
print("""
Task 3:Game of lucky sevens. Uses a pair of dice. User input a bet amount say $ 20.  Roll the dice. If the dots count 7, then the player wins $4, added to his bet $20, now the bet amount is $24.  Otherwise,   the player looses,  $1 is subtracted, his net bet amount is $19. Get the bet amount from the user. Roll the dice. Print the  roll #, dots count, win or loose and the resultant  bet amount.
Repeat the roll for each ‘enter’  key press and stop the play when the amount is less than or equal to $0. The player looses.
""")

input("Press Enter to execute program:\n")
import random
#sum_dice variable is used to store the summation value of both rolled dice
#bet_amount variable is used to store the user betting amount in dollars

#Function for playing game of lucky 7
def gameon(sum_dice,bet_amount):
    amount=bet_amount
    if sum_dice == 7:
        #global bet_amount
        bet_amount+=4    #if sum of dice is 7 then add 4 to bet amount and update it
        print("you win!!! current amount is:$", bet_amount)
        input("Press Enter if you want to roll again: ") #if user want to play again
    else:
        bet_amount-=1     #if sum is not 7 then deduct 1 from bet amount and update it
        print("Sorry you lose...you did not roll a 7,current amount  is :$",bet_amount)
        input("Press Enter if you want to roll again: ") #if user want to play again
    return bet_amount
def main():
    #take bet amount from user
    bet_amount = int(input("Please enter your bet amount:$"))
    print("Game of lucky sevens begin by rolling dice\n")
    count=0
    sum_dice=0
    #play untill bet amount is greater then zero      
    while bet_amount!=0:
        count+=1
        dice1  = random.randint(1, 6)
        print("value on dice 1: " ,dice1)
        dice2 = random.randint(1, 6)
        print("value on dice 2: " ,dice2 ,"\n")
        sum_dice = dice1 + dice2
        print("Dots count: %d" %sum_dice )
        bet_amount= gameon(sum_dice,bet_amount)
    # stop playing when bet amount is 0 or less
    if bet_amount<=0:
        print("Sorry you loses, your amount is zero")
    print("Number of Rolls: ",count)

main()
