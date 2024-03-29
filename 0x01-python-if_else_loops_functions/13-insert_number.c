#include "lists.h"

/**
 * insert_node - function
 * @head: head of the list
 * @number: number
 * Return: 0 or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
