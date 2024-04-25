import random

def miller_rabin_test(n, k = 5):
    """
    Miller-Rabin primality test.

    Parameters:
    - n: The number to be tested for primality.
    - k: The number of iterations for the test. Higher k means higher accuracy.

    Returns:
    - True if n is likely to be prime, False if n is definitely composite ( more than 2 factors) .
    """
    if n <= 1: # composite
        return False
    if n == 2 or n == 3: # prime numbers
        return True
    if n % 2 == 0: # even numbers are composite
        return False

    # Find an odd number d s.t. n-1 can be written as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0: #do the while until d becomes odd
        r += 1
        d //= 2 #divide d by 2

    # perform the primality test k times
    for _ in range(k):
        # Choose a random integer a in the range [2, n-2]
        a = random.randint(2, n - 2)
        # Compute x = a^d mod n
        x = pow(a, d, n)
        # Check if x is 1 or n-1; if true, continue to the next iteration
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            # Compute x = x^2 mod n
            x = pow(x, 2, n)
            # If x is congruent to n-1, break out of the loop
            if x == n - 1:
                break
        else:
            return False  # n is definitely composite

    return True  # n is likely to be prime

number_to_test = 5  # Replace this with the number you want to test
is_prime = miller_rabin_test(number_to_test)
print(f"{number_to_test} is {'probably prime' if is_prime else 'composite'}")
