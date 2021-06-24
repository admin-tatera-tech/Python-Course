balance = 99999
annual_interest_rate = 0.2
monthly_interest_rate = annual_interest_rate / 12
updated_balance = balance
low = updated_balance / 12
high = (balance * (1 + monthly_interest_rate) ** 12) / 12
payment = (high + low) / 2
months = 0
epsilon = 0.01

#increase monthly payment
while (updated_balance >= (0 + epsilon)) and (updated_balance <= (0 - epsilon)):
    
    while (months < 12):
        unpaid_balance = updated_balance - payment
        updated_balance = unpaid_balance + (unpaid_balance * monthly_interest_rate)
        months += 1
    
       
    if updated_balance >0:
        low = payment
        payment = (high + low) /2
    elif updated_balance < 0:
        high = payment
        payment = (high + low) /2
        
print(payment)