#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	for column in matrix:
		count = len(column)
		for x in range(count):
			print('{}'.format(column[x]), end='')
			if x != count - 1:
				print(' ', end='')
		print('')
		return
