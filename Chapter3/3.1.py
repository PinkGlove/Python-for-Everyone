hrs = input("Enter Hours:")
rates = input("Enter rates:")
h = float(hrs)
r = float(rates)
if h <= 40:
    print(h * r)
else:
    print(40 * r + (h - 40) * r * 1.5)
