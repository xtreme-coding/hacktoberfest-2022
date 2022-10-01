def find_gcd(n1, n2):
    """
    Recursively finds the greatest common divisor of n1 and n2.
    """
    if n2 == 0:
        return n1
    else:
        return find_gcd(n2, n1 % n2)


gcd = find_gcd(7395, 105)
print(gcd)  # 15
