# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
  arr = []
  for x in recipe:
    if x not in available:
      return 0
    arr.append(int(available[x]/recipe[x]))
  return min(arr)

needed = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
owned = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(needed, owned))