# 8. Create a shopping list where the user can add an item and remove an item.
size = int(input("enter the value of size:"))
lists = []
for i in range(size):
    value = input(f"enter the items:")
    lists.append(value)
choice = int(input("do you want to add or delete item, choose - 1 for specific postition , 2 for multiple items, 3. delete an item :"))
match choice :
    case 1 :
        pos = int(input("enter desired pos :"))
        newvalue =input("enter desired new item :")
        lists.insert(pos,newvalue)
        print(lists)
    case 2 :
        size = int(input("enter the no. of items you want to add:"))
        for i in range(size):
            items = input(f"enter the items:")
            lists.extend([items])
        print(lists)   
    case 3 :
        delitem =input("enter desired item to delete :")
        lists.remove(delitem)
        print(lists)
            
            
            
