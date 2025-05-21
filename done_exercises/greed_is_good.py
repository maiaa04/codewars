def greed(roll):
  numbers = {
    10: roll.count(1),
    2: roll.count(2),
    3: roll.count(3),
    4: roll.count(4),
    5: roll.count(5),
    6: roll.count(6)
  }

  sum = 0
  for x in numbers:
      if numbers[x] >= 3:
         sum += x*100
         numbers[x] -= 3
      if numbers[x] > 0 and (x == 10 or x == 5):
        sum += 10*x*numbers[x]
  return (sum)

roll = [2,2,1,5,1]
print(greed(roll))