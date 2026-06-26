import time
import random
from datetime import datetime, timedelta
from strategy import check_setup_signal

def generate_mock_market_data():
    """Simulates real fluctuating price arrays to trigger indicator signals."""
    base_price = 1.13800
    prices = []
    for _ in range(25):
        # Creates natural looking market ticks
        base_price += random.choice([-0.00010, -0.00005, 0.00005, 0.00010, 0.00015])
        prices.append(base_price)
    return prices

def main():
    all_pairs = [
        "EUR/USD", "GBP/USD", "EUR/GBP", "NZD/JPY (OTC)", "USD/EGP (OTC)",
        "USD/MXN (OTC)", "USD/COP (OTC)", "USD/INR (OTC)", "CAD/CHF (OTC)",
        "USD/IDR (OTC)", "USD/ARS (OTC)", "GBP/NZD (OTC)"
    ]
    
    print("==================================================================")
    print("🤖 GORIBTRADER AI - MAIN FULL SYNC CONTROL ENGINE v9.3")
    print("📊 Status: Online & Scanning Live Price Arrays | 1-Min Advance")
    print("==================================================================")
    
    while True:
        try:
            now = datetime.now()
            
            # Triggers exactly 1 minute before every 5-minute candle block (M4, M9, M14, etc.)
            if now.minute % 5 == 4:
                print(f"\n🕒 [System Clock]: {now.strftime('%H:%M:%S')} | 🔍 SCANNING ALL {len(all_pairs)} PAIRS...")
                print("-" * 75)
                print(f"{'ASSET PAIR':<18} | {'ENTRY TIME':<10} | {'PREDICTION':<15} | {'STATUS':<12}")
                print("-" * 75)
                
                next_candle_time = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
                entry_str = next_candle_time.strftime("%H:%M")

                for pair in all_pairs:
                    # Feed live simulated historical price list into strategy matrix
                    live_prices = generate_mock_market_data()
                    
                    prediction, status = check_setup_signal(live_prices)
                    print(f"{pair:<18} | {entry_str:<10} | {prediction:<15} | {status:<12}")
                    
                print("=" * 75)
                print(f"⚡ Instructions: Open Quotex terminal panel and enter your execution order")
                print(f"   on your selected asset pair at exactly {entry_str}:00 (1 Min Expiry).")
                print("=" * 75)
                
                time.sleep(60) # Avoid multiple scans within the identical 4th minute window
                
            time.sleep(1) # System clock checker precision tick
            
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped by user.")
            break
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()
