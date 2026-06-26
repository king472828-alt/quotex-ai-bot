def check_signal(price, ema_fast, ema_slow, rsi, candle_open, candle_close):

    # BUY
    if (
        ema_fast > ema_slow
        and price > ema_fast
        and rsi > 55
        and candle_close > candle_open
    ):
        return "UP"

    # SELL
    elif (
        ema_fast < ema_slow
        and price < ema_fast
        and rsi < 45
        and candle_close < candle_open
    ):
        return "DOWN"

    return "WAIT"
