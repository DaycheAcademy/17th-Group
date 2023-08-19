#listNumber=[]
#x=range(0,100,3)
#for i in x:
#listNumber.append(i)

for num in range(1, 100):
    #if num >1 :
       for b in range(2,num):
         if (num % b ) == 0:
              break
       else : print (num , end="-")

