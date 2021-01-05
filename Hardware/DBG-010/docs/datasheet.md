# DBG-010 Debug/Development Board

## Overview
The DBG board is design to allow for basic debug functionality for Modular Payload System (MPS)  modules.

The board provides the following functionality:
- 4mm Banana jacks for powering the bus
- An ATSAMC21G17 microcontroller, with two CAN transceivers, for developing and testing code
- Enable lines broken out (EN_0, EN_1 and EN_2)
- Various jumpers to configure P_GOOD, EN_x, +5V_Bootstrap, and +5V_Preboot

## Specifications
### Operating Conditions
|               | Min. | Typ. | Max. | Unit |
| ------------- | ---- | ---- | ---- | ---- |
| +VBAT         | 12.8 | 22   | 34   | V    |
| +12V          | 11.2 | 12   | 12.6 | V    |
| +5V           | 4.75 | 5    | 5.25 | V    |
| +VBAT Current |      | 0.1  | 7.6  | A    |
| +12V Current  |      | 0.1  | 4    | A    |
| +5V Current   |      | 0.2  | 3.2  | A    |


## Configurations
### DBG-011
This configuration has all of the functionality of the board. It has the banana jacks for powering the bus, the enable lines,  P_GOOD, two CAN transceivers, and the ATSAMC21G17.
### DBG-012
Same as DBG-010 but with P1 and P2 installed
### DBG-013
This configuration only has the banana jacks for powering the bus, the enable lines, and P_GOOD. This configuration is designed for simply providing power to the bus
### DBG-014
This configuration only has the banana jacks and top and bottom bus connectors. This configuration is designed to breakout the power connections to measure or load the rails for testing

## Jumpers
- **P5** enables generation of the +5V_Preboot rail from the +5V rail. Jumper pins 1 and 2 to enable. Jumper pins 2 and 3 to disable.
- **P6** enables generation of the +5V_Bootstrap rail from the +5V rail.  Jumper pins 1 and 2 to enable. Jumper pins 2 and 3 to disable.
- **P7** selects the EN signal for the local +3.3V LDO. Jumper pins 1 and 2 to enable the local +3.3V LDO when P_GOOD is high. This matches the functionality of most of the modules. This requires a PSU module to be present. Jumper pins 2 and 3 to enable the +3.3V LDO. Remove the jumper to disable the +3.3V LDO.
- **P21** controls the P_GOOD signal. Jumper pins 1 and 2 to force P_GOOD high. This will enable the rest of the modules on the bus. (Note, this requires the +3.3V regulator to be enabled with P7).  Jumper pins 2 and 3 to allow PSU modules to control P_GOOD. 
- **P22** controls the DETECT_B signal. Jumper pins 1 and 2 to pull DETECT_B low and start the ident process. Jumper pins 2 and 3 to leave this functionality disabled.
- **P9** enables additional termination on CAN0. Install the jumper to enable additional termination, remove the jumper to disable. This allows for somewhat proper operation of the CAN0 bus without using a TOP module.
- **P11** enables additional termination on CAN1. Install the jumper to enable additional termination, remove the jumper to disable. This allows for somewhat proper operation of the CAN1 bus without using a TOP module.
- **P12** selects the EN_0 mode. Jumper pins 1 and 2 to force EN_0 high.  Jumper pins 2 and 3 to allow the external control of EN_0 from P18. (Note, both these modes require +5V_Preboot to be present. Either enable local generation using P5, or use a PSU module)
- **P13** selects the inversion of the EN_0 signal from P18. Jumper pins 1 and 2 to use the P18 EN_0 signal. Jumper pins 2 and 3 to invert the EN_0 signal from P18.
- **P14** selects the EN_1 mode. Jumper pins 1 and 2 to force EN_1 high.  Jumper pins 2 and 3 to allow the external control of EN_1 from P19. (Note, both these modes require +5V_Preboot to be present. Either enable local generation using P5, or use a PSU module)
- **P15** selects the inversion of the EN_1 signal from P19. Jumper pins 1 and 2 to use the P19 EN_1 signal. Jumper pins 2 and 3 to invert the EN_1 signal from P19.
- **P16** selects the EN_2 mode. Jumper pins 1 and 2 to force EN_2 high.  Jumper pins 2 and 3 to allow the external control of EN_2 from P20. (Note, both these modes require +5V_Preboot to be present. Either enable local generation using P5, or use a PSU module)
- **P17** selects the inversion of the EN_2 signal from P20. Jumper pins 1 and 2 to use the P20 EN_2 signal. Jumper pins 2 and 3 to invert the EN_2 signal from P20.