def mean(number):
  number_str = str(number)
  sum=0
  for i in (number_str):
    sum+=int(i)
    mean=sum/len(number_str)
    return int(mean)

