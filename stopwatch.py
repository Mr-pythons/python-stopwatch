import time
import msvcrt

print("Секундомер")

probel = input("Нажми ENTER если хочешь начать, а если хочешь закончить тоже нажми ENTER: ")
if probel == "":
    for x in range(0, 100000000):
        time.sleep(1)
        print(x)
        if msvcrt.kbhit():
            if msvcrt.getch() == b'\r':
                print("Стоп")
                break