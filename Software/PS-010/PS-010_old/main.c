#include <atmel_start.h>
//#include "utils.h"
//#include "canard.h"


int main(void)
{
	/* Initializes MCU, drivers and middleware */
	atmel_start_init();
	
	printf("System Initialization Complete.\r\n");
	
	/* Replace with your application code */
	while (1) {
		for(int i = 0; i<2; i++) {
			printf("ex%i\r\n",i);
		}
		
		//wait_millis_approx(1000);
		printf("loop end\r\n");
		//wait_millis_approx(100);
	}
}
