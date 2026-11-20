# Author: Alizon Martinez
# 11/11/26
# Description: This syntax tests \
# various numeric conversion techniques.\

a = " 101.1 "
b = "55"
c = "402 Stevens"
d = "Number 5 "

a_int = int(a)
# ValueError because 101.1 is not a whole number

b_int = int(b)

c_int = int(c)
# ValueError because text exists

d_int = int(d)
# ValueError because text exists

a_float = float(a)

b_float = float(b)

c_float = float(c)
# ValueError because text exists

d_float = float(d)
# ValueError because text exists

a_float_to_int = int(float(a))

c_num = c[:3]

print(c_num)

c_num_int = int(c_num)

d_num = d[-2]

d_num_int = int(d_num)

print(a.strip())
print(d.strip())

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print(a_float, type(a_float))
print(b_int, type(b_int))
print(b_float, type(b_float))
print(a_float_to_int, type(a_float_to_int))

# int(a) causes a ValueError because 101.1 is not an integer.

# float(a) works because 101.1 is a valid decimal value.

# int(float(a)) works because float()
# converts it first, then int() removes decimals.

# strip() removes leading and trailing spaces.