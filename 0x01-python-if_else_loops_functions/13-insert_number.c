#include "lists.h"

/**
 * insert_node - function
 * @head: head of the list
 * @number: number
 * Return: 0 or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *t = *head, *b;

	b = malloc(sizeof(listint_t));
	if (b == NULL)
		return (NULL);
	b->n = number;
	if (t == NULL || t->n >= number)
	{
		b->next = t;
		*head = b;
		return (b);
	}
	while (t && t->next && t->next->n < number)
		t = t->next;
	b->next = t->next;
	t->next = b;
	return (b);
}
