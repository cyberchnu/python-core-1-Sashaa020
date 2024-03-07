def mean(number):
  number_str = str(number)
  sum=0
  for i in number_str:
    inti=int(i)
    sum=sum+inti
    average=sum/len(number_str)
    return average

