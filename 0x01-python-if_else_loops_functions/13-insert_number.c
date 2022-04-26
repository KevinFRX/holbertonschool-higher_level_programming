#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the list
 * @number: the number to inserts
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux, *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	node->n = number;
	aux = *head;

	if (!head || !*head)
	{
		node->next = NULL;
		*head = node;
		return (*head);
	}
	while (aux->next && number > aux->next->n)
		aux = aux->next;
	if (number < aux->n)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	node->next = aux->next;
	aux->next = node;
	return (node);
}
