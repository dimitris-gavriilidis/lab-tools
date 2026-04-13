# sequence_generator.py

def hplc_sequence_generator():
    print("🔹 Welcome to the HPLC Sequence Generator 🔹")
    
    try:
        n = int(input("Enter number of samples to generate: "))
        for i in range(1, n + 1):
            print(f"Sample {i}")
    
    except ValueError:
        print("⚠️ Please enter a valid integer!")

if __name__ == "__main__":
    hplc_sequence_generator()
