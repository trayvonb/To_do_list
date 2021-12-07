my_To_Do_List = []
#print(my_To_Do_List)
#print(len(my_To_Do_List))
#print(my_To_Do_List.index("buy christmas presents"))
# print("my_To_Do_List")
# for task in my_To_Do_List:
#  print (task)
#  print("what would you like to add?")
#  add = input()
# my_To_Do_List.append(add)
# for task in my_To_Do_List:
#   print (task)
#   print("what would you like to remove?")
#   remove = input()
#   my_To_Do_List.remove(remove)
#   for task in my_To_Do_List:
#     print(task) 
if len(my_To_Do_List) == 0:
  print ("what would you like to add?")
add = input()
my_To_Do_List.append(add)

print("My To Do List")
for task in my_To_Do_List:
 print (task)