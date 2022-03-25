age = input("75 yaşından büyük sigara bağımlısı mısınız? Y/N").upper().split()
chronic = input("Kronik rahatsızlığınız var mı? Y/N").upper().split()
immune = input("Bağışıklık sisteminiz çok mu zayıf? Y/N").upper().split()
risk = age or chronic or immune
if risk :
  print("You are in risky group")
else :
  print("You are not in risky group")  
