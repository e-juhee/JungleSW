fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def f(this):
  count = 0
  for fruit in fruits:
    if fruit == this:
      count += 1
  return count

print(f('사과'))

apple_count= f('사과')
print(apple_count)