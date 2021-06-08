import os
import shutil
import argparse

# Written By NxtDaemon Any Issues or Additions you would like please contact me here https://nxtdaemon.xyz/contact
#  __    __            __     _______                                                   
# |  \  |  \          |  \   |       \                                                  
# | ▓▓\ | ▓▓__    __ _| ▓▓_  | ▓▓▓▓▓▓▓\ ______   ______  ______ ____   ______  _______  
# | ▓▓▓\| ▓▓  \  /  \   ▓▓ \ | ▓▓  | ▓▓|      \ /      \|      \    \ /      \|       \ 
# | ▓▓▓▓\ ▓▓\▓▓\/  ▓▓\▓▓▓▓▓▓ | ▓▓  | ▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\
# | ▓▓\▓▓ ▓▓ >▓▓  ▓▓  | ▓▓ __| ▓▓  | ▓▓/      ▓▓ ▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓
# | ▓▓ \▓▓▓▓/  ▓▓▓▓\  | ▓▓|  \ ▓▓__/ ▓▓  ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓__/ ▓▓ ▓▓  | ▓▓
# | ▓▓  \▓▓▓  ▓▓ \▓▓\  \▓▓  ▓▓ ▓▓    ▓▓\▓▓    ▓▓\▓▓     \ ▓▓ | ▓▓ | ▓▓\▓▓    ▓▓ ▓▓  | ▓▓ 
#  \▓▓   \▓▓\▓▓   \▓▓   \▓▓▓▓ \▓▓▓▓▓▓▓  \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓  \▓▓  \▓▓ \▓▓▓▓▓▓ \▓▓   \▓▓
                                                                                      
class Color:
    'Class for Colors to be used in Execution'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    QuestionColor = BOLD+YELLOW
    ErrorColor = RED+BOLD
    InfoColor = CYAN 
    SuccessColor = GREEN

class Notify():
	'Managed what type of message is sent'

	def Error(Message):
		'Error Messages'
		print(f"{Color.ErrorColor}[!] - {Message}{Color.RESET}")

	def Info(Message):
		'Infomation Messages'
		print(f"{Color.InfoColor}[*] - {Message}{Color.RESET}")

	def Success(Message):
		'Success Messages'
		print(f"{Color.SuccessColor}[$] - {Message}{Color.RESET}")

	def Question(Message):
		'Get infomation from user'
		input(f"{Color.QuestionColor}[?] - {Message}{Color.RESET}")


class ManageHosts():
	def AppendHosts(Entry):
		try:
			os.system(f"""sudo sh -ce "echo {Entry} >> /etc/hosts" """)
			return(0)
		except Exception as Err:
			Notify.Error(f"Error Found : '{Err}'")
			return(1)

	def RemoveHosts():
		print("Function to be Written later")

# Argparse 
Parser = argparse.ArgumentParser()
Parser.add_argument("ip",help="pass the IP to add to /etc/hosts",type=str,action="store")
Parser.add_argument("Hostname",help="pass the Hostname to add to /etc/hosts",type=str,action="extend",nargs="+")
Args = Parser.parse_args()

def main():
	Notify.Info("Started Process")
	# Unpacking Variables
	IP = Args.ip 
	Hostname = Args.Hostname
	Notify.Info("Collected Arguments")

	# Set String to add 
	Hosts = " ".join(Hostname)
	Entry = f"{IP} {Hosts}"
	Notify.Info("Generated Entry")
	Failure = ManageHosts.AppendHosts(Entry) 
	if Failure: Notify.Error("Program Failed") ; exit()
	Notify.Success("Added Entry to /etc/hosts")



if __name__ == "__main__":
	main()