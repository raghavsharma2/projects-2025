# import calendar
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# print(calendar.month(year, month))
import calendar
s = int(input("Enter year: "))
k = int(input("Enter month: "))
print(calendar.month(s, k))
# Timer functionality
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        timer.sleep(1)
        seconds -= 1
    print("Time's up!")