
def decimal_to_r_base(r: int, num: float):
    org = int(num)
    converted_int_portion = ""

    # integer portion conversion
    while int(org) != 0:
        converted_int_portion += str(org % r)
        org//=r

    # fraction portion conversion
    # getting the fraction protion

    frac = num % int(num)
    converted_frac_portion = ""

    for i in range(0, 6):
        converted_frac_portion += str(int(frac * r))
        if int(frac) != 0:
            frac = frac % int(frac)
        else: 
            frac = frac
    

    return float(converted_int_portion[::-1] + converted_frac_portion )

print(decimal_to_r_base(56, 8))

# def sub_rs_comp(r, n, m):
#     N = str(n)
#     M = str(m)

#     answer = ""
#     diff_in_length = len(N) - len(M)

#     if diff_in_length > 0:
#         M = ('0' * diff_in_length) + M
#         M_comp = ""
#         for i in range(0, len(N)):
#             M_comp += str(9 - int(M[i]))
        
#         print(M_comp)
        



# sub_rs_comp(10, 122333,  123)