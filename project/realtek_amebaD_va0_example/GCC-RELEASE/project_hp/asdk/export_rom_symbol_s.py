#!/usr/bin/env python

import sys
import subprocess
import os


readelf = '../toolchain/cygwin/asdk-5.4.1/cygwin/newlib/bin/arm-none-eabi-readelf';
axf_file = 'lib/rom_acut/target_rom.axf'

if os.path.exists('rom_symbol_s.txt'):
	os.remove('rom_symbol_s.txt')
file=open('rom_symbol_s.txt', 'w')

command = readelf + " -W -s " + axf_file + " | sort -k 2";

proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

print("SECTIONS", file=file)
print("{", file=file)
for line in proc.stdout:
#	print line
	items = list(filter(None, line.decode('ASCII').strip().split(' ')))

        num = len(items)
        if  num >= 8  :
	    type = items[4]
	    if type.lower() == 'global' or type.lower() == 'weak' : 
	    	address = int(items[1], 16)
            	symbol = items[7]
                print("    " + symbol + " = " + hex(address) + ";", file=file)
                #print "    " + symbol + " = " + hex(address) + ";";

print("}", file=file)

file.close()
