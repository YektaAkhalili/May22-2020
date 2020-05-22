usernames = ["yekta", "johnJohn", "JaneDoe", "Smith"]

new_users = ["yekta", "smith", "Bella"]

for i in range(len(usernames)):
	usernames[i] = usernames[i].lower()

# print(usernames)

for user in new_users:
	if user.lower() in usernames:
		print("This username is already taken.")
	else: 
		print("username available.")