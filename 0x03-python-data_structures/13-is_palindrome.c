#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - function to check singly linked list for palindrome
* @head: pointer to the list head
* Return: 0 if not palindrome, else 1
*/

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *value = NULL;
	int x = -1, y = 0, num;

	if (current == NULL)
		return (1);
	value = malloc(sizeof(int) * 10);
	if (value == NULL)
	{
		free(value);
		return (0);
	}
	for (; current;)
	{
		x++;
		num = current->n;
		value[x] = num;
		current = current->next;
	}
	while (y <= x)
	{
		if (value[y] == value[x])
			y++, x--;
		else
			return (0);
	}

	free(value);
	return (1);
}
