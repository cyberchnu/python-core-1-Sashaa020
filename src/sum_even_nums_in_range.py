def sum_even_nums_in_range(start, stop):
  sum_even = 0
  for i in range(start, stop + 1):
    if num % 2==0:
    sum_even += i
  return sum_even