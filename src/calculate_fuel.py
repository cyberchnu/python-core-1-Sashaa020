def calculate_fuel(distance):
  fluel_needed = distance*10
  if fluel_needed < 100:
    return 100 - fluel_needed
  else:
    return fluel_needed