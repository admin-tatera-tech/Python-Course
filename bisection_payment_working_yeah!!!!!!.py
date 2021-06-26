balance = 999999
annualInterestRate = 0.18
monthly_interest_rate = annualInterestRate / 12
low = balance / 12
high = (balance * (1 + monthly_interest_rate) ** 12) / 12
payment = (high + low) / 2
months = 0
epsilon = 0.01
in_range = True



#increase monthly payment
while True:
    temp_balance = balance
    #calculate end of year balance with current monthly payment
    for i in range(12):
       
        unpaid_balance = temp_balance - payment
        temp_balance = unpaid_balance + (unpaid_balance * monthly_interest_rate)
            
    #change low and high to narrow in on payment
    if temp_balance > (0 + epsilon):
        low = payment
        payment = (high + low) / 2
        
    elif temp_balance < (0 - epsilon):
        high = payment
        payment = (high + low) / 2
        
    else:
        balance = round(temp_balance, 2)
        payment = round(payment, 2)
        break
print('Lowest Payment: ', payment)