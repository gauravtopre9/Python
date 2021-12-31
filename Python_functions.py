tom = [2100,3400,3500]
joe = [200,500,700]

#FUNCTIONS

def calculate_total(exp): #This part is sfunction ARGUMENT
    total =0
    for items in exp:   #This part comes Under Function Body
        total = total+items
    return total #This is RETURN part of function
tom_total = calculate_total(tom)
print(tom_total)
joe_total = calculate_total(joe)
print(joe_total)

def two_num_sum(a,b=45): #this means if b is not assigned while calling function assume that b as 45
    """
    This function take which are integer number and return sum of them as a output
    :param a: input()
    :param b: 45
    :return:
    """
    total =0
    total = a +b
    return total
five_eleven = two_num_sum(5)
print(five_eleven)



#EXERCISE

#Q.no 1
def calculate_area(base,height):
    """
    Function calculate_area is taking input as base and height of triangle and wil be returning area of triangle
    :param base: base of triangle
    :param height: height of triangle
    :return: area of triangle
    """
    area = 0.5 * (base) * (height)
    return area

#answer_test
area1 = calculate_area(5,10)
print(area1)

#Q.no 2
def calculate_area_mod(base,height,shape= 'triangle'):
    area_temp = 0
    if shape == 'triangle':
        area_temp = 0.5 * base * height
        return area_temp
    elif shape == 'rectangle':
        area_temp = base * height
        return area_temp
    else:
        print('Shape is not listed for this function')


#Ans_test
area_mod_1 = calculate_area_mod(5,10,'rectangle')
print( area_mod_1)
area_mod_2 = calculate_area_mod(5,10,'triangle')
print(area_mod_2)
area_mod_3 = calculate_area_mod(5,10,'square')
print(area_mod_3)
area_mod_4 = calculate_area_mod(5,10)
print(area_mod_4)

#Q.no 3
def print_pattern(num):
    for i in range(num+1):
        print (i * '*')
    return none

#ANS_TEST
print_pat_1 = print_pattern(4)
print(print_pat_1)