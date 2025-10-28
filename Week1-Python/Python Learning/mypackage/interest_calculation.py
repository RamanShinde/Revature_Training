''' module for Interest Calculation'''


def simple_interest(prin,ny,roi): #roi->Rate of interest
    '''Return the interest value
    prin: principal interest value
    ny: number of years
    roi: area of interest
    '''
    si_values=prin*ny*roi/100
    amount_value=prin+si_values
    return si_values,amount_value


def compound_interest(prin, ny, roi, n):  # n -> number of times compounded per year
    '''Return the Amount value
    prin=principal interest value
    ny=number of years
    roi=area of interest
    '''
    amount_cpd = prin * (1 + (roi / (100 * n))) ** (n * ny)
    return amount_cpd

si,amount=(simple_interest(20,5,7))
compund_amount=compound_interest(50,20,5,7)

print(f"Simple Interest: {si},Amount: {amount}")
print(f"Compound Interest: {compund_amount}")
