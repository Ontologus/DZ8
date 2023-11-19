def my_rec_max(list1):
  if not list1:
    return
  if len(list1) == 1:
    return list1[0]
  if list1[0] > my_rec_max(list1[1:]):
    return list1[0]
  else:
    return my_rec_max(list1[1:])
print(my_rec_max([1, 3, 5, 9]))
