import time
import winsound

def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(m, s)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

if __name__ == '__main__':
    minutes = int(input("Enter the number of minutes for the timer: "))
    countdown_timer(minutes)
