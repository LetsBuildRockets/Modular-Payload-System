/*
 * Code generated from Atmel Start.
 *
 * This file will be overwritten when reconfiguring your Atmel Start project.
 * Please copy examples or other code you want to keep to a separate file
 * to avoid losing it when reconfiguring.
 */

#include "driver_init.h"
#include <peripheral_clk_config.h>
#include <utils.h>
#include <hal_init.h>

#include <hpl_adc_base.h>

struct can_async_descriptor CAN_0;

struct adc_sync_descriptor ADC_0;

struct usart_sync_descriptor DEBUG_UART;

void ADC_0_PORT_init(void)
{

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA02, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA02, PINMUX_PA02B_ADC0_AIN0);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA04, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA04, PINMUX_PA04B_ADC0_AIN4);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA05, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA05, PINMUX_PA05B_ADC0_AIN5);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA06, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA06, PINMUX_PA06B_ADC0_AIN6);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA07, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA07, PINMUX_PA07B_ADC0_AIN7);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA08, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA08, PINMUX_PA08B_ADC0_AIN8);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA09, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA09, PINMUX_PA09B_ADC0_AIN9);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA10, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA10, PINMUX_PA10B_ADC0_AIN10);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA11, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA11, PINMUX_PA11B_ADC0_AIN11);

	// Disable digital pin circuitry
	gpio_set_pin_direction(PA03, GPIO_DIRECTION_OFF);

	gpio_set_pin_function(PA03, PINMUX_PA03B_ADC0_VREFP);
}

void ADC_0_CLOCK_init(void)
{
	hri_mclk_set_APBCMASK_ADC0_bit(MCLK);
	hri_gclk_write_PCHCTRL_reg(GCLK, ADC0_GCLK_ID, CONF_GCLK_ADC0_SRC | (1 << GCLK_PCHCTRL_CHEN_Pos));
}

void ADC_0_init(void)
{
	ADC_0_CLOCK_init();
	ADC_0_PORT_init();
	adc_sync_init(&ADC_0, ADC0, _adc_get_adc_sync());
}

void DEBUG_UART_PORT_init(void)
{

	gpio_set_pin_function(PA16, PINMUX_PA16D_SERCOM3_PAD0);

	gpio_set_pin_function(PA17, PINMUX_PA17D_SERCOM3_PAD1);
}

void DEBUG_UART_CLOCK_init(void)
{
	hri_gclk_write_PCHCTRL_reg(GCLK, SERCOM3_GCLK_ID_CORE, CONF_GCLK_SERCOM3_CORE_SRC | (1 << GCLK_PCHCTRL_CHEN_Pos));
	hri_gclk_write_PCHCTRL_reg(GCLK, SERCOM3_GCLK_ID_SLOW, CONF_GCLK_SERCOM3_SLOW_SRC | (1 << GCLK_PCHCTRL_CHEN_Pos));
	hri_mclk_set_APBCMASK_SERCOM3_bit(MCLK);
}

void DEBUG_UART_init(void)
{
	DEBUG_UART_CLOCK_init();
	usart_sync_init(&DEBUG_UART, SERCOM3, (void *)NULL);
	DEBUG_UART_PORT_init();
}

void CAN_0_PORT_init(void)
{

	gpio_set_pin_function(PB23, PINMUX_PB23G_CAN0_RX);

	gpio_set_pin_function(PB22, PINMUX_PB22G_CAN0_TX);
}
/**
 * \brief CAN initialization function
 *
 * Enables CAN peripheral, clocks and initializes CAN driver
 */
void CAN_0_init(void)
{
	hri_mclk_set_AHBMASK_CAN0_bit(MCLK);
	hri_gclk_write_PCHCTRL_reg(GCLK, CAN0_GCLK_ID, CONF_GCLK_CAN0_SRC | (1 << GCLK_PCHCTRL_CHEN_Pos));
	can_async_init(&CAN_0, CAN0);
	CAN_0_PORT_init();
}

