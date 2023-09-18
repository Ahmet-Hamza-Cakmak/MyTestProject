import time

try:
    hour = int(input("enter the hour: "))
    minute = int(input("enter the minute: "))
    second = int(input("enter the second: "))

except ValueError:
    print("Please enter the values as integers")

total_second = hour*3600 + minute*60 + second

for s in range(total_second,0,-1):

    new_hour = (s // 3600)
    new_minute = (s//60) % 60
    new_second = s % 60

    print(f"{new_hour:02}:{new_minute:02}:{new_second:02}")

    time.sleep(1)

