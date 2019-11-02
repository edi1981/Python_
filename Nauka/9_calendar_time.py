import time
import calendar

print("Obecny czas to", time.time())
print("Obecny czas to", time.localtime(time.time()))
print("Obecny czas to", time.asctime(time.localtime(time.time())))



print(calendar.month(2019, 4))
# calendar.setfirstweekday(0) - ustawiamy który dzień, ma być jako pierwszy dzień tygodnia
