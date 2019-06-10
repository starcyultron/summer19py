import time
current_time=time.localtime()
current_hour=current_time.tm_hour
name=input("Enter your name:")
if current_hour>=6 and current_hour<12:
    print(f"Good Morning {name}")
elif current_hour>=12 and current_hour<17:
    print(f"Good Afternoon {name}")
elif current_hour>=17 and current_hour<20:
    print(f"Good Evening {name}")
else:
    print(f"Good Night {name}")