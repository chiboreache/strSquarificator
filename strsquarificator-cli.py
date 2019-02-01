#!/bin/python
# %%


def str_sqr(str_arg):

    str_list = list(str_arg.upper())
    tmp_list = list()

    for i in range(len(str_list)):
        pop_first = str_list[i:]
        get_poped = str_list[:i]
        shift_right = pop_first + get_poped
        shift_right = ' '.join(shift_right)
        tmp_list.append(shift_right)
        print(shift_right)
    return tmp_list


print('Waiting for input:\n')

i = input()
print('\n')

str_sqr(i)
print('\n')
