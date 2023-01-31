# class ComplexNumber :
#     def __init__(self,real_part,imag_part):
#         self.real_part = real_part
#         self.imag_part = imag_part
#     def __add__(cn1,cn2) :
#         real_part = cn1.real_part + cn2.real_part
#         imag_part = cn1.imag_part + cn2.imag_part
#         return complex(real_part,imag_part)

#     def __mul__(cn1,cn2) :
#         real_part = cn1.real_part * cn2.real_part-cn1.imag_part * cn2.imag_part
#         imag_part = (cn1.real_part * cn2.imag_part) + (cn1.imag_part *cn2.real_part) 
#         return complex(real_part,imag_part)

# cn1 = ComplexNumber(5,3)
# print("Complex Number 1 :- " + str(complex(cn1.real_part,cn1.imag_part)))

# cn2 = ComplexNumber(6,4)
# print("Complex Number 2 :- " + str(complex(cn2.real_part,cn2.imag_part)))

# print("Adding two complex numbers we get :-",end=" ")
# print(cn1+cn2)

# print("Multiplying two complex numbers we get :-",end=" ")
# print(cn1*cn2)

from datetime import datetime

def print_time(self) :
    
    print(str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))
    # OR
    # print(now.strftime("%H:%M:%S"))

now = datetime.now()
print_time(now)
