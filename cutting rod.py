def rod_cutting(price, n):
    if n == 0:
        return 0
    max_val = -99999
    for i in range(0, n):
        max_val = max(max_val, price[i] +
                      rod_cutting(price, n - i - 1))
    return max_val


arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is", rod_cutting(arr, size))
