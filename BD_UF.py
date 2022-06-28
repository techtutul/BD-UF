import os,sys,time
 
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.030)
logo =("""
 
 
\033[97;1mUUUUUUUU     UUUUUUUUFFFFFFFFFFFFFFFFFFFFFF
\033[97;1mU::::::U     U::::::UF::::::::::::::::::::F
\033[97;1mU::::::U     U::::::UF::::::::::::::::::::F
\033[97;1mUU:::::U     U:::::UUFF::::::FFFFFFFFF::::F
\033[97;1mU:::::U     U:::::U   F:::::F       FFFFFF
\033[97;1mU:::::D     D:::::U   F:::::F             
\033[97;1mU:::::D     D:::::U   F::::::FFFFFFFFFF   
\033[97;1mU:::::D     D:::::U   F:::::::::::::::F   
\033[97;1mU:::::D     D:::::U   F:::::::::::::::F   
\033[97;1mU:::::D     D:::::U   F::::::FFFFFFFFFF   
\033[97;1mU:::::D     D:::::U   F:::::F             
\033[97;1mU::::::U   U::::::U   F:::::F             
\033[97;1mU:::::::UUU:::::::U FF:::::::FF           
\033[97;1mUU:::::::::::::UU  F::::::::FF           
\033[97;1mUU:::::::::UU    F::::::::FF          
\033[97;1m/UUUUUUUUU      FFFFFFFFFFF           
                                           

 
 
\n\x1b[1;33;40m--------------------------------------------------\n  \x1b[1;36;40mAuthor     \x1b[1;33;40m: \x1b[0;37;40mMajharul Islam Tutul\n  \x1b[1;36;40mGitHub     \x1b[1;33;40m: \x1b[0;37;40mhttps://github.com/techtutul\n  \x1b[1;36;40mFacebook   \x1b[1;33;40m: \x1b[0;37;40mhttps://www.facebook.com/toxic.tutul.GITHUB.toxictutul\n  \x1b[1;36;40mPublic     \x1b[1;33;40m: \x1b[0;37;40m12-06-2022\x1b[1;33;40m
\x1b[1;33;40m--------------------------------------------------\n
""")
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("")
		psb("\033[1;37m     FOLLOW 1ST ADMIN ID  TO GET  USER AND PASS ")
		print("")
		psb("\033[1;32m [1]  TOOL ADMIN ID")
		psb("\033[1;33m [2]  Exit")
		print("")
		SecDet = input("\n\033[1;31m  Choose ==> \033[1;32m")
		if SecDet in ["", " "]:
			exit()
		elif SecDet in ["2", "02"]:
			print("    GOOD BYE BRo♥️")
			os.system("xdg-open https://www.facebook.com/toxic.tutul.GITHUB.toxictutul")
			exit()
		elif SecDet in ["1", "01"]:
			os.system("xdg-open https://www.facebook.com/toxic.tutul.GITHUB.toxictutul")
		else:
			psb("\n\033[1;31m  [<_] WRONG NUMBER SIR.....SELECT CORRCT NUMBER  TO ENTER TOOL.....!")
			time.sleep(2.0)
			Main()
			#os.system("clear")
#			print(logo)
#			print("\033[1;33mType Your Fb id name")
#			print("")
#			input("\n\033[1;32mType Name ==> \033[1;36m")
#			time.sleep(2.1)
#			print("")
#			psb("\033[1;32mSuccessful Bro")
#			time.sleep(2.0)
		os.system("clear")
		print(logo)
		print("\033[1;33m SELECT YOUR CLONING DIGIT ")
		print("\033[0;90m ><><><><><><><><><><><><><><><><><><>><")
		print("\033[0;94m            [1] 6 DIGIT CLONING")
		print("\033[0;93m            [2] 7 DIGIT CLONING")
		print(" \033[96;1m           [3] 8 DIGIT CLONING")
		print(" \033[0;94m           [4] 11 DIGIT CLONING")
		print("  \033[1;97m          [5] FOLLOW ON FACEBOOK")
		print(" \033[1;33m           [6] OWNER GITHUB\033[0;92m ")
		print("\033[0;91m            [E] Exit \n")
		ADNAN =input(" \033[0;93mChoose : ")
		if ADNAN in ["1", "01"]:
			os.system("python2 DIGIT6.py")
		if ADNAN in ["2", "02"]:
			os.system("python2 DGT7.py")
		if ADNAN in ["3", "03"]:
			os.system("python2 DIGIT08.py")
		if ADNAN in ["4", "04"]:
			os.system("python2 CODE11-11.py")
		if ADNAN in ["5", "05"]:
			os.system("xdg-open https://www.facebook.com/toxic.tutul.GITHUB.toxictutul")
			Main()
		if ADNAN in ["6", "06"]:
			os.system("xdg-open https://github.com/techtutul")
			Main()
		if ADNAN in ["E", "e"]:
			exit()	
			
		else:
			print (" Select Correctly ")
			time.sleep(1)
			Main()
try:Main()
except Exception as e:exit(str(e))