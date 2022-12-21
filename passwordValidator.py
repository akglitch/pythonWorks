def valid_password(password):
	correct_length = False
	has_uppercase = False
	has_lowercase = False
	has_digit = False
	
	
	if len(password) >= 7:
			correct_length =True
			

			for letter in password:
				if letter.isupper():
					has_uppercase = True
					
					
				elif letter.islower():
					has_lowercase = True
					
				
				elif letter.isdigit():
					has_digit =True
					
	
	if correct_length and has_uppercase and has_lowercase and has_digit:
				return True
				
	else:
				return False
				
				
print(valid_password("Kay555teezy"))