#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks palindrome
 * @head: The head of list
 *
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *begin = NULL, *end = NULL;
	unsigned int i = 0, len = 0, len_cyc = 0, len_list = 0;

	if (head == NULL)
	return (0);
	if (*head == NULL)
		return (1);
	begin = *head;
	len = listint_len(begin);
	len_cyc = len * 2;
	len_list = len_cyc - 2;
	end = *head;
	for (; i < len_cyc; i = i + 2)
	{
		if (begin[i].n != end[len_list].n)
		return (0);
	len_list = len_list - 2;
	}
	return (1);
}

/**
 * get_nodeint_at_index - Gets a node
 * @head: The head list
 * @index: The index
 *
 * Return: node of list
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *temp = head;
	unsigned int iter = 0;

	if (head)
	{
		while (temp != NULL)
		{
			if (iter == index)
			return (temp);
		temp = temp->next;
		++iter;
		}
	}
	return (NULL);
}

/**
 * listint_len - Counts elements
 * @h: list count
 *
 * Return: Num of elemnts
 */
size_t listint_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
		++len;
		h = h->next;
	}
	return (len);
}

