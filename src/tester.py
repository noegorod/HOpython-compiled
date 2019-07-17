#testeador de libreria

import ctypes as C
calcu = C.CDLL('./libdin.so')

##add_int

print("integer result")
print(calcu.add_int(1,3))

##add_int_ref

##add_float

print("float result")
calcu.add_float.restype = C.c_float
calcu.add_float.argtypes = [C.c_float, C.c_float]
print(calcu.add_float(1,3))

##add_float_ref

##add_int_array

print ("array result")
vec1 = (C.c_int * 3) (1, 2, 3)
vec2 = (C.c_int * 3) (4, 5, 6)
print(calcu.add_int_array(C.byref(vec1), C.byref(vec1)))



##dot_product



