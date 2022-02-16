######################################
# My First usefull script lol
# Needs to be added in autostart, is closing programs specifiec in PROGRAMS_TO_CLOSE
# 
# Author: Stefan Schoerkmeier
# Date: 2/16/2022
######################################
import psutil,os
from datetime import datetime, time


# ====================== Tweakable Parameters ======================
PROGRAMS_TO_CLOSE = ["steam.exe"]
CLOSING_DAYS = [0, 1, 2, 3, 4] # 0 = monday, 1 = tuesday ... according to datetime.today().weekday()
CLOSING_TIME_FRAMES = [(time(5,00), time(11,00)), (time(20,00), time(23,00))] 

# ====================== Helper Methods ============================
def is_in_closing_time():
    current_time = datetime.now().time()

    for start_time, end_time in CLOSING_TIME_FRAMES:
        if start_time < end_time: 
            is_in_time_frame = current_time >= start_time and current_time <= end_time 
        else: 
            #Over midnight: 
            is_in_time_frame = current_time >= start_time or current_time <= end_time 

        if is_in_time_frame:
            return is_in_time_frame

# ====================== Main Program =============================
if __name__ == "__main__":
    current_weekday = datetime.today().weekday()
    while True:
        if current_weekday in CLOSING_DAYS:
            if is_in_closing_time(): 
                for process in (process for process in psutil.process_iter() if process.name() in PROGRAMS_TO_CLOSE):
                    process.kill()



