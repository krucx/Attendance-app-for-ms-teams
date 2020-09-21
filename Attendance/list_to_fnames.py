import os


with open("names.txt","r") as file:
  dict = {}
  for row in file:
    list = row.split(' ')
    fullName = (list[1]+" "+list[0]).upper()
    dict[fullName] = 0


with open("fname.txt","w") as file1:
  file1.write("{},{},\n".format("LECTURE",0))
  for name in dict:
    file1.write("{},{},\n".format(name,dict[name]))
   