# rsd_checker.py
import statistics

def rsd_checker():
    print("🔹 Welcome to the %RSD Checker 🔹")
    try:
        # Ask user for numbers separated by commas
        data_input = input("Enter your data points separated by commas: ")
        data = [float(x.strip()) for x in data_input.split(",")]

        mean = statistics.mean(data)
        stdev = statistics.stdev(data)
        rsd = (stdev / mean) * 100 if mean != 0 else 0

        print(f"\n✅ Mean: {mean:.2f}")
        print(f"✅ Standard Deviation: {stdev:.2f}")
        print(f"✅ %RSD: {rsd:.2f}%")

    except ValueError:
        print("⚠️ Please enter valid numbers!")

if __name__ == "__main__":
    rsd_checker()
