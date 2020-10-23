initialAmount = 2450
myPerDayContribution = 100
myThreeDayContribution = 100 * 3
totalAmount = 2450 + myThreeDayContribution
myShare = int((1/4) * totalAmount)
donation = totalAmount % 4
print('Initial Amount: ', initialAmount)
print('My contribution: ', myThreeDayContribution)
print('Total amount: ', totalAmount)
print('My share: ', myShare)
print('Donation: ', donation)
