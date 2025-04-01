
billTypes = [100, 20, 10, 5, 1]

def hitTheLottery(currentMoney):
    numberOfBills = 0
    for billType in billTypes:
        numberOfBills += currentMoney // billType # Floor division to remove decimal
        currentMoney %= billType # Modulus to get the remainder 

    return numberOfBills

print(hitTheLottery(int(input())))