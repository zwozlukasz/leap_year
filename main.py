
def is_leap_year():
  input_year = int(input("Set year to check: "))
  is_leap = False
  if input_year % 4 == 0:
    is_leap = True
    if input_year % 100 == 0:
        is_leap = True
        if input_year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
  return is_leap


result = is_leap_year()
if result:
  print("leap year")
else:
  print("non-leap year")