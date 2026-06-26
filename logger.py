
from datetime import datetime

def log_signal(signal, price):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("signals.log", "a") as file:
        file.write(f"{now} | {signal} | Price: {price}\n")

    print(f"{now} | {signal} | Price: {price}")
