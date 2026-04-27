import os
import time
from datetime import datetime
import platform
import os

def play_alarm():
    system = platform.system()

    if system == "Windows":
        import winsound
        duration = 1000  # milliseconds
        freq = 1000      # Hz
        for _ in range(5):
            winsound.Beep(freq, duration)
            time.sleep(0.5)

    elif system == "Darwin":  # macOS
        os.system("afplay /System/Library/Sounds/Glass.aiff")

    else:  # Linux
        os.system("beep -f 1000 -l 500")

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {now}", end="\r")

        if now == alarm_time:
            print("\n⏰ Wake up buddy!")
            play_alarm()
            break

        time.sleep(1)

# ==== USER INPUT ====
alarm_time = input("Enter alarm time (HH:MM:SS): ")
set_alarm(alarm_time)