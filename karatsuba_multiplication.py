def get_product_of_two_numbers_with_karatsuba_method(a, b):
    if a < 10 or b < 10:
        return a * b

    m = max(len(str(a)), len(str(b))) // 2

    a_high = a // 10**m
    a_low = a % (10**m)

    b_high = b // 10**m
    b_low = b % (10**m)

    c = get_product_of_two_numbers_with_karatsuba_method(a_high, b_high)
    d = get_product_of_two_numbers_with_karatsuba_method(a_low, b_low)
    e = get_product_of_two_numbers_with_karatsuba_method(a_high + a_low, b_high + b_low) - c - d

    return c * (10**(m*2)) + e * (10**m) + d
