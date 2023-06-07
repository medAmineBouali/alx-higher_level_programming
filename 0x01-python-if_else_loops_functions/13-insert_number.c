#include "lists.h"
/**
 * insert_node - Insert node in order mode to linkedlist
 * @head: head
 * @number: num to be added
 * Return: the address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (!new)
		return (NULL);

	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next)
	{
		if ((current->next)->n >= number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}

	new->next = NULL;
	current->next = new;

	return (new);
}
