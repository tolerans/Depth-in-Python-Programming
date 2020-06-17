# -*- coding: utf-8 -*-
import pefile
import sys

def main():
	
	malware_sample = sys.argv[1]
	pe = pefile.PE(malware_sample)

	for entry in pe.DIRECTORY_ENTRY_IMPORT:
		print(entry.dll)
		for imp in entry.imports:
			if (imp.name != None):
				print(f'\t{hex(imp.address)} {imp.name}')
			else:
				print(f'\tord{str(imp.ordinal)}')
			
if __name__ == "__main__":
	main()
