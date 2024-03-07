def int_within_bounds(number, lower_bound, upper_bound):
  if type(number) is float:
    return False
  elif number > lower_bound:
    return True
  elif number < upper_bound:
    return True
  else:
    return False