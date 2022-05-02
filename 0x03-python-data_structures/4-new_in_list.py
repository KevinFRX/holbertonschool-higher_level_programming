#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    for i in new_list:
        pass
    if idx < 0 or idx >= i:
        return(new_list)
    new_list[idx] = element
    return(new_list)
