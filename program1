def can_crack(n: int) -> bool:
    
    if n <= 0:
        return False

    original = n
    reversed_n = 0
    digit_sum = 0

   
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        digit_sum += digit
        n //= 10

    
    return (reversed_n == original) and (original % digit_sum == 0)



test_inputs = [121, 12321, 7, 0, -121, 18, 11, 171, 303]

for num in test_inputs:
    result = can_crack(num)
    print(f"can_crack({num}) -> {result}")
