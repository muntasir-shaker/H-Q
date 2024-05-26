import string
#def quiser
def quiser(n,massege): 
 word=string.ascii_lowercase
 code=""
#for 
 for i in massege:
#if1 litter in massege
  if i.lower() in word:  
#yes1:l+2
   position=word.index(i.lower())

################### when I want to decode (position - n)##############################

   new_position=(position - n) % 26
   code_litter=word[new_position]
#if2 upper  
   if i.isupper():
#yes1:make upper    
     code_litter=code_litter.upper()
   code+=code_litter 
#no2
  else:
   code+=i
#print code  
 print(code)
#call function
N=int(input("enter key\n"))
M=(input("enter massege\n"))
quiser(n=N,massege=M)
