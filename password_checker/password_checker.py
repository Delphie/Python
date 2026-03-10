def check_password(password):



	length = len(password)

	if length < 6:
		return "too short."

	elif length <10:
		return "Weak"

	elif length <15:
		return "Medium"

	else:
		return"Strong"



print(check_password("cat"))
print(check_password("mypassword"))
print(check_password("supersecurepassword123"))
print(check_password("123456"))
