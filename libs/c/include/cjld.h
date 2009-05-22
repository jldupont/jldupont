/**
 * @file   cjld.h
 *
 * @date   2009-05-22
 * @author Jean-Lou Dupont
 *
 * @mainpage Welcome to the documentation for the library <b>cjld</b> -- $version
 *
 *
 *
 */

#ifndef CJLD_H_
#define CJLD_H_

#include <errno.h>
#include <pthread.h>

	/**
	 * Single linked-list node
	 *
	 * @param node pointer to node
	 * @param next pointer to next node
	 */
	typedef struct _cjld_snode {

		void *node;
		struct _cjld_snode *next;

	} cjld_snode;

	/**
	 * Queue - thread-safe
	 *
	 * @param mutex: mutex
	 * @param cond:  the condition variable
	 * @param head:  pointer to ``head``
	 * @param tail:  pointer to ``tail``
	 */
	typedef struct {
		pthread_cond_t  *cond;
		pthread_mutex_t *cond_mutex;
		pthread_mutex_t *mutex;

		struct _cjld_snode *head, *tail;
		int num;
		int id;
		int total_in;
		int total_out;
	} cjld_queue;


	/******************************************************
	 * QUEUE related
	 *****************************************************/

	cjld_queue *cjld_queue_create(int id);

	void  cjld_queue_destroy(cjld_queue *queue);

	int   cjld_queue_put_nb(cjld_queue *q, void *msg);
	int   cjld_queue_put(cjld_queue *q, void *msg);
	int	  cjld_queue_put_wait(cjld_queue *q, void *node);

	int   cjld_queue_put_head_nb(cjld_queue *q, void *node);
	int   cjld_queue_put_head(cjld_queue *q, void *msg);
	int   cjld_queue_put_head_wait(cjld_queue *q, void *node);


	void *cjld_queue_get(cjld_queue *q);
	void *cjld_queue_get_nb(cjld_queue *q);
	int   cjld_queue_wait(cjld_queue *q);

	int   cjld_queue_peek(cjld_queue *q);
	void  cjld_queue_signal(cjld_queue *q);



#endif /* CJLD_H_ */
