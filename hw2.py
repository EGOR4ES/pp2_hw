#bool examples:
print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


  bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#while loops exxamples:
i = 1
while i < 6:
  print(i)
  i += 1


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# for loops examples:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)