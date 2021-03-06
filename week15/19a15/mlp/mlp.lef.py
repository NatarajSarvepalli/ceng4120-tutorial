#!/usr/bin/env python

BEGIN = '''
VERSION 5.8 ;
BUSBITCHARS "[]" ;
DIVIDERCHAR "/" ;

UNITS
  DATABASE MICRONS 2000 ;
END UNITS

PROPERTYDEFINITIONS
    LAYER LEF58_CORNERSPACING STRING ;
END PROPERTYDEFINITIONS

CLEARANCEMEASURE EUCLIDEAN ;
MANUFACTURINGGRID 0.0005 ;
USEMINSPACING OBS ON ;

LAYER Metal1
  TYPE ROUTING ;
  DIRECTION VERTICAL ;
  PITCH 0.10 0.10 ;
  WIDTH 0.05 ;
  MINWIDTH 0.05 ;
  AREA 0.0115 ;
  SPACINGTABLE
    PARALLELRUNLENGTH  0.0 0.22 0.47 0.63 1.50
    WIDTH 0.0         0.05 0.05 0.05 0.05 0.05
    WIDTH 0.10        0.05 0.06 0.06 0.06 0.06
    WIDTH 0.28        0.05 0.10 0.10 0.10 0.10
    WIDTH 0.47        0.05 0.10 0.13 0.13 0.13
    WIDTH 0.63        0.05 0.10 0.13 0.15 0.15
    WIDTH 1.50        0.05 0.10 0.13 0.15 0.50 ;
  SPACING 0.06 ENDOFLINE 0.06 WITHIN 0.025 ;
END Metal1

LAYER Via1
  TYPE CUT ;
  SPACING 0.075 ;
  WIDTH 0.05 ;
END Via1

LAYER Metal2
  TYPE ROUTING ;
  DIRECTION HORIZONTAL ;
  PITCH 0.10 0.10 ;
  WIDTH 0.05 ;
  MINWIDTH 0.05 ;
  AREA 0.014 ;
  SPACINGTABLE
    PARALLELRUNLENGTH  0.0 0.22 0.47 0.63 1.5
    WIDTH 0.0         0.05 0.05 0.05 0.05 0.05
    WIDTH 0.09        0.05 0.06 0.06 0.06 0.06
    WIDTH 0.16        0.05 0.10 0.10 0.10 0.10
    WIDTH 0.47        0.05 0.10 0.13 0.13 0.13
    WIDTH 0.63        0.05 0.10 0.13 0.15 0.15
    WIDTH 1.5         0.05 0.10 0.13 0.15 0.50 ;
  SPACING 0.08 ENDOFLINE 0.08 WITHIN 0.025 ;
  SPACING 0.10 ENDOFLINE 0.08 WITHIN 0.025 PARALLELEDGE 0.10 WITHIN 0.025 ;
  PROPERTY LEF58_CORNERSPACING "CORNERSPACING CONVEXCORNER EXCEPTEOL 0.08
    WIDTH 0.00 SPACING 0.10
    WIDTH 0.20 SPACING 0.20
    WIDTH 0.50 SPACING 0.30 ;" ;
END Metal2

LAYER Via2
  TYPE CUT ;
  SPACING 0.075 ;
  WIDTH 0.05 ;
  SPACING 0.155 ADJACENTCUTS 3 WITHIN 0.200 ;
END Via2

LAYER Metal3
  TYPE ROUTING ;
  DIRECTION VERTICAL ;
  PITCH 0.10 0.10 ;
  WIDTH 0.05 ;
  MINWIDTH 0.05 ;
  AREA 0.017 ;
  SPACINGTABLE
    PARALLELRUNLENGTH  0.0 0.22 0.47 0.63 1.5
    WIDTH 0.0         0.05 0.05 0.05 0.05 0.05
    WIDTH 0.09        0.05 0.06 0.06 0.06 0.06
    WIDTH 0.16        0.05 0.10 0.10 0.10 0.10
    WIDTH 0.47        0.05 0.10 0.13 0.13 0.13
    WIDTH 0.63        0.05 0.10 0.13 0.15 0.15
    WIDTH 1.5         0.05 0.10 0.13 0.15 0.50 ;
  SPACING 0.08 ENDOFLINE 0.08 WITHIN 0.025 ;
  SPACING 0.10 ENDOFLINE 0.08 WITHIN 0.025 PARALLELEDGE 0.10 WITHIN 0.025 ;
  PROPERTY LEF58_CORNERSPACING "CORNERSPACING CONVEXCORNER EXCEPTEOL 0.08
    WIDTH 0.00 SPACING 0.10
    WIDTH 0.20 SPACING 0.20
    WIDTH 0.50 SPACING 0.30 ;" ;
END Metal3

LAYER Via3
  TYPE CUT ;
  SPACING 0.075 ;
  WIDTH 0.05 ;
  SPACING 0.155 ADJACENTCUTS 3 WITHIN 0.200 ;
END Via3

LAYER Metal4
  TYPE ROUTING ;
  DIRECTION HORIZONTAL ;
  PITCH 0.10 0.10 ;
  WIDTH 0.05 ;
  MINWIDTH 0.05 ;
  AREA 0.017 ;
  SPACINGTABLE
    PARALLELRUNLENGTH  0.0 0.22 0.47 0.63 1.5
    WIDTH 0.0         0.05 0.05 0.05 0.05 0.05
    WIDTH 0.09        0.05 0.06 0.06 0.06 0.06
    WIDTH 0.16        0.05 0.10 0.10 0.10 0.10
    WIDTH 0.47        0.05 0.10 0.13 0.13 0.13
    WIDTH 0.63        0.05 0.10 0.13 0.15 0.15
    WIDTH 1.5         0.05 0.10 0.13 0.15 0.50 ;
  SPACING 0.08 ENDOFLINE 0.08 WITHIN 0.025 ;
  SPACING 0.10 ENDOFLINE 0.08 WITHIN 0.025 PARALLELEDGE 0.10 WITHIN 0.025 ;
  PROPERTY LEF58_CORNERSPACING "CORNERSPACING CONVEXCORNER EXCEPTEOL 0.08
    WIDTH 0.00 SPACING 0.10
    WIDTH 0.20 SPACING 0.20
    WIDTH 0.50 SPACING 0.30 ;" ;
END Metal4

LAYER Via4
  TYPE CUT ;
  SPACING 0.075 ;
  WIDTH 0.05 ;
  SPACING 0.155 ADJACENTCUTS 3 WITHIN 0.200 ;
END Via4

LAYER Metal5
  TYPE ROUTING ;
  DIRECTION VERTICAL ;
  PITCH 0.10 0.10 ;
  WIDTH 0.05 ;
  MINWIDTH 0.05 ;
  AREA 0.017 ;
  SPACINGTABLE
    PARALLELRUNLENGTH  0.0 0.22 0.47 0.63 1.5
    WIDTH 0.0         0.05 0.05 0.05 0.05 0.05
    WIDTH 0.09        0.05 0.06 0.06 0.06 0.06
    WIDTH 0.16        0.05 0.10 0.10 0.10 0.10
    WIDTH 0.47        0.05 0.10 0.13 0.13 0.13
    WIDTH 0.63        0.05 0.10 0.13 0.15 0.15
    WIDTH 1.5         0.05 0.10 0.13 0.15 0.50 ;
  SPACING 0.08 ENDOFLINE 0.08 WITHIN 0.025 ;
  SPACING 0.10 ENDOFLINE 0.08 WITHIN 0.025 PARALLELEDGE 0.10 WITHIN 0.025 ;
  PROPERTY LEF58_CORNERSPACING "CORNERSPACING CONVEXCORNER EXCEPTEOL 0.08
    WIDTH 0.00 SPACING 0.10
    WIDTH 0.20 SPACING 0.20
    WIDTH 0.50 SPACING 0.30 ;" ;
END Metal5

LAYER Via5
  TYPE CUT ;
  SPACING 0.075 ;
  WIDTH 0.05 ;
  SPACING 0.155 ADJACENTCUTS 3 WITHIN 0.200 ;
END Via5

LAYER Metal6
  TYPE ROUTING ;
  DIRECTION HORIZONTAL ;
  PITCH 0.15 0.15 ;
  WIDTH 0.07 ;
  MINWIDTH 0.07 ;
  AREA 0.025 ;
  SPACINGTABLE
    PARALLELRUNLENGTH  0.0 0.22 0.47 0.63 1.5
    WIDTH 0.0         0.08 0.08 0.08 0.08 0.08
    WIDTH 0.10        0.08 0.12 0.12 0.12 0.12
    WIDTH 0.16        0.08 0.12 0.15 0.15 0.15
    WIDTH 0.47        0.08 0.12 0.15 0.18 0.18
    WIDTH 0.63        0.08 0.12 0.15 0.18 0.25
    WIDTH 1.5         0.08 0.12 0.15 0.18 0.50 ;
  SPACING 0.10 ENDOFLINE 0.10 WITHIN 0.035 ;
  SPACING 0.12 ENDOFLINE 0.10 WITHIN 0.035 PARALLELEDGE 0.12 WITHIN 0.035 ;
  PROPERTY LEF58_CORNERSPACING "CORNERSPACING CONVEXCORNER EXCEPTEOL 0.08
    WIDTH 0.00 SPACING 0.10
    WIDTH 0.20 SPACING 0.20
    WIDTH 0.50 SPACING 0.30 ;" ;
END Metal6

LAYER Via6
  TYPE CUT ;
  SPACING 0.10 ;
  WIDTH 0.07 ;
  SPACING 0.20 ADJACENTCUTS 3 WITHIN 0.25 ;
END Via6

LAYER Metal7
  TYPE ROUTING ;
  DIRECTION VERTICAL ;
  PITCH 0.15 0.15 ;
  WIDTH 0.07 ;
  MINWIDTH 0.07 ;
  AREA 0.025 ;
  SPACINGTABLE
    PARALLELRUNLENGTH  0.0 0.22 0.47 0.63 1.5
    WIDTH 0.0         0.08 0.08 0.08 0.08 0.08
    WIDTH 0.10        0.08 0.12 0.12 0.12 0.12
    WIDTH 0.16        0.08 0.12 0.15 0.15 0.15
    WIDTH 0.47        0.08 0.12 0.15 0.18 0.18
    WIDTH 0.63        0.08 0.12 0.15 0.18 0.25
    WIDTH 1.5         0.08 0.12 0.15 0.18 0.50 ;
  SPACING 0.10 ENDOFLINE 0.10 WITHIN 0.035 ;
  SPACING 0.12 ENDOFLINE 0.10 WITHIN 0.035 PARALLELEDGE 0.12 WITHIN 0.035 ;
  PROPERTY LEF58_CORNERSPACING "CORNERSPACING CONVEXCORNER EXCEPTEOL 0.08
    WIDTH 0.00 SPACING 0.10
    WIDTH 0.20 SPACING 0.20
    WIDTH 0.50 SPACING 0.30 ;" ;
END Metal7

LAYER Via7
  TYPE CUT ;
  SPACING 0.10 ;
  WIDTH 0.07 ;
  SPACING 0.20 ADJACENTCUTS 3 WITHIN 0.25 ;
END Via7

LAYER Metal8
  TYPE ROUTING ;
  DIRECTION HORIZONTAL ;
  PITCH 0.2 0.2 ;
  WIDTH 0.10 ;
  MINWIDTH 0.10 ;
  AREA 0.052 ;
  SPACINGTABLE
    PARALLELRUNLENGTH 0.0 0.22 0.47 0.63 1.5
    WIDTH 0	     0.10 0.10 0.10 0.10 0.10
    WIDTH 0.2	     0.10 0.15 0.15 0.15 0.15
    WIDTH 0.4	     0.10 0.15 0.20 0.20 0.20
    WIDTH 1.5	     0.10 0.15 0.20 0.30 0.50 ;
  SPACING 0.12 ENDOFLINE 0.12 WITHIN 0.035 ;
END Metal8

LAYER Via8
  TYPE CUT ;
  SPACING 0.15 ;
  WIDTH 0.10 ;
END Via8

LAYER Metal9
  TYPE ROUTING ;
  DIRECTION VERTICAL ;
  PITCH 0.2 0.2 ;
  WIDTH 0.10 ;
  MINWIDTH 0.10 ;
  AREA 0.052 ;
  SPACINGTABLE
    PARALLELRUNLENGTH 0.0 0.22 0.47 0.63 1.5
    WIDTH 0	     0.10 0.10 0.10 0.10 0.10
    WIDTH 0.2	     0.10 0.15 0.15 0.15 0.15
    WIDTH 0.4	     0.10 0.15 0.20 0.20 0.20
    WIDTH 1.5	     0.10 0.15 0.20 0.30 0.50 ;
  SPACING 0.12 ENDOFLINE 0.12 WITHIN 0.035 ;
END Metal9

LAYER OVERLAP
  TYPE OVERLAP ;
END OVERLAP

VIA VIA12_1C DEFAULT
    LAYER Metal1 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
    LAYER Via1 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal2 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
END VIA12_1C

VIA VIA12_1C_H DEFAULT
    LAYER Metal1 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
    LAYER Via1 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal2 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
END VIA12_1C_H

VIA VIA12_1C_V DEFAULT
    LAYER Metal1 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
    LAYER Via1 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal2 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
END VIA12_1C_V

VIA VIA12_PG
    LAYER Metal1 ;
        RECT -0.350000 -0.050000 0.350000 0.050000 ;
    LAYER Via1 ;
        RECT -0.325000 -0.025000 -0.275000 0.025000 ;
        RECT -0.175000 -0.025000 -0.125000 0.025000 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
        RECT 0.125000 -0.025000 0.175000 0.025000 ;
        RECT 0.275000 -0.025000 0.325000 0.025000 ;
    LAYER Metal2 ;
        RECT -0.350000 -0.050000 0.350000 0.050000 ;
END VIA12_PG

VIA VIA23_1C DEFAULT
    LAYER Metal2 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
    LAYER Via2 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal3 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
END VIA23_1C

VIA VIA23_1C_H DEFAULT
    LAYER Metal2 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
    LAYER Via2 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal3 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
END VIA23_1C_H

VIA VIA23_1C_V DEFAULT
    LAYER Metal2 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
    LAYER Via2 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal3 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
END VIA23_1C_V

VIA VIA23_1ST_E DEFAULT
    LAYER Metal2 ;
        RECT -0.055000 -0.025000 0.325000 0.025000 ;
    LAYER Via2 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal3 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
END VIA23_1ST_E

VIA VIA23_1ST_W DEFAULT
    LAYER Metal2 ;
        RECT -0.325000 -0.025000 0.055000 0.025000 ;
    LAYER Via2 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal3 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
END VIA23_1ST_W

VIA VIA23_PG
    LAYER Metal2 ;
        RECT -0.350000 -0.050000 0.350000 0.050000 ;
    LAYER Via2 ;
        RECT -0.325000 -0.025000 -0.275000 0.025000 ;
        RECT -0.175000 -0.025000 -0.125000 0.025000 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
        RECT 0.125000 -0.025000 0.175000 0.025000 ;
        RECT 0.275000 -0.025000 0.325000 0.025000 ;
    LAYER Metal3 ;
        RECT -0.350000 -0.050000 0.350000 0.050000 ;
END VIA23_PG

VIA VIA34_1C DEFAULT
    LAYER Metal3 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
    LAYER Via3 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal4 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
END VIA34_1C

VIA VIA34_1C_H DEFAULT
    LAYER Metal3 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
    LAYER Via3 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal4 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
END VIA34_1C_H

VIA VIA34_1C_V DEFAULT
    LAYER Metal3 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
    LAYER Via3 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal4 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
END VIA34_1C_V

VIA VIA34_1ST_N DEFAULT
    LAYER Metal3 ;
        RECT -0.025000 -0.055000 0.025000 0.325000 ;
    LAYER Via3 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal4 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
END VIA34_1ST_N

VIA VIA34_1ST_S DEFAULT
    LAYER Metal3 ;
        RECT -0.025000 -0.325000 0.025000 0.055000 ;
    LAYER Via3 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal4 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
END VIA34_1ST_S

VIA VIA34_PG
    LAYER Metal3 ;
        RECT -0.350000 -0.050000 0.350000 0.050000 ;
    LAYER Via3 ;
        RECT -0.325000 -0.025000 -0.275000 0.025000 ;
        RECT -0.175000 -0.025000 -0.125000 0.025000 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
        RECT 0.125000 -0.025000 0.175000 0.025000 ;
        RECT 0.275000 -0.025000 0.325000 0.025000 ;
    LAYER Metal4 ;
        RECT -0.350000 -0.050000 0.350000 0.050000 ;
END VIA34_PG

VIA VIA45_1C DEFAULT
    LAYER Metal4 ;
        RECT -0.055000 -0.025000 0.055000 0.025000 ;
    LAYER Via4 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal5 ;
        RECT -0.025000 -0.055000 0.025000 0.055000 ;
END VIA45_1C

VIA VIA45_PG
    LAYER Metal4 ;
        RECT -0.200000 -0.050000 0.200000 0.050000 ;
    LAYER Via4 ;
        RECT -0.175000 -0.025000 -0.125000 0.025000 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
        RECT 0.125000 -0.025000 0.175000 0.025000 ;
    LAYER Metal5 ;
        RECT -0.200000 -0.050000 0.200000 0.050000 ;
END VIA45_PG

VIA VIA5_0_VH DEFAULT
    LAYER Metal5 ;
        RECT -0.035000 -0.065000 0.035000 0.065000 ;
    LAYER Via5 ;
        RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal6 ;
        RECT -0.065000 -0.035000 0.065000 0.035000 ;
END VIA5_0_VH

VIA VIA56_PG
    LAYER Metal5 ;
        RECT -0.150000 -0.150000 0.150000 0.150000 ;
    LAYER Via5 ;
        RECT -0.150000 -0.150000 -0.100000 -0.100000 ;
        RECT -0.150000 0.100000 -0.100000 0.150000 ;
        RECT 0.100000 0.100000 0.150000 0.150000 ;
        RECT 0.100000 -0.150000 0.150000 -0.100000 ;
    LAYER Metal6 ;
        RECT -0.150000 -0.150000 0.150000 0.150000 ;
END VIA56_PG

VIA VIA6_0_HV DEFAULT
    LAYER Metal6 ;
        RECT -0.065000 -0.035000 0.065000 0.035000 ;
    LAYER Via6 ;
        RECT -0.035000 -0.035000 0.035000 0.035000 ;
    LAYER Metal7 ;
        RECT -0.035000 -0.065000 0.035000 0.065000 ;
END VIA6_0_HV

VIA VIA67_PG
    LAYER Metal6 ;
        RECT -0.170000 -0.170000 0.170000 0.170000 ;
    LAYER Via6 ;
        RECT -0.170000 -0.170000 -0.100000 -0.100000 ;
        RECT -0.170000 0.100000 -0.100000 0.170000 ;
        RECT 0.100000 0.100000 0.170000 0.170000 ;
        RECT 0.100000 -0.170000 0.170000 -0.100000 ;
    LAYER Metal7 ;
        RECT -0.170000 -0.170000 0.170000 0.170000 ;
END VIA67_PG

VIA VIA7_0_VH DEFAULT
    LAYER Metal7 ;
        RECT -0.050000 -0.260000 0.050000 0.260000 ;
    LAYER Via7 ;
        RECT -0.050000 -0.050000 0.050000 0.050000 ;
    LAYER Metal8 ;
        RECT -0.260000 -0.050000 0.260000 0.050000 ;
END VIA7_0_VH

VIA VIA78_PG
    LAYER Metal7 ;
        RECT -0.170000 -0.170000 0.170000 0.170000 ;
    LAYER Via7 ;
        RECT -0.170000 -0.170000 -0.100000 -0.100000 ;
        RECT -0.170000 0.100000 -0.100000 0.170000 ;
        RECT 0.100000 0.100000 0.170000 0.170000 ;
        RECT 0.100000 -0.170000 0.170000 -0.100000 ;
    LAYER Metal8 ;
        RECT -0.170000 -0.170000 0.170000 0.170000 ;
END VIA78_PG

VIA VIA8_0_HV DEFAULT
    LAYER Metal8 ;
        RECT -0.260000 -0.050000 0.260000 0.050000 ;
    LAYER Via8 ;
        RECT -0.050000 -0.050000 0.050000 0.050000 ;
    LAYER Metal9 ;
        RECT -0.050000 -0.260000 0.050000 0.260000 ;
END VIA8_0_HV

VIA VIA12_2C_W DEFAULT
    LAYER Metal1 ;
	RECT -0.150000 -0.055000 0.025000 0.055000 ;
    LAYER Via1 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.150000 -0.025000 -0.100000 0.025000 ;
    LAYER Metal2 ;
	RECT -0.180000 -0.025000 0.055000 0.025000 ;
END VIA12_2C_W

VIA VIA12_2C_CH DEFAULT
    LAYER Metal1 ;
	RECT -0.087500 -0.055000 0.087500 0.055000 ;
    LAYER Via1 ;
	RECT 0.037500 -0.025000 0.087500 0.025000 ;
	RECT -0.087500 -0.025000 -0.037500 0.025000 ;
    LAYER Metal2 ;
	RECT -0.117500 -0.025000 0.117500 0.025000 ;
END VIA12_2C_CH

VIA VIA12_2C_E DEFAULT
    LAYER Metal1 ;
	RECT -0.025000 -0.055000 0.150000 0.055000 ;
    LAYER Via1 ;
	RECT 0.100000 -0.025000 0.150000 0.025000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal2 ;
	RECT -0.055000 -0.025000 0.180000 0.025000 ;
END VIA12_2C_E

VIA VIA12_2C_S DEFAULT
    LAYER Metal1 ;
	RECT -0.025000 -0.180000 0.025000 0.055000 ;
    LAYER Via1 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.025000 -0.150000 0.025000 -0.100000 ;
    LAYER Metal2 ;
	RECT -0.055000 -0.150000 0.055000 0.025000 ;
END VIA12_2C_S

VIA VIA12_2C_CV DEFAULT
    LAYER Metal1 ;
	RECT -0.025000 -0.117500 0.025000 0.117500 ;
    LAYER Via1 ;
	RECT -0.025000 0.037500 0.025000 0.087500 ;
	RECT -0.025000 -0.087500 0.025000 -0.037500 ;
    LAYER Metal2 ;
	RECT -0.055000 -0.087500 0.055000 0.087500 ;
END VIA12_2C_CV

VIA VIA12_2C_N DEFAULT
    LAYER Metal1 ;
	RECT -0.025000 -0.055000 0.025000 0.180000 ;
    LAYER Via1 ;
	RECT -0.025000 0.100000 0.025000 0.150000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal2 ;
	RECT -0.055000 -0.025000 0.055000 0.150000 ;
END VIA12_2C_N

VIA VIA23_2C_W DEFAULT
    LAYER Metal2 ;
	RECT -0.180000 -0.025000 0.055000 0.025000 ;
    LAYER Via2 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.150000 -0.025000 -0.100000 0.025000 ;
    LAYER Metal3 ;
	RECT -0.150000 -0.055000 0.025000 0.055000 ;
END VIA23_2C_W

VIA VIA23_2C_CH DEFAULT
    LAYER Metal2 ;
	RECT -0.117500 -0.025000 0.117500 0.025000 ;
    LAYER Via2 ;
	RECT 0.037500 -0.025000 0.087500 0.025000 ;
	RECT -0.087500 -0.025000 -0.037500 0.025000 ;
    LAYER Metal3 ;
	RECT -0.087500 -0.055000 0.087500 0.055000 ;
END VIA23_2C_CH

VIA VIA23_2C_E DEFAULT
    LAYER Metal2 ;
	RECT -0.055000 -0.025000 0.180000 0.025000 ;
    LAYER Via2 ;
	RECT 0.100000 -0.025000 0.150000 0.025000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal3 ;
	RECT -0.025000 -0.055000 0.150000 0.055000 ;
END VIA23_2C_E

VIA VIA23_2C_S DEFAULT
    LAYER Metal2 ;
	RECT -0.055000 -0.150000 0.055000 0.025000 ;
    LAYER Via2 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.025000 -0.150000 0.025000 -0.100000 ;
    LAYER Metal3 ;
	RECT -0.025000 -0.180000 0.025000 0.055000 ;
END VIA23_2C_S

VIA VIA23_2C_CV DEFAULT
    LAYER Metal2 ;
	RECT -0.055000 -0.087500 0.055000 0.087500 ;
    LAYER Via2 ;
	RECT -0.025000 0.037500 0.025000 0.087500 ;
	RECT -0.025000 -0.087500 0.025000 -0.037500 ;
    LAYER Metal3 ;
	RECT -0.025000 -0.117500 0.025000 0.117500 ;
END VIA23_2C_CV

VIA VIA23_2C_N DEFAULT
    LAYER Metal2 ;
	RECT -0.055000 -0.025000 0.055000 0.150000 ;
    LAYER Via2 ;
	RECT -0.025000 0.100000 0.025000 0.150000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal3 ;
	RECT -0.025000 -0.055000 0.025000 0.180000 ;
END VIA23_2C_N

VIA VIA34_2C_W DEFAULT
    LAYER Metal3 ;
	RECT -0.150000 -0.055000 0.025000 0.055000 ;
    LAYER Via3 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.150000 -0.025000 -0.100000 0.025000 ;
    LAYER Metal4 ;
	RECT -0.180000 -0.025000 0.055000 0.025000 ;
END VIA34_2C_W

VIA VIA34_2C_CH DEFAULT
    LAYER Metal3 ;
	RECT -0.087500 -0.055000 0.087500 0.055000 ;
    LAYER Via3 ;
	RECT 0.037500 -0.025000 0.087500 0.025000 ;
	RECT -0.087500 -0.025000 -0.037500 0.025000 ;
    LAYER Metal4 ;
	RECT -0.117500 -0.025000 0.117500 0.025000 ;
END VIA34_2C_CH

VIA VIA34_2C_E DEFAULT
    LAYER Metal3 ;
	RECT -0.025000 -0.055000 0.150000 0.055000 ;
    LAYER Via3 ;
	RECT 0.100000 -0.025000 0.150000 0.025000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal4 ;
	RECT -0.055000 -0.025000 0.180000 0.025000 ;
END VIA34_2C_E

VIA VIA34_2C_S DEFAULT
    LAYER Metal3 ;
	RECT -0.025000 -0.180000 0.025000 0.055000 ;
    LAYER Via3 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.025000 -0.150000 0.025000 -0.100000 ;
    LAYER Metal4 ;
	RECT -0.055000 -0.150000 0.055000 0.025000 ;
END VIA34_2C_S

VIA VIA34_2C_CV DEFAULT
    LAYER Metal3 ;
	RECT -0.025000 -0.117500 0.025000 0.117500 ;
    LAYER Via3 ;
	RECT -0.025000 0.037500 0.025000 0.087500 ;
	RECT -0.025000 -0.087500 0.025000 -0.037500 ;
    LAYER Metal4 ;
	RECT -0.055000 -0.087500 0.055000 0.087500 ;
END VIA34_2C_CV

VIA VIA34_2C_N DEFAULT
    LAYER Metal3 ;
	RECT -0.025000 -0.055000 0.025000 0.180000 ;
    LAYER Via3 ;
	RECT -0.025000 0.100000 0.025000 0.150000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal4 ;
	RECT -0.055000 -0.025000 0.055000 0.150000 ;
END VIA34_2C_N

VIA VIA45_2C_W DEFAULT
    LAYER Metal4 ;
	RECT -0.180000 -0.025000 0.055000 0.025000 ;
    LAYER Via4 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.150000 -0.025000 -0.100000 0.025000 ;
    LAYER Metal5 ;
	RECT -0.150000 -0.055000 0.025000 0.055000 ;
END VIA45_2C_W

VIA VIA45_2C_CH DEFAULT
    LAYER Metal4 ;
	RECT -0.117500 -0.025000 0.117500 0.025000 ;
    LAYER Via4 ;
	RECT 0.037500 -0.025000 0.087500 0.025000 ;
	RECT -0.087500 -0.025000 -0.037500 0.025000 ;
    LAYER Metal5 ;
	RECT -0.087500 -0.055000 0.087500 0.055000 ;
END VIA45_2C_CH

VIA VIA45_2C_E DEFAULT
    LAYER Metal4 ;
	RECT -0.055000 -0.025000 0.180000 0.025000 ;
    LAYER Via4 ;
	RECT 0.100000 -0.025000 0.150000 0.025000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal5 ;
	RECT -0.025000 -0.055000 0.150000 0.055000 ;
END VIA45_2C_E

VIA VIA45_2C_S DEFAULT
    LAYER Metal4 ;
	RECT -0.055000 -0.150000 0.055000 0.025000 ;
    LAYER Via4 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.025000 -0.150000 0.025000 -0.100000 ;
    LAYER Metal5 ;
	RECT -0.025000 -0.180000 0.025000 0.055000 ;
END VIA45_2C_S

VIA VIA45_2C_CV DEFAULT
    LAYER Metal4 ;
	RECT -0.055000 -0.087500 0.055000 0.087500 ;
    LAYER Via4 ;
	RECT -0.025000 0.037500 0.025000 0.087500 ;
	RECT -0.025000 -0.087500 0.025000 -0.037500 ;
    LAYER Metal5 ;
	RECT -0.025000 -0.117500 0.025000 0.117500 ;
END VIA45_2C_CV

VIA VIA45_2C_N DEFAULT
    LAYER Metal4 ;
	RECT -0.055000 -0.025000 0.055000 0.150000 ;
    LAYER Via4 ;
	RECT -0.025000 0.100000 0.025000 0.150000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal5 ;
	RECT -0.025000 -0.055000 0.025000 0.180000 ;
END VIA45_2C_N

VIA VIA56_2C_W DEFAULT
    LAYER Metal5 ;
	RECT -0.150000 -0.055000 0.025000 0.055000 ;
    LAYER Via5 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.150000 -0.025000 -0.100000 0.025000 ;
    LAYER Metal6 ;
	RECT -0.180000 -0.025000 0.055000 0.025000 ;
END VIA56_2C_W

VIA VIA56_2C_CH DEFAULT
    LAYER Metal5 ;
	RECT -0.087500 -0.055000 0.087500 0.055000 ;
    LAYER Via5 ;
	RECT 0.037500 -0.025000 0.087500 0.025000 ;
	RECT -0.087500 -0.025000 -0.037500 0.025000 ;
    LAYER Metal6 ;
	RECT -0.117500 -0.025000 0.117500 0.025000 ;
END VIA56_2C_CH

VIA VIA56_2C_E DEFAULT
    LAYER Metal5 ;
	RECT -0.025000 -0.055000 0.150000 0.055000 ;
    LAYER Via5 ;
	RECT 0.100000 -0.025000 0.150000 0.025000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal6 ;
	RECT -0.055000 -0.025000 0.180000 0.025000 ;
END VIA56_2C_E

VIA VIA56_2C_S DEFAULT
    LAYER Metal5 ;
	RECT -0.025000 -0.180000 0.025000 0.055000 ;
    LAYER Via5 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
	RECT -0.025000 -0.150000 0.025000 -0.100000 ;
    LAYER Metal6 ;
	RECT -0.055000 -0.150000 0.055000 0.025000 ;
END VIA56_2C_S

VIA VIA56_2C_CV DEFAULT
    LAYER Metal5 ;
	RECT -0.025000 -0.117500 0.025000 0.117500 ;
    LAYER Via5 ;
	RECT -0.025000 0.037500 0.025000 0.087500 ;
	RECT -0.025000 -0.087500 0.025000 -0.037500 ;
    LAYER Metal6 ;
	RECT -0.055000 -0.087500 0.055000 0.087500 ;
END VIA56_2C_CV

VIA VIA56_2C_N DEFAULT
    LAYER Metal5 ;
	RECT -0.025000 -0.055000 0.025000 0.180000 ;
    LAYER Via5 ;
	RECT -0.025000 0.100000 0.025000 0.150000 ;
	RECT -0.025000 -0.025000 0.025000 0.025000 ;
    LAYER Metal6 ;
	RECT -0.055000 -0.025000 0.055000 0.150000 ;
END VIA56_2C_N

VIA VIA67_2C_W DEFAULT
    LAYER Metal6 ;
	RECT -0.235000 -0.035000 0.065000 0.035000 ;
    LAYER Via6 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
	RECT -0.205000 -0.035000 -0.135000 0.035000 ;
    LAYER Metal7 ;
	RECT -0.205000 -0.065000 0.035000 0.065000 ;
END VIA67_2C_W

VIA VIA67_2C_CH DEFAULT
    LAYER Metal6 ;
	RECT -0.150000 -0.035000 0.150000 0.035000 ;
    LAYER Via6 ;
	RECT 0.050000 -0.035000 0.120000 0.035000 ;
	RECT -0.120000 -0.035000 -0.050000 0.035000 ;
    LAYER Metal7 ;
	RECT -0.120000 -0.065000 0.120000 0.065000 ;
END VIA67_2C_CH

VIA VIA67_2C_E DEFAULT
    LAYER Metal6 ;
	RECT -0.065000 -0.035000 0.235000 0.035000 ;
    LAYER Via6 ;
	RECT 0.135000 -0.035000 0.205000 0.035000 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
    LAYER Metal7 ;
	RECT -0.035000 -0.065000 0.205000 0.065000 ;
END VIA67_2C_E

VIA VIA67_2C_S DEFAULT
    LAYER Metal6 ;
	RECT -0.065000 -0.205000 0.065000 0.035000 ;
    LAYER Via6 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
	RECT -0.035000 -0.205000 0.035000 -0.135000 ;
    LAYER Metal7 ;
	RECT -0.035000 -0.235000 0.035000 0.065000 ;
END VIA67_2C_S

VIA VIA67_2C_CV DEFAULT
    LAYER Metal6 ;
	RECT -0.065000 -0.120000 0.065000 0.120000 ;
    LAYER Via6 ;
	RECT -0.035000 0.050000 0.035000 0.120000 ;
	RECT -0.035000 -0.120000 0.035000 -0.050000 ;
    LAYER Metal7 ;
	RECT -0.035000 -0.150000 0.035000 0.150000 ;
END VIA67_2C_CV

VIA VIA67_2C_N DEFAULT
    LAYER Metal6 ;
	RECT -0.065000 -0.035000 0.065000 0.205000 ;
    LAYER Via6 ;
	RECT -0.035000 0.135000 0.035000 0.205000 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
    LAYER Metal7 ;
	RECT -0.035000 -0.065000 0.035000 0.235000 ;
END VIA67_2C_N

VIA VIA78_2C_W DEFAULT
    LAYER Metal7 ;
	RECT -0.205000 -0.065000 0.035000 0.065000 ;
    LAYER Via7 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
	RECT -0.205000 -0.035000 -0.135000 0.035000 ;
    LAYER Metal8 ;
	RECT -0.235000 -0.035000 0.065000 0.035000 ;
END VIA78_2C_W

VIA VIA78_2C_CH DEFAULT
    LAYER Metal7 ;
	RECT -0.120000 -0.065000 0.120000 0.065000 ;
    LAYER Via7 ;
	RECT 0.050000 -0.035000 0.120000 0.035000 ;
	RECT -0.120000 -0.035000 -0.050000 0.035000 ;
    LAYER Metal8 ;
	RECT -0.150000 -0.035000 0.150000 0.035000 ;
END VIA78_2C_CH

VIA VIA78_2C_E DEFAULT
    LAYER Metal7 ;
	RECT -0.035000 -0.065000 0.205000 0.065000 ;
    LAYER Via7 ;
	RECT 0.135000 -0.035000 0.205000 0.035000 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
    LAYER Metal8 ;
	RECT -0.065000 -0.035000 0.235000 0.035000 ;
END VIA78_2C_E

VIA VIA78_2C_S DEFAULT
    LAYER Metal7 ;
	RECT -0.035000 -0.235000 0.035000 0.065000 ;
    LAYER Via7 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
	RECT -0.035000 -0.205000 0.035000 -0.135000 ;
    LAYER Metal8 ;
	RECT -0.065000 -0.205000 0.065000 0.035000 ;
END VIA78_2C_S

VIA VIA78_2C_CV DEFAULT
    LAYER Metal7 ;
	RECT -0.035000 -0.150000 0.035000 0.150000 ;
    LAYER Via7 ;
	RECT -0.035000 0.050000 0.035000 0.120000 ;
	RECT -0.035000 -0.120000 0.035000 -0.050000 ;
    LAYER Metal8 ;
	RECT -0.065000 -0.120000 0.065000 0.120000 ;
END VIA78_2C_CV

VIA VIA78_2C_N DEFAULT
    LAYER Metal7 ;
	RECT -0.035000 -0.065000 0.035000 0.235000 ;
    LAYER Via7 ;
	RECT -0.035000 0.135000 0.035000 0.205000 ;
	RECT -0.035000 -0.035000 0.035000 0.035000 ;
    LAYER Metal8 ;
	RECT -0.065000 -0.035000 0.065000 0.205000 ;
END VIA78_2C_N

VIARULE M4_M3 GENERATE DEFAULT
  LAYER Metal3 ;
    ENCLOSURE 0.005 0.03 ;
  LAYER Via3 ;
    RECT -0.025 -0.025 0.025 0.025 ;
    SPACING 0.11 BY 0.11 ;
  LAYER Metal4 ;
    ENCLOSURE 0.005 0.03 ;
END M4_M3

VIARULE M5_M4 GENERATE DEFAULT
  LAYER Metal4 ;
    ENCLOSURE 0.005 0.03 ;
  LAYER Via4 ;
    RECT -0.025 -0.025 0.025 0.025 ;
    SPACING 0.11 BY 0.11 ;
  LAYER Metal5 ;
    ENCLOSURE 0.005 0.03 ;
END M5_M4

VIARULE M6_M5 GENERATE DEFAULT
  LAYER Metal5 ;
    ENCLOSURE 0.005 0.03 ;
  LAYER Via5 ;
    RECT -0.025 -0.025 0.025 0.025 ;
    SPACING 0.11 BY 0.11 ;
  LAYER Metal6 ;
    ENCLOSURE 0.005 0.03 ;
END M6_M5

VIARULE M7_M6 GENERATE DEFAULT
  LAYER Metal6 ;
    ENCLOSURE 0.005 0.03 ;
  LAYER Via6 ;
    RECT -0.035 -0.035 0.035 0.035 ;
    SPACING 0.15 BY 0.15 ;
  LAYER Metal7 ;
    ENCLOSURE 0.005 0.03 ;
END M7_M6

VIARULE M8_M7 GENERATE DEFAULT
  LAYER Metal7 ;
    ENCLOSURE 0.005 0.03 ;
  LAYER Via7 ;
    RECT -0.035 -0.035 0.035 0.035 ;
    SPACING 0.15 BY 0.15 ;
  LAYER Metal8 ;
    ENCLOSURE 0.005 0.03 ;
END M8_M7

SITE CoreSite
  CLASS CORE ;
  SIZE 0.1 BY 1.2 ;
END CoreSite

'''

