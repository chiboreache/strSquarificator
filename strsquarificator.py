# %%
# i = 'input string'


def str_sqr(str_arg):

    str_list = list(str_arg.upper())
    tmp_list = list()

    for i in range(len(str_list)):
        pop_first = str_list[i:]
        get_poped = str_list[:i]
        shift_right = pop_first + get_poped
        shift_right = ' '.join(shift_right)
        tmp_list.append(shift_right)
    return tmp_list


# str_sqr(i)
