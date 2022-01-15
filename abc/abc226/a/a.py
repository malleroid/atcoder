import decimal

X = input()
X.replace('.', '')[:-2]

print(decimal.Decimal(X).quantize(
    decimal.Decimal('1'), rounding=decimal.ROUND_HALF_UP))
