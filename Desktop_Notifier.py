import time
from plyer import notification

while True:
    notification.notify(
        title="Please Take Break",
        message='''Doctors recommend rule of 20(work)-20(rest) to prevent eye strain.Digital eye strain is a problem caused by extended digital device use.Symptoms include eye discomfort and fatigue,dry eye,blurry vision,and headaches.''',
        app_icon='c:/Users/Lenovo/Documents/Projects/eye.ico',
        timeout=10
    )
    time.sleep(60*20)