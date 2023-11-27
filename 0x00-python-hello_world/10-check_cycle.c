#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * check_cycle - function to scan for cycles
 * @list: list pointer
 * Return:  0 if theres no cycle, else return 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
