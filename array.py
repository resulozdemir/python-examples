store_items = ['Apple', 1.49, 'Banana', 1 , 'Milk' , 2.99  ]
print(store_items,type(store_items))
print(store_items[2])
print(store_items[0:4])   #0 inci indeksten 4 uncu indexe kadar sıralama

print(store_items[2:])

print(store_items[:2])

store_items[2] = 'Chocolate'



names = [ "Max" ,"Felix" , "Deniz" , "Selin" , "Lucas" , 26, "Sarah" ]

for name in names:
  if type(name) != str:
    print("found!" , name)
    break
  else:
    print(name, "is a string")
