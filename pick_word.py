import random
from guessing_letter import*
from szubienica import*

print("welcome inthe Hangman!")

sowpods=[]
with open("sowpods_list.txt","r") as file:
	word=file.readline()
	while word:
		sowpods.append(word)
		word=file.readline()

random_word1=random.choice(sowpods)
# print(random_word)


len=len(random_word1)
unknown_word=(len-1)*("_")
print(unknown_word)
unknown_word=list(unknown_word)
random_word=list(random_word1)
print()
	
guessed_list=[]

licznik=0
while licznik<8:
	letter=guessing_letter()
	if letter in guessed_list:
		print("arleady guessed")
	elif letter in random_word:
		for x in range(0,len-1):
			if letter==random_word[x]:
				unknown_word[x]=letter
				random_word[x]="-"
		print("".join(unknown_word))
		guessed_list.append(letter)
	else:
		szubienica1=szubienica()
		print(szubienica1[licznik])
		licznik+=1
	if licznik==7:
		print("game over")
		print(random_word1)
		exit=input("do you want start again?yes or no\n")
		if exit=="yes":
			continue
		else:
			break
	if "_" not in unknown_word:
		print("you won!!!! :D")
		exit=input("do you want start again?yes or no")
		if exit=="yes":
			continue
		else:
			break
	
	