with open('mlp.lef', 'w') as f:
    f.write(BEGIN)
    for i in range(0, 2):
        for j in range(0, 4):
            if i:
                name = 'NEUROS{0}'.format(j)
            else:
                name = 'NEURON{0}'.format(j)

            f.write('MACRO {0}\n'.format(name))
            f.write('    CLASS CORE ;\n')
            f.write('    FOREIGN {0} 0.000000 0.000000 ;\n'.format(name))
            f.write('    ORIGIN 0.000000 0.000000 ;\n')
            f.write('    SIZE {0:.1f} BY 1.200000 ;\n'.format(-j * 0.1 + 6.4))
            f.write('    SYMMETRY X Y ;\n')
            f.write('    SITE CoreSite ;\n')
            for k in range(0, 5):
                for l in range(0, 8):
                    f.write('    PIN A{0}{1}\n'.format(k, l))
                    f.write('        DIRECTION INPUT ;\n')
                    f.write('        USE SIGNAL ;\n')
                    f.write('        PORT\n')
                    f.write('        LAYER Metal1 ;\n')
                    x = l * 0.6 + 0.3
                    if i:
                        y = -k * 0.2 + 1.0
                    else:
                        y = +k * 0.2 + 0.2

                    f.write('        RECT {0:.3f} {1:.3f} {2:.3f} {3:.3f} ;\n'.format(x - 0.025, y - 0.055, x + 0.025, y + 0.055))
                    f.write('        END\n')
                    f.write('    END A{0}{1}\n'.format(k, l))

            for k in range(0, 4):
                for l in range(0, 2):
                    f.write('    PIN Y{0}\n'.format(k * 2 + l))
                    f.write('        DIRECTION OUTPUT ;\n')
                    f.write('        USE SIGNAL ;\n')
                    f.write('        PORT\n')
                    f.write('        LAYER Metal1 ;\n')
                    x = -j * 0.1 + l * 0.6 + 5.5
                    if i:
                        y = -k * 0.2 + 0.9
                    else:
                        y = +k * 0.2 + 0.3

                    f.write('        RECT {0:.3f} {1:.3f} {2:.3f} {3:.3f} ;\n'.format(x - 0.025, y - 0.055, x + 0.025, y + 0.055))
                    f.write('        END\n')
                    f.write('    END Y{0}\n'.format(k * 2 + l))

            f.write('    PIN VDD\n')
            f.write('        DIRECTION INOUT ;\n')
            f.write('        SHAPE ABUTMENT ;\n')
            f.write('        USE POWER ;\n')
            f.write('        PORT\n')
            f.write('        LAYER Metal1 ;\n')
            f.write('        RECT 0.000000 1.120000 {0:.1f} 1.280000 ;\n'.format(-j * 0.1 + 6.4))
            f.write('        END\n')
            f.write('    END VDD\n')
            f.write('    PIN VSS\n')
            f.write('        DIRECTION INOUT ;\n')
            f.write('        SHAPE ABUTMENT ;\n')
            f.write('        USE GROUND ;\n')
            f.write('        PORT\n')
            f.write('        LAYER Metal1 ;\n')
            f.write('        RECT 0.000000 -0.080000 {0:.1f} 0.080000 ;\n'.format(-j * 0.1 + 6.4))
            f.write('        END\n')
            f.write('    END VSS\n')
            f.write('END {0}\n\n'.format(name))

    f.write('END LIBRARY\n\n')

