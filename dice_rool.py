import random
min=1
max=6
rool_again="yes"
while rool_again=="yes" or rool_again=="y":
    print("rolling the dices...")
    print("the values are...")
    print(random.randint(min,max))
    print(random.randint(min,max))
    rool_again=input("rool the dices again?  :")