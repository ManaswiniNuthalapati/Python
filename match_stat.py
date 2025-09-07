'''ATM Transaction System
Input: (operation, amount) where operation can be "withdraw", "deposit", or "check".
Use match:
"withdraw" → Deduct balance if enough money, else show "Insufficient Balance".
"deposit" → Add to balance.
"check" → Print balance.
Default → "Invalid operation".'''

operation=int(input())
amount=int(input())
balance=10000
match operation:
    case 1:
        if amount<=balance:
            print(balance-amount)
        else:
            print("invalid balance")
    case 2:
        print(balance+amount)
    case _:
        print("Invalid operation")
        
        
        
            
        