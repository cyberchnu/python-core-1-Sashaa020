def mean(number):
  number_str = str(number)
  sum=0
  count=0
  for i in number_str:
    if i.isdigit():
      sum+=int(i)
      count=1
  if count==0:
    return 0
  else:
    return sum/count
