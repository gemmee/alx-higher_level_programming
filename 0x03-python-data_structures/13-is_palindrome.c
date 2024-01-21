#include "lists.h"

/**
 * reverse_list - reverses the linked list
 * @head: double pointer to the head
 *
 * Return: pointer to head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head of the linked list
 *
 * Return: 1 if it's a palindrome linked list
 *         0 if it's not a palindrome
 * Author: Gamachu AD
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *mid, *temp, *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /* empty list and one element list is palindrome */

	/*
	 * the logic I use is to find the middle of the list, reverse the second half
	 * and then compare the first half with the reversed second half
	 */
	slow = fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		if (fast == NULL) /* means even-length list */
			mid = slow; /* set mid just before slow */
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next; /* make slow point to the second half */
	}
	second_half = reverse_list(&slow);

	temp = *head;
	while (second_half != NULL)
	{
		if (temp->n != second_half->n)
			return (0);
		temp = temp->next;
		second_half = second_half->next;
	}
	mid->next = reverse_list(&slow);
	return (1);
}
