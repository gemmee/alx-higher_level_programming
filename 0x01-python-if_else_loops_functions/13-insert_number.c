#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to a pointer of the first node in the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node inserted.
 *         NULL if it failed.
 * Author: Gamachu AD
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	temp = *head;
	new = malloc(sizeof(*new));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (temp == NULL) /* edge case 1: list is empty */
	{
		temp = new;
		return (new);
	}
	if (new->n < temp->n) /* edge case 2: number is the smallest */
	{
		new->next = temp;
		temp = new;
		return (new);
	}
	if (temp->next == NULL && new->n > temp->n)
	{ /* edge case 3: there's only one element and number is larger */
		temp->next = new;
		return (new);
	}
	/* locate temp before the node to be inserted */
	while (new->n > temp->next->n)
	{
		temp = temp->next;
		if (temp->next == NULL) /*edge case 4: reached end of list*/
			break;
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}

