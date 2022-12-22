#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it using
 * Floyd's cycle checking algorithm(also called tortoise and hare algorithm)
 * @list:  pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *rabbit;

	tortoise = list;
	rabbit = list;
	while (tortoise && rabbit && rabbit->next)
	{
		tortoise = tortoise->next;
		rabbit = rabbit->next->next;
		if (tortoise == rabbit)
		{
			return (1);
		}
	}
	return (0);
}
