import random
mesaj_file_read = open("mesaj.txt","r") #eger dosya varsa acar yoksa olusturur

context = mesaj_file_read.read()
mesaj_file_read.close()

print(context)

mesaj_file_write = open("mesaj.txt","w")   #yazma islemi
mesaj_file_write.write("asd")
mesaj_file_write.close()

#numbers_file = open("numbers.txt","w")
with open("numbers.txt", "w") as numbers_file: #python otomatik olarak kapatır dosyanın kullanımı bittikten sonra

    while True:
        random_number = random.randrange(1000)
        print(random_number)
        numbers_file.write(str(random_number))
        numbers_file.write("\n")
        numbers_file.close()
        if random_number == 777:
            numbers_file.write("Found!")
            break
