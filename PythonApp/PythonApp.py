def main():

    again = 1
    multlist = []
    print("For this calculator you must input a minimum of two bet odds!")
    while again == 1:
   
        odds = int(input("Input the odds to the bet! (Must be a positive or negative integer!: "))

        if odds >= 100:
            updatednumber = odds + 100
            multiplier = updatednumber / 100
            round(multiplier, 4)
            multlist.append(multiplier)
            again = int(input("Do you want to enter another bet odds? (1 = yes, 0 = no): "))

        else:
            updatednumber = 100 + abs(odds)
            multiplier = updatednumber / abs(odds)
            round(multiplier, 4)
            multlist.append(multiplier)
            again = int(input("Do you want to enter another bet odds? (1 = yes, 0 = no): "))

    print("Your odds for this parlay are ", multiplyList(multlist), "!")
    bet = int(input("Input the amount you would like to bet to the nearest dollar!: "))
    print("Your payout would be $", bet * multiplyList(multlist), "!")


def multiplyList(list):
    result = 1
    for x in list:
        result = result * x
    return result

main()
