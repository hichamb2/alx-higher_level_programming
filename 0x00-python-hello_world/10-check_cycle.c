#include "lists.h"
/**
 * check_cycle - function
 * @list: the node
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *b;

	if (!list || !list->next)
		return (0);
	temp = list;
	b = temp->next;
	while (temp && b->next && b->next->next)
	{
		if (temp == b)
			return (1);
		temp = temp->next;
		b = b->next->next;
	}
	return (0);
}
