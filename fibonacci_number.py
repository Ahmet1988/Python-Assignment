	
inp1 = int(input("Write a number and see the fibonnacci's :"))
counter = 0
a = 0
b = 1
print(a ,end=" ")
while inp1 > counter :
  print(b , end=" ")
  a, b = b, a+b
  counter += 1
