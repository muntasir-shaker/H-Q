#hangman list
import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


#random word
random_word=["man","girl","women","boy"]


#chose one word
word=random.choice(random_word)


#empt word (_):
array=[]
for i in (word):  
 array.append("_")
Array=" ".join(array) 
print(Array) 


#try=6
tr=6


#hangman[0]
print(HANGMANPICS[0])


#list of gussed litter
guessed=[]


#while
while "_" in array and tr>0:


#ask user chose letter
 litter=input("enter one litter\n").lower()


#if in try again continue
 if litter in guessed:
    print("you chose this litter befor try again please")
    continue
 guessed.append(litter) 


#compair between user and letter by if
 if litter not in word:


#yes
   tr-=1
   print(HANGMANPICS[6-tr])
   print(f"you have {tr} trys\n")


#swap


 else:
  for j in range(len(word)):
    if litter==word[j]:
       array[j]=litter
  print(''.join(array))


#if you lose
if tr==0: 
    print("""
    **********************
    ***you lose*********
    ****************
    """)
    print(HANGMANPICS[6])


#else you win
else:
    print("""
    **********************
    ***you win*********
    ****************
    """)
