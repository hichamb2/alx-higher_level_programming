#include "lists.h"
/**
 * check_cycle - function
 * @list: the node
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);
	slow = list;
	fast = slow->next;
	while (slow && fast->next && fast->next->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