void system_init(void)
{
	init_mcu();

	// GPIO on PA00

	// Set pin direction to input
	gpio_set_pin_direction(CTRL_SYNC, GPIO_DIRECTION_IN);

	gpio_set_pin_pull_mode(CTRL_SYNC,
	                       // <y> Pull configuration
	                       // <id> pad_pull_config
	                       // <GPIO_PULL_OFF"> Off
	                       // <GPIO_PULL_UP"> Pull-up
	                       // <GPIO_PULL_DOWN"> Pull-down
	                       GPIO_PULL_DOWN);

	gpio_set_pin_function(CTRL_SYNC, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA12

	// Set pin direction to input
	gpio_set_pin_direction(DETECT_A, GPIO_DIRECTION_IN);

	gpio_set_pin_pull_mode(DETECT_A,
	                       // <y> Pull configuration
	                       // <id> pad_pull_config
	                       // <GPIO_PULL_OFF"> Off
	                       // <GPIO_PULL_UP"> Pull-up
	                       // <GPIO_PULL_DOWN"> Pull-down
	                       GPIO_PULL_UP);

	gpio_set_pin_function(DETECT_A, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA13

	// Set pin direction to input
	gpio_set_pin_direction(DETECT_B, GPIO_DIRECTION_IN);

	gpio_set_pin_pull_mode(DETECT_B,
	                       // <y> Pull configuration
	                       // <id> pad_pull_config
	                       // <GPIO_PULL_OFF"> Off
	                       // <GPIO_PULL_UP"> Pull-up
	                       // <GPIO_PULL_DOWN"> Pull-down
	                       GPIO_PULL_UP);

	gpio_set_pin_function(DETECT_B, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA18

	// Set pin direction to input
	gpio_set_pin_direction(PG_5V_BT, GPIO_DIRECTION_IN);

	gpio_set_pin_pull_mode(PG_5V_BT,
	                       // <y> Pull configuration
	                       // <id> pad_pull_config
	                       // <GPIO_PULL_OFF"> Off
	                       // <GPIO_PULL_UP"> Pull-up
	                       // <GPIO_PULL_DOWN"> Pull-down
	                       GPIO_PULL_OFF);

	gpio_set_pin_function(PG_5V_BT, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA19

	// Set pin direction to input
	gpio_set_pin_direction(PG_5V, GPIO_DIRECTION_IN);

	gpio_set_pin_pull_mode(PG_5V,
	                       // <y> Pull configuration
	                       // <id> pad_pull_config
	                       // <GPIO_PULL_OFF"> Off
	                       // <GPIO_PULL_UP"> Pull-up
	                       // <GPIO_PULL_DOWN"> Pull-down
	                       GPIO_PULL_OFF);

	gpio_set_pin_function(PG_5V, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA20

	// Set pin direction to input
	gpio_set_pin_direction(PG_12V, GPIO_DIRECTION_IN);

	gpio_set_pin_pull_mode(PG_12V,
	                       // <y> Pull configuration
	                       // <id> pad_pull_config
	                       // <GPIO_PULL_OFF"> Off
	                       // <GPIO_PULL_UP"> Pull-up
	                       // <GPIO_PULL_DOWN"> Pull-down
	                       GPIO_PULL_OFF);

	gpio_set_pin_function(PG_12V, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA21

	gpio_set_pin_level(EN_12V,
	                   // <y> Initial level
	                   // <id> pad_initial_level
	                   // <false"> Low
	                   // <true"> High
	                   false);

	// Set pin direction to output
	gpio_set_pin_direction(EN_12V, GPIO_DIRECTION_OUT);

	gpio_set_pin_function(EN_12V, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA22

	gpio_set_pin_level(EN_5V_BT,
	                   // <y> Initial level
	                   // <id> pad_initial_level
	                   // <false"> Low
	                   // <true"> High
	                   true);

	// Set pin direction to output
	gpio_set_pin_direction(EN_5V_BT, GPIO_DIRECTION_OUT);

	gpio_set_pin_function(EN_5V_BT, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA23

	gpio_set_pin_level(EN_5V,
	                   // <y> Initial level
	                   // <id> pad_initial_level
	                   // <false"> Low
	                   // <true"> High
	                   false);

	// Set pin direction to output
	gpio_set_pin_direction(EN_5V, GPIO_DIRECTION_OUT);

	gpio_set_pin_function(EN_5V, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA27

	gpio_set_pin_level(P_GOODn,
	                   // <y> Initial level
	                   // <id> pad_initial_level
	                   // <false"> Low
	                   // <true"> High
	                   true);

	// Set pin direction to output
	gpio_set_pin_direction(P_GOODn, GPIO_DIRECTION_OUT);

	gpio_set_pin_function(P_GOODn, GPIO_PIN_FUNCTION_OFF);

	// GPIO on PA28

	gpio_set_pin_level(CAN0_STBY,
	                   // <y> Initial level
	                   // <id> pad_initial_level
	                   // <false"> Low
	                   // <true"> High
	                   true);

	// Set pin direction to output
	gpio_set_pin_direction(CAN0_STBY, GPIO_DIRECTION_OUT);

	gpio_set_pin_function(CAN0_STBY, GPIO_PIN_FUNCTION_OFF);

	ADC_0_init();

	DEBUG_UART_init();
	CAN_0_init();
}
