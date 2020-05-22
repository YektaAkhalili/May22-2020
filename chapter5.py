hosts = ["dolores","teddy","maeve","clementine","angela","bernard"]

print("is Dolores a host? I think she is!")
print('dolores' in hosts)

if hosts[0] == 'Dolores':
	print("You got it!")
elif hosts[0] == 'dolores':
	print("should've said Dolores, with a capital D!")
else: 
	print("It's just not capital!")

if hosts[0].lower() == 'dolores':
	print("yup")

x = 10
y = 100 

if (x > y):
	print("you're wrong.")
elif (x == y):
	print("you're still wrong.")
else: 
	print("finally!")

if (x < y and y > 50):
	print("great job!")
else:
	print("nope.")

if (x < y or y < 0 ):
	print("still a good job!")	
else:
	print("nope nope nope!")