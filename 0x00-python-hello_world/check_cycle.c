#include "lists.h"
/**
 *
 *
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;
	int i = 0;


	fast = list;
	slow = list;
	do{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
		i++;
	}while (fast != NULL);
	return (0);
}
