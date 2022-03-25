age = bool(input("75 yaşından büyük sigara bağımlısı mısınız?:"))
chronic = bool(input("Kronik rahatsızlığınız var mı?:"))
immune = bool(input("Bağışıklık sisteminiz çok mu zayıf?:"))
risk = age or chronic or immune
print(risk)
