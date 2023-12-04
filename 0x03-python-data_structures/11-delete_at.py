#!/usr/bin/python
def delete_at(my_list=[], idx=0):
	if idx < 0:
		return my_list
	count = len(my_list)
	if idx > count:
		return my_list
	del my_list[idx]

	return my_list
