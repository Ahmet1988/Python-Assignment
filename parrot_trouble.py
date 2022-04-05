def parrot_trouble(talking, hour):
   if talking and (hour < 6 or hour > 22) :
     return True
   else:
     return False 
