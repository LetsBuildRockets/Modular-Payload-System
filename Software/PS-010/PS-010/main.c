#include <atmel_start.h>
#include "hpl_adc_config.h"
#include "mps_utils.h"
//#include "canard.h"

#define adc_pres 1000000
#define ADC_REF_VOLTAGE 2.0480
#if CONF_ADC_0_RESSEL == 0x0
  #define ADC_RESOLUTION (1<<12)
#elif CONF_ADC_0_RESSEL == 0x1
  #define ADC_RESOLUTION (1<<16)
#elif CONF_ADC_0_RESSEL == 0x2
  #define ADC_RESOLUTION (1<<10)
#elif CONF_ADC_0_RESSEL == 0x3
  #define ADC_RESOLUTION (1<<8)
#else
  #error "CONF_ADC_0_RESSEL NOT DEFINED"
#endif

#define ADC_CH_VBAT_VMON		0x00	// PA02 - AIN0
#define ADC_CH_12V_INT_VMON		0x04	// PA04 - AIN4
#define ADC_CH_5V_BT_VMON		0x05	// PA05 - AIN5
#define ADC_CH_5V_VMON			0x06	// PA06 - AIN6
#define ADC_CH_5V_BT_INT_VMON	0x07	// PA07 - AIN7
#define ADC_CH_5V_INT_VMON		0x08	// PA08 - AIN8
#define ADC_CH_12V_VMON			0x09	// PA09 - AIN9
#define ADC_CH_5V_IMON			0x0A	// PA10 - AIN10
#define ADC_CH_12V_IMON			0x0B	// PA11 - AIN11

void print_adc_voltage(uint8_t channel, int numerator, int demoninator, char unit)
{
		uint8_t buffer[2];
		WAIT_APPROX_MILLIS(10);
		_adc_sync_set_inputs(&ADC_0, channel, 0x18, 0);
		adc_sync_enable_channel(&ADC_0, 0);
		adc_sync_read_channel(&ADC_0, 0, buffer, 2);
		//adc_sync_disable_channel(&ADC_0, channel);
		unsigned int val = (buffer[1]<<8)+(buffer[0]);
		unsigned int voltage_uV = val*(ADC_REF_VOLTAGE*adc_pres/ADC_RESOLUTION);
		unsigned int votlage_converted = voltage_uV*numerator/demoninator;
		printf("ADC CH %u: %u, %u, %u.%u %c\r\n", channel, val, voltage_uV, (unsigned int)(votlage_converted/adc_pres),(unsigned int)(votlage_converted/1000-(adc_pres/1000)*(votlage_converted/adc_pres)), unit);
}

int main(void)
{
	unsigned int loop_count = 0;
	/* Initializes MCU, drivers and middleware */
	atmel_start_init();
		
	printf("init done\r\n");
	printf("adc res: %i, %i\r\n",CONF_ADC_0_RESSEL,ADC_RESOLUTION);
	WAIT_APPROX_MILLIS(100);
	int32_t temp;
	temp_sync_enable(&TEMPERATURE_SENSOR_0);
	/* Replace with your application code */
	while (1) {
		if(loop_count>0) {
			gpio_set_pin_level(EN_5V, 1);
			gpio_set_pin_level(EN_12V, 1);
		}
		
		print_adc_voltage(ADC_CH_VBAT_VMON, 250, 10, 'V');
		print_adc_voltage(ADC_CH_5V_BT_INT_VMON, 56, 20, 'V');
		print_adc_voltage(ADC_CH_5V_BT_VMON, 56, 20, 'V');
		print_adc_voltage(ADC_CH_5V_INT_VMON, 56, 20, 'V');
		print_adc_voltage(ADC_CH_5V_VMON, 56, 20, 'V');
		print_adc_voltage(ADC_CH_5V_IMON, 2000, 1, 'm');
		print_adc_voltage(ADC_CH_12V_INT_VMON, 130, 20, 'V');
		print_adc_voltage(ADC_CH_12V_VMON, 130, 20, 'V');
		print_adc_voltage(ADC_CH_12V_IMON, 2000, 1, 'm');
		temp_sync_read(&TEMPERATURE_SENSOR_0, &temp);
		printf("temp: %ul\r\n", temp);
		
		WAIT_APPROX_MILLIS(1000);
		printf("end loop %u\r\n",loop_count);
		WAIT_APPROX_MILLIS(100);
		loop_count++;
	}
}
