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
    case "withdraw":
        if amount<=balance:
            print("withdraw",balance-amount)
        else:
            print("invalid balance")
    case "deposit":
        print("deposit",balance+amount)
    case "check":
        print("check",balance)
    case _:
        print("Invalid balance")
        
'''
3. Password Strength Checker
Input: A password string.
Use match to classify:
Only numbers → "Weak".
Only letters → "Medium".
Letters + Numbers → "Strong".
Letters + Numbers + Special chars → "Very Strong".
'''
password=input()
match str:
    case "numbers":
        print("Weak",password.isdigit())
    case "letters":
        print("Medium",password.isalpha())
    case "letters+numbers":
        print("Strong",password.isalpha()+password.isdigit())
    case _:
        print("Very Strong")
        
        

        
        
        
            
        