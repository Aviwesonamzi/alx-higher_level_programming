#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the pointer of the first node in the list.
 * @number: Number to be inserted into the list.
 *
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    /* Set the data for the new node */
    new_node->n = number;
    new_node->next = NULL;

    /* Special case: inserting at the beginning or into an empty list */
    if (!*head || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Find the correct position to insert the new node */
    current = *head;
    while (current->next && current->next->n < number)
    {
        current = current->next;
    }

    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}
