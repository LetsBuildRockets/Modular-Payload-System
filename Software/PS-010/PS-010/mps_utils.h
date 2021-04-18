/*
 * mps_utils.h
 *
 * Created: 3/7/2021 2:08:41 PM
 *  Author: erics
 */ 


#ifndef MPS_UTILS_H_
#define MPS_UTILS_H_

#define TICKS_PER_MILLISECOND 12000

static inline void WAIT_APPROX_MILLIS(unsigned long millis)
{
	for(int i =0; i < (millis * TICKS_PER_MILLISECOND); i++);
}

#endif /* MPS_UTILS_H_ */