/*
 * Code generated from Atmel Start.
 *
 * This file will be overwritten when reconfiguring your Atmel Start project.
 * Please copy examples or other code you want to keep to a separate file
 * to avoid losing it when reconfiguring.
 */
#ifndef ATMEL_START_PINS_H_INCLUDED
#define ATMEL_START_PINS_H_INCLUDED

#include <hal_gpio.h>

// SAMC21 has 9 pin functions

#define GPIO_PIN_FUNCTION_A 0
#define GPIO_PIN_FUNCTION_B 1
#define GPIO_PIN_FUNCTION_C 2
#define GPIO_PIN_FUNCTION_D 3
#define GPIO_PIN_FUNCTION_E 4
#define GPIO_PIN_FUNCTION_F 5
#define GPIO_PIN_FUNCTION_G 6
#define GPIO_PIN_FUNCTION_H 7
#define GPIO_PIN_FUNCTION_I 8

#define CTRL_SYNC GPIO(GPIO_PORTA, 0)
#define PA02 GPIO(GPIO_PORTA, 2)
#define PA03 GPIO(GPIO_PORTA, 3)
#define PA04 GPIO(GPIO_PORTA, 4)
#define PA05 GPIO(GPIO_PORTA, 5)
#define PA06 GPIO(GPIO_PORTA, 6)
#define PA07 GPIO(GPIO_PORTA, 7)
#define PA08 GPIO(GPIO_PORTA, 8)
#define PA09 GPIO(GPIO_PORTA, 9)
#define PA10 GPIO(GPIO_PORTA, 10)
#define PA11 GPIO(GPIO_PORTA, 11)
#define DETECT_A GPIO(GPIO_PORTA, 12)
#define DETECT_B GPIO(GPIO_PORTA, 13)
#define PA16 GPIO(GPIO_PORTA, 16)
#define PA17 GPIO(GPIO_PORTA, 17)
#define PG_5V_BT GPIO(GPIO_PORTA, 18)
#define PG_5V GPIO(GPIO_PORTA, 19)
#define PG_12V GPIO(GPIO_PORTA, 20)
#define EN_12V GPIO(GPIO_PORTA, 21)
#define EN_5V_BT GPIO(GPIO_PORTA, 22)
#define EN_5V GPIO(GPIO_PORTA, 23)
#define P_GOODn GPIO(GPIO_PORTA, 27)
#define CAN0_STBY GPIO(GPIO_PORTA, 28)
#define PB22 GPIO(GPIO_PORTB, 22)
#define PB23 GPIO(GPIO_PORTB, 23)

#endif // ATMEL_START_PINS_H_INCLUDED
