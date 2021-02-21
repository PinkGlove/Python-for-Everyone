def computepay(h, r):
	if h <= 40:
		return h * r
	else:
		return 40 * r + (h - 40) * 1.5 * r


hrs = input("Enter Hours:")
rates = input("Enter rates:")
p = computepay(float(hrs), float(rates))
print("Pay", p)
