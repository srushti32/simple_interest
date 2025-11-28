import sys

if len(sys.argv) != 4:
    print("usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

p = float(sys.argv[1])
R = float(sys.argv[2])
T = float(sys.argv[3])

s1 = (p * R * T) / 100

print("simple interest:", s1)


