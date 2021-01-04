# CPU-010 Debug/Development Board

## Overview
.

## Specifications
### Operating Conditions
|               | Min. | Typ. | Max. | Unit |
| ------------- | ---- | ---- | ---- | ---- |
| +VBAT         | 12.8 | 22   | 34   | V    |
| +12V          | 11.2 | 12   | 12.6 | V    |
| +5V           | 4.75 | 5    | 5.25 | V    |
| +VBAT Current |      | - | - | A    |
| +12V Current  |      | - | -   | A    |
| +5V Current   |      | - | -  | A    |


## Configurations
### CPU-011

## Design Notes
### Power Consumption

|      Device       |          PN          |         Min.         | Typ.  | Max.  |
| :---------------: | :------------------: | :------------------: | :---: | :---: |
|        U1         |   ATSAMV71Q19B-AAB   |                      |       | 90mA  |
|        U3         |     ATA6561-GAQW     |        0.01mA        | 0.2mA | 0.5mA |
|        U4         |     ATA6561-GAQW     | 0mA (Not in Config.) | 0.2mA | 0.5mA |
|        U5         |  IS45S16800F-7TLA2   | 0mA (Not in Config.) | 80mA  | 120mA |
|        U8         |     KSZ8061RNBV      | 0mA (Not in Config.) |       |       |
|        X1         |                      |                      |       |       |
|        X2         | MC2016K25.0000C16ESH | 0mA (Not in Config.) |  1mA  |  5mA  |
| SD Card<br/>e.MMC |                      | 0mA (Not in Config.) | 100mA | 200mA |
|                   |                      |                      |       |       |
|       Total       |                      |                      |       |       |


