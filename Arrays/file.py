alist = []

z = int(input("Enter no of elements:"))


for i in range(z):
  a=int(input())
  alist.append(a)

print(alist)

x = int(input("Enter the element to check: "))

if x in alist:
  print("Present")

else:
  print("Not present")


  