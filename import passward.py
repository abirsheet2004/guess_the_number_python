import random
pas=['a','b','c','d','e','f','g'
'h','i','j','k','l','m','n',
'o','p','q','r','s','t','u',
'v','w','x','y','z','A','B',
'C','D','E','F','G','H','I',
'J','K','L','M','N','O','P',
'Q','R','S','T','U','V','W',
'X','Y','Z','1','2','3','4',
'5','6','7','8','9','0','&',
'!','@','#','$','%','_']
Password=""
for i in range(8):

  Password=Password+random.choices(pas)[0]
print("your password:",Password)
