#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a double pointer to the head of the node
 * @number: the number to be inserted
 *
 * Return: the address of the new node inserted or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	/* special case for the head end */
	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		/* Locate the node before the point of insertion */
		while (current->next != NULL && current->next->n < new_node->n)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
