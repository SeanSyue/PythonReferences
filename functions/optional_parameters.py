def opt_fun(x, *positional_parameters, **keyword_parameters):
    print("++++++++++")

    print(x)
    print(positional_parameters)
    print(keyword_parameters)

    if positional_parameters:
        print('a positional parameter detected.')
    else:
        print('no positional parameter, sorry')

    if 'optional' in keyword_parameters:
        print('optional parameter found, it is ', keyword_parameters['optional'])
    else:
        print('no optional parameter, sorry')


opt_fun(1)  # only pass in required argument
opt_fun(1, 2)  # pass in an additional position argument
opt_fun(1, 2, optional=3)  # pass in position argument and keyword argument
opt_fun(1, 2, fake=3)  # specify the keyword argument's keyword='optional'
