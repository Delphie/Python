library late fee function

def calculate_late_fee(days_late):

    if days_late <= 0:
        return 0

    elif days_late <= 5:
        return days_late * 1

    else:
        first_five = 5 * 1
        remaining_days = days_late - 5
        remaining_fee = remaining_days * 2
        return first_five + remaining_fee


# Test cases
print(calculate_late_fee(0))
print(calculate_late_fee(3))
print(calculate_late_fee(7))
print(calculate_late_fee(12))



def withdraw(balance, amount):
	
	if amount < 0:
		return "Invalid amount"
	
	fee= 5
	total = amount + fee

      #if total > balance:
      #return "Insufficient funds."

	elif amount > balance :
		return "Insuffiecient funds"
	else:
		new_balance = balance - amount
		return new_balance

print(withdraw(500,30))




def apply_discount(amount):

	if amount < 0:
		return "Invalid amount"
	
	elif amount <50:
		return  amount

	elif amount >=100:
		discount = amount *0.10
		return amount - discount

	else:
		discount = amount * 0.20
		return amount - discount

	



print(apply_discount(30))    # no discount
print(apply_discount(75))    # 10% discount
print(apply_discount(150))   # 20% discount
print(apply_discount(-10))   # invalid









def check_password(password):

	if len(password) < 6:
		return "too short."



print(check_password("cat"))
print(check_password("mypassword"))
print(check_password("supersecurepassword123"))
print(check_password("123456"))
