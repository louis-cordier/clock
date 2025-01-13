from datetime import datetime , timedelta
import os
import time
  
def ask_hour_return_datetime():
    H = int(input('choose the hours'))
    M = int(input('Choose the minutes'))
    S = int(input('choose the secondes'))
    new_date = datetime.now()
    new_date = new_date.replace(hour=H, minute=M, second=S)
    return new_date

#debut de ma boucle principale

def main_process():    
    manual_hours_datetime= ask_hour_return_datetime()
    if manual_hours_datetime: 
        while True:
            manual_hours_datetime = manual_hours_datetime + timedelta(seconds=1)
            os.system('cls')
            date_time = manual_hours_datetime.strftime('%H:%M:%S')
            print(date_time)
            time.sleep(1)  

# fin de la boucle principale    
        
def alarm():

        minutes = int(input('choose minutes'))
        hour = int(input('choose hour'))  
        new_alarm = datetime.now()
        new_alarm = new_alarm.replace(hour=hour, minute=minutes)
       
        user_clock = ask_hour_return_datetime()
        print(user_clock)
        print(new_alarm)

        while True:
            current_time= datetime.now()
            if current_time >= new_alarm: 
                user_clock= user_clock+ timedelta(seconds=1)       
                print ('ding_dong') 
                time.sleep(1)
                break

alarm()
main_process()

