number = int(input("sayı giriniz:"))
count = 0
for i in range(2,number) :
  if number % i == 0 :
    count += 1
    break
if count == 0 :
  print(number,"is a prime number")
else:
  print(number,"is not a prime number")
