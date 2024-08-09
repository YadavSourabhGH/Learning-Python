import math


def calculate_area(radius):
  if not isinstance(radius, (int, float)):
    return "Radius Must Be A Number"

  elif (radius < 0):
    return "Radius Cannot Be Negative."


  area = math.pi * radius**2
  return area

print(calculate_area("hi"))
