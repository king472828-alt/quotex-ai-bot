from strategy import check_signal

def backtest(candles):
    total = 0
    up = 0
    down = 0

    for candle in candles:
        signal = check_signal(candle["close"], candle["close"])

        if signal == "UP":
            up += 1
        elif signal == "DOWN":
            down += 1

        total += 1

    print("Total Candles:", total)
    print("UP Signals:", up)
    print("DOWN Signals:", down)
