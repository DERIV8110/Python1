hour=int(input('enter a hour between 1-12> '))
ahead=int(input('enter number of hours ahead> '))
x=hour+ahead
if x>12:
    print(x-12, "o'clock")
else:
    print(x, "o'clock")