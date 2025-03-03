a = 5  # Integer
x = -5
y = 1234567896767575

print(a, x, y)
print(type(a))


b = 3.14  # Float
d = -3.14
e = 3.0

print(b, d, e)
print(type(b))

c = 2 + 3j  # Complex
print(c)
print(type(c))

print(f"a is {type(a)}.")
print(f"b is {type(b)}.")
print(f"c is {type(c)}.")
print(f"d is {type(d)}.")
print(f"e is {type(e)}.")
print(f"x is {type(x)}.")
print(f"y is {type(y)}.")


# Convert one type to another
fl_a = float(a)
print(fl_a)
print(f"fl_a is {type(fl_a)}.")

int_b = int(b)
print(int_b)
print(f"int_b is {type(int_b)}.")

print(a, b)
print(fl_a, int_b)