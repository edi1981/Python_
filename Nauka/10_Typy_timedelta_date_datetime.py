import datetime

print("%a", datetime.datetime.now().strftime("%a"))
print("%A", datetime.datetime.now().strftime("%A"))
print("%w", datetime.datetime.now().strftime("%w"))
print("%Y-%m-%d_%H_%M_%S_%f", datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))