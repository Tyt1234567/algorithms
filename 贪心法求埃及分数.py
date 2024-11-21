import fractions
from fractions import Fraction
a=int(input("分子="))
b=int(input("分母="))

num=Fraction(a,b)
while  True :
    if a !=1:
        c=b//a
        d=b%a
        e=c+1
        fraction=Fraction(1,e)
        print(Fraction(1,e))

        num=num-Fraction(1,e)
        a=num.numerator
        b=num.denominator
    else:
        print(Fraction(a,b))
        break