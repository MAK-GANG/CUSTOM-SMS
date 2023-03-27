import os
import time
from platform import machine
if machine()=='aarch64':
	import MAIN
else:
	time.sleep(2)
	print("  		\033[1;91m Sorry Bro System Not Supported   \n 		 Contact Me To Use The Tools ")
	print(" Follow Team Dccs-team On Github ")
	os.system('xdg-open https://github.com/Dccs-team/ ')
	time.sleep(3)
	print("		 Tools Is Free Don’t Worry ")
	time.sleep(1)
	os.system('xdg-open https://wa.me/+8801870830179')
	os.system('clear')
	print(" If You Have 64bit Then Run Again ")
	os.system(' cd $HOME && rm -rf CUSTOM-SMS ')
	
