#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        pass
    if idx < 0 or idx >= i:
        return(my_list)
    my_list.remove(my_list[idx])
    return my_list
