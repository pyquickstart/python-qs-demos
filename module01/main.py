# variables for a cryptocurrency transaction
coin = "bitcoin"    # str
amount = 0.5        # float
buy = True          # bool

import datetime     # import the datetime module
timestamp = datetime.date(2026, 2, 20) # date

# display the values of the variables

print(coin)         # bitcoin
print(amount)       # 0.5
print(buy)          # True
print(timestamp)    # 2026-02-20

print(timestamp.strftime("%b. %e, %Y"))     # Feb. 20, 2026

print(f"Transaction for {amount} {coin} on {timestamp.strftime('%b. %e, %Y')}")
# Transaction for 0.5 bitcoin on Feb. 20, 2026

# conditionals

print(f"{buy} {amount} of {coin} on {timestamp.strftime('%b. %e, %Y')}")
# True 0.5 of bitcoin on Feb. 20, 2026

if buy == True:
    action = "Bought"
else:
    action = "Sold"

print(f"{action} {amount} of {coin} on {timestamp.strftime('%b. %e, %Y')}")
# Bought 0.5 of bitcoin on Feb. 20, 2026

print(f"{'Bought'if buy == True else 'Sold'} {amount} of {coin} on {timestamp.strftime('%b. %e, %Y')}")
# Bought 0.5 of bitcoin on Feb. 20, 2026