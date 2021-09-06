#!/usr/bin/env python3

# NOTE: All the shells that are generated for you have been copied from : https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md

import argparse

## All the available shells:
shells = [
	'bash', 'php', 'php_one_liner', 'php_windows', 'perl', 'perl_windows', 'python', 'python2_windows', 'powershell', 'powershell_nishang',
	'netcat', 'netcat_windows', 'netcat_windows_ps', 'lua', 'ruby', 'golang', 'awk'
]

class Generator:
	def __init__(self, shell, ip, port, out_file):
		self.shell = shell
		self.ip = ip
		self.port = port
		self.out_file = out_file
		self.IP_DELIM = 'REV_SHELL_IP'
		self.PORT_DELIM = 'REV_SHELL_PORT'
	def generate(self):

		shell_file = 'shells/' + self.shell
		# Reading the shell from the file
		try:
			f = open(shell_file, 'r')
		except Exception as E:
			print(f"[-] An error occurred. Error Details: {E}")
			exit()

		shell_data = f.read()
		f.close()
		shell_data = shell_data.replace(self.IP_DELIM, self.ip)
		shell_data = shell_data.replace(self.PORT_DELIM, str(self.port))

		if self.out_file != None:
			try:
				f = open(self.out_file, 'w')
			except Exception as E:
				print(f"[-] An error occurred. Error Details: {E}")
				exit()

			f.write(shell_data)
			f.close()
			print(f"[+] Successfully Stored reverse shell to file {self.out_file}.")
		else:
			print("[*] Shell is:")
			print("=" * 25)
			print(f"{shell_data}")
			print("=" * 25)


class ArgsHandler:
	def __init__(self):
		self.banner = '''
		                    _          _ _
		 _ __ _____   _____| |__   ___| | |
		| '__/ _ \ \ / / __| '_ \ / _ \ | |
		| | |  __/\ V /\__ \ | | |  __/ | |
		|_|  \___| \_/ |___/_| |_|\___|_|_|
						by @TheFlash2k'''

		self.parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description=f"{self.banner}\nrevshell - A Reverse Shell Generator from the CLI - By @TheFlash2k")
		self.parser.add_argument("shell",help="The type of reverse shell you want to generate.",choices=shells)
		self.parser.add_argument("--address", "-i",dest="ip_address",help="The Attacker's IP Address.",required=True)
		self.parser.add_argument("--port", "-p",dest="port",help="The Attacker's Listening Port.",type=int,required=True)
		self.parser.add_argument("--output", "-o",dest="out_file",help="The Output file name of the reverse shell.")

	def get_all_args(self):
		parser = self.parser.parse_args()
		return parser.shell, parser.ip_address, parser.port, parser.out_file

if __name__ == "__main__":

	args = ArgsHandler()
	shell, ip, port, out_file = args.get_all_args()
	gen = Generator(shell=shell, ip=ip, port=port, out_file=out_file)
	gen.generate()