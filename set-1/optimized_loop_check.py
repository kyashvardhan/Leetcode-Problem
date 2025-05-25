def count_even_numbers_optimized(arr):
    count = 0
    for num in arr:
        if num == -1:
            break
        if num & 1 == 0:
            count += 1
    return count

def main():
    data = [2, 4, 5, 7, 8, 10, -1, 6, 12]  # -1 stops the loop
    result = count_even_numbers_optimized(data)
    print(f"✅ Even numbers counted before -1: {result}")

if __name__ == "__main__":
    main()
