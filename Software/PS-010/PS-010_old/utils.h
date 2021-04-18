/*
 * utils.h
 *
 * Created: 3/7/2021 12:31:30 PM
 *  Author: erics
 */ 


#ifndef UTILS_H_
#define UTILS_H_

#define COUNTS_PER_MILLISECOND 12000

static inline void wait_millis_approx(unsigned long millis)
{
	for(int i =0; i < (millis*COUNTS_PER_MILLISECOND); i++);
}



#endif /* UTILS_H_ */