secret=28

attempts=0

difference=secret-guess or guess-secret

i=0

while i<=5:
    guess=int(input("enteer number"))
    if  guess==secret:
      print("sucsess")
      attemps=5
    else:
       print ("try again")

if difference==range(5):
   print("hot")
elif difference==range(5,10):
   print("warm")
   
elif difference==range(10,20):
   print("cold")
else:
   pritn("ice cold")
   

