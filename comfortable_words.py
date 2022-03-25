right = set("yuıopğühjklşinmöç")
left = set("qwertasdfgzxcvb")
kelime = set(input("kelime giriniz :"))
print(bool (kelime.difference(right) and kelime.difference(left)))
