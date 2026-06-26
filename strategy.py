def check_signal(price, ema):
    if price > ema:
        return "UP"
    elif price < ema:
        return "DOWN"
    return "WAIT"
