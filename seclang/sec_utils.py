

def luhn(input):
    """
    From:
    - http://stackoverflow.com/questions/21068074/python-credit-card-validation-code
    """
    digits = [int(c) for c in input if c.isdigit()]
    if len(digits) == 0:
        return False

    checksum = digits.pop()
    digits.reverse()
    doubled = [2*d for d in digits[0::2]]
    total = sum(d-9 if d > 9 else d for d in doubled) + sum(digits[1::2])
    return (total * 9) % 10 == checksum
