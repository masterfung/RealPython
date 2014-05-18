base = raw_input('Enter a base: ')
exponent = raw_input('Enter an exponent: ')
result = int(base) ** int(exponent)
print int(base), ' to the power of ', int(exponent), ' = ', result
print '{} to the power of {} = {}'.format(base, exponent, result)