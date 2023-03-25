shopping_list = ["Apple","Banana","Ball","Book"]
print(shopping_list)

shopping_list.append("Water")   #sonuna ekler
print(shopping_list)

shopping_list.insert(2,"Juice") #ikinci indekse ekler 2.indeksteki olan 3.indekse kayar
print(shopping_list)

shopping_list.remove("Apple")  #apple yi siler
print(shopping_list)

shopping_list[3] = "Strawberry"
print(shopping_list)

number_list = [1,2,3,4,5]
square_list = []

for number in number_list:
   square_list.append(number**2)
print(square_list)
#yukarıdaki sekilde veya asagıdaki sekilde yapabilirsin
square_list = [number**2 for number in number_list]
print(square_list)


#listlere sonradan veri ekleyebilir, değiştirebilir veya silebilirsin
#ancak tuplelara tanımladıktan sonra yapamazsın
#listlerden tanımlanırken süslü parantez kullanılır ancak tupleler tanımlanırken
#normal parantez kullanılır
#asagıdaki isleme packecing tuples denir

shopping_list_tuple = ("Apple","Juice","Ball","Book")
#asagıdaki isleme unpackecing tuples denir

item1, item2, item3, item4 = shopping_list_tuple
print(item1)
print(item2)
print(item3)
print(item4)

print(shopping_list_tuple[0])
print(shopping_list_tuple[1:3])

phone_book = {"Resul Ozdemir": "0553 113 10 10", "Ramazan Ozdemir" : "555 333 22 11", "Isim Soyisim" : "544 444 33 22"}
print(phone_book)

print(phone_book["Resul Ozdemir"])

shopping_list = {'item1':'section1', 'item2':'section2'} #bu sekilde de olusturulabilir
inventory = dict()  #bu sekilde bos bir kutuphane olusturabilirsin yukarıdakinın farklı bır tanımlama sekli (phone_book)
inventory["bananas"] = 25  #25 adet muz kaydettik kutuphaneye
inventory["apples"] = 102
inventory["oranges"] = 54
inventory["watermelons"] = 4

print(inventory)

print(inventory["apples"])
print(inventory.keys())
print(inventory.values())
print(inventory.items())

for key in inventory:
    inventory[key] += 100

print(inventory)

for key, value in inventory.items():
    if value > 200:
        print("Too many", key)
    else:
        print("Enough",key)


shopping_list = [("milk","dairy"),("apples","fruits"),("oranges","fruits"),("bananas","fruits"),("onions","vegetables"),("bread","bakery")]
