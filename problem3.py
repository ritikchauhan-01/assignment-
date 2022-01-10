import re

# Speed should always be in kmph
# Example string = "470kmph, 240kmph, 380kmph, 440kmph, 190kmph, 320kmph, 265kmph"
cars_speed=input()
prices=list(map(int,re.findall('\d+', cars_speed)))
minimum=float("+inf")
answer=0
for i in range(0,len(prices)-1):
  for j in range(i+1,len(prices)):
    answer=abs(prices[i]-prices[j])
    if answer<minimum:
      minimum=answer
      a=prices[i]
      b=prices[j]

print(a,b,minimum)
