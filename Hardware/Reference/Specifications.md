# Modular Payload System Specifications
Revision: Draft

## Overview
These specifications are split into two categories, General Requirements that all module developers shall follow, and a following section that pertains only to modules that meet the High Reliability Requirements (HR)

## General Specifications
1. Performance

   1. Electrical connectors shall have continuous current carrying capacity derated to 80%.
   2. Ceramic capacitors shall be derated to 60% operating Voltage. Partial non compliance here is acceptable if the derating failure is only due to voltage rail tolerance. I.e.. a 10V capacitor is acceptable on a 5V rail.
   
   3. Polymer tantalum capacitors shall be derated to 80% operating Voltage
   4. Polymer tantalums shall be sourced from reputable manufacturers (KEMET, AVX, etc.) No other type of polarized capacitor should be used. (The goal here is to provide safe operation for the entire bus in hot environments and at high altitudes/low pressure. Deviation from this requirement is allowed, but should be done with caution)
   
   5. Tjmax for all ICs and components shall be derated to 80%
   6. All passive electrical components shall be AEC-Q200 qualified
   
   7. All discrete components shall be AEC-Q101 qualified
   8. All IC should be AEC-Q100 qualified. If the IC is not AEC-Q100 qualified, then it should have a pin compatible/orderable part that is AEC-Q100 qualified. (The goal here is that if the user wants to pay the extra or jump through the purchasing hurdles to actually get an AEC-Q100 part then they can, but it should be the same. For example the ATSAMC21 that is planned for this project has a AEC-Q100 qualified PN suffix, but they are non-stock. We would have to order a full reel. But by using this part, we have the option to simply order the AEC-Q100 part in the future if needed.)
   9. When digital communication and clocks greater than 25.575Mhz are used, the frequency should be chosen such that there are no odd harmonics in the L1 GPS band (1575.42 MHz ± 15.345 MHz). Digital frequencies keep out table included for reference below. For example, clock frequencies of 48MHz are not allow because they are between 47.275MHz and 48.205MHz and will produce a 33rd harmonic in the L1 GPS band. 48.25MHz, for example is allowed. If frequencies are used that are in the frequency keep out regions, shielding options should be evaluated in order to prevent interference with GPS receivers. If an applications uses GPS other than L1, a frequency keep out table should be made by dividing the the upper and lower bandwidth limits of the band by odd divisors.
   | Harmonic # | Lower (MHz) | Upper (MHz) |
   | :--------: | :---------: | :---------: |
   |     61     |   25.575    |   26.079    |
   |     59     |   26.441    |   26.963    |
   |     57     |   27.369    |   27.909    |
   |     55     |   28.365    |   28.923    |
   |     53     |   29.435    |   30.015    |
   |     51     |   30.589    |   31.192    |
   |     49     |   31.838    |   32.465    |
   |     47     |   33.193    |   33.847    |
   |     45     |   34.668    |   35.351    |
   |     43     |   36.280    |   36.995    |
   |     41     |   38.050    |   38.800    |
   |     39     |   40.001    |   40.789    |
   |     37     |   42.164    |   42.994    |
   |     35     |   44.573    |   45.451    |
   |     33     |   47.275    |   48.205    |
   |     31     |   50.325    |   51.315    |
   |     29     |   53.795    |   54.854    |
   |     27     |   57.780    |   58.918    |
   |     25     |   62.403    |   63.631    |
   |     23     |   67.829    |   69.164    |
   |     21     |   74.289    |   75.751    |
   |     19     |   82.109    |   83.725    |
   |     17     |   91.769    |   93.575    |
   |     15     |   104.005   |   106.051   |
   |     13     |   120.005   |   122.367   |
   |     11     |   141.825   |   144.615   |
   |     9      |   173.341   |   176.752   |
   |     7      |   222.867   |   227.253   |
   |     5      |   312.015   |   318.153   |
   |     3      |   520.025   |   530.255   |
   |     1      |  1560.075   |  1590.765   |

   10. Pinout
             1. TBD
   11. BUS Power
             1. +VBAT Rail
                1. +VBAT rail shall be 12.8VDC to 34VDC
                2. +VBAT rail steady state current shall be no more than 7.6A
                3. Total +VBAT rail transient current shall be < 1.5x max rated current of 7.6A =  11.4A (this includes inrush or any other transient loads, such as when radios are transmitting, etc.)
                4. All modules that generate the +VBAT rail via switching regulator topologies shall be 100% tested to ensure conformance to operating voltage requirement. This requirement does not apply to modules that generate the +VBAT rail only from a battery with no power path components that will significantly cause a drop (or increase) in rail voltage.
             2. +12V Rail
                      1. +12V rail shall be 11.2VDC to 12.6VDC
                      2. +12V rail steady state current shall be no more than 4A
                      3. Total +12V rail transient current shall be < 1.5x max rated current of 4A =  6A (this includes inrush or any other transient loads, such as when radios are transmitting, etc.)
                      4. All modules capable of generating the +12V rail shall be 100% tested to ensure conformance to operating voltage requirement 
             3. +5V Rail
                      1. +5V rail shall be 4.85V to 5.25V
                      2. +5V rail steady state current shall be no more than 3.2A
                      3. Total +5V rail transient current shall be < 1.5x max rated current of 3.2A =  4.8A (this includes inrush or any other transient loads, such as when radios are transmitting, etc.)
                      4. All modules capable of generating the +5V rail shall be 100% tested to ensure conformance to operating voltage requirement
             4. +VBAT_Preboot
                      1. TBD
             5. +5V_Preboot
                      1. TBD
             6. +5V_Bootstrap
                      1. TBD
      12. BUS Signals
                1. CAN0
                         1. TBD
                2. CAN1
                         1. TBD
                3. PPS
                         1. TBD
                4. CTRL_SYNC
                         1. TBD
                5. EN_0
                         1. TBD
                6. EN_1
                         1. TBD
                7. EN_2
                         1. TBD
                8. P_GOOD
                         1. **Intended Use** The P_GOOD signal is intended to be to power on reset signal for the bus. It can be used to enable local 3.3V LDOs or tied to the rest pin of a microcontroller. This allows the power supplies to come up, then assert the P_GOOD signal in order to enable the rest of the modules.
                         2. The P_GOOD signal shall be asserted to 3.3V (2.2V min. - 3.6V max.) after VBAT, 12V, and 5V rails have reached operating voltage
                         3. The P_GOOD signal shall be de-asserted if any of the rails fall below operating range after ~1ms of persistence
                         4. The P_GOOD net is driven through a 220ohm series resistor and a Schottky diode and has a 100kohm pulldown. The total amount of current sourced from this net shall be < 1.8 mA. The total amount of current per board sourced from P_GOOD should be < 150uA. (The goal of this requirement is to keep the P_GOOD rail from sagging excessively under load. The exception to this is reset buttons or other reset features. P_GOOD can be tied low which will draw ~10mA, which will hold the modules in reset)
   
   2. Mechanical

         1. Connectors
         2. Component Height
         3. Board Outline
         4. Mounting Holes
         5. Board thickness
         6. Test Points
               1. SMT test points should be at least 40mil in diameter
               2. SMT test points should be located on a 0.1” grid on the board. Per TBD drawing. (This allows for a standardized pogo pin test board that picks up on this grid. Save from having to create a pogo pin board for each module)
               3. SMT test points should be prioritized to be on top side of the board

## High Reliability Specifications

1. Performance
   1. Switching regulators shall have a gain margin of 10dB or greater and a phase margin of 35 degrees or greater
   2. Switching regulators shall have stability performance verified by Monte-Carlo Simulation over load and over component tolerance.
   3. Switching regulators shall have stability performance verified by test at nominal load.
   4. Linear regulators shall have a phase margin of 35 degrees or greater
   5. Linear regulators shall have stability performance verified by test at nominal load.
   6. All ICs and discrete electrical components shall be analyzed to ensure TJ MAX is not exceeded under max load.
