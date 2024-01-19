#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	print_listint(head);
	
	printf("----------------\n");
	/* Insert in NULL / empty list */
	insert_node(&head, -5);
	print_listint(head);

	printf("-----------------\n");

	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 2);
	add_nodeint_end(&head, 3);
	add_nodeint_end(&head, 4);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 402);
	add_nodeint_end(&head, 1024);
	print_listint(head);

	printf("-----------------\n");

	/* Insert node at middle */
	insert_node(&head, 27);
	/* Insert node at beginning */
	insert_node(&head, -7);
	/* Insert node at end */
	insert_node(&head, 5000);
    /* Insert duplicate value */
	insert_node(&head, 1);
	/* Insert multiple duplicate values */
	insert_node(&head, 98);
	insert_node(&head, 98);

	print_listint(head);

	free_listint(head);

	return (0);
}
