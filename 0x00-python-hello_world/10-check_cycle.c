#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the linked list
 *
 * Return: 1 if it has a cycle
 *         0 if it doesn't have a cycle
 * Author: Gamachu AD
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	int has_cycle = 0;

	while (temp->next != NULL)
	{
		if (temp->next == list)
		{
			has_cycle = 1;
			break;
		}
		temp = temp->next;
	}
	return (has_cycle);
}
