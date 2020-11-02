# decorator is concept of adding additional features to existing function with out altering
def div(a, b):  # like as default function used more places as like
    print(a / b)


div(2, 4)


# if you want to swap of numerator and denominator you can add
def extra_div(funct):  # we are passing function
    def inner_funct(a, b):
        if a < b:
            a, b = b, a  # swapping in python
        return funct(a, b)  # swapped values
    return inner_funct


div1 = extra_div(div)  # we are passing function to new function

div1(2, 4)

div = extra_div(div)

div(2, 4)
