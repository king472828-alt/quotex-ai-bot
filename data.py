import csv

def load_data(file_path):
    candles = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            candles.append({
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": float(row.get("volume", 0))
            })

    return candles
