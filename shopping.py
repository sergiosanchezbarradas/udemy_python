shopping_list = ["eggs", "pasta", "milk", "pan", "chocolate", "span"]

item_to_find = "pasta"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found,  in position {}".format(found_at))
else:
    print("Item {} not found in this list".format(item_to_find))