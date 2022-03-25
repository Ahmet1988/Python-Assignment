sayı = input("sayı :")
x = 0
toplam = 0
for i in sayı :
  x = int(i) ** len(sayı)
  toplam += x
if toplam == int(sayı) :
  print(f"{sayı} is an Armstrong number!!!")
else :
  print(f"{sayı} is not an Armstrong number...")
