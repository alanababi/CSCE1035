import math
def calc_hex_area(x):
	area= 3*math.sqrt(3)*(math.pow(x,2))
	print(f'Surface area of hexagonal faces is {area} square feet')
	return area
def calc_side_area(h,b):
    sa=6*b*h
    print(f'Surface area of rectangular sides is {sa} square feet')
    return sa
def display_surface_area(hex, side):
    print('The total surface area is {:.3f} square feet'.format(hex+side))

if __name__ == "__main__":
    height=float(input('Enter height of hexagonal prism in feet: '))
    base=float(input('Enter length of the base edge in feet  : '))
    hex=calc_hex_area(base)
    side=calc_side_area(height, base)
    display_surface_area(hex,side)