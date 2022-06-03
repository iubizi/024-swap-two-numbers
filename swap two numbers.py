a = 12345
b = 678910

print('a =', a, end='\t'); print('b =', b)

####################
# XOR
####################

a = a ^ b
b = a ^ b
a = a ^ b

print('a =', a, end='\t'); print('b =', b)

####################
# +-
####################

a = a + b
b = a - b
a = a - b

print('a =', a, end='\t'); print('b =', b)

####################
# temp
####################

temp = a
a = b
b = temp

print('a =', a, end='\t'); print('b =', b)

####################
# python
####################

a, b = b, a

print('a =', a, end='\t'); print('b =', b)
