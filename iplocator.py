#!/usr/bin/env python3
# quick and dirty ipinfo lookup using curl
# why curl? because i already have it everywhere and dont want deps

import subprocess as sp
import json
import sys
import os
from pathlib import Path

# ascii art cause why not
BANNER = r"""
 _____ _____  _                     _             
|_   _|  __ \| |                   | |            
  | | | |__) | |     ___   ___ __ _| |_ ___  _ __ 
  | | |  ___/| |    / _ \ / __/ _` | __/ _ \| '__|
 _| |_| |    | |___| (_) | (_| (_| | || (_) | |   
|_____|_|    |______\___/ \___\__,_|\__\___/|_|   
"""

# hacky color support
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
NC = '\033[0m'

def curl(url):
    """run curl, return output or None"""
    try:
        r = sp.run(['curl', '-s', url], capture_output=True, text=True, timeout=10)
        return r.stdout if r.returncode == 0 else None
    except:
        return None

def lookup(ip=''):
    """lookup ip info"""
    url = f'https://ipinfo.io/{ip}/json' if ip else 'https://ipinfo.io/json'
    
    # add token from env if exists
    token = os.getenv('IPINFO_TOKEN')
    if token:
        url += f'?token={token}'
    
    result = curl(url)
    if not result:
        print(f"{RED}Failed to get data{NC}")
        return None
    
    try:
        return json.loads(result)
    except:
        print(f"{RED}Bad response{NC}")
        return None

def show(data):
    """print the data nicely"""
    if not data:
        return
    
    print()
    for k, v in data.items():
        if k not in ['readme', 'anycast']:  # skip junk
            print(f"{GREEN}{k:10}{NC}: {v}")
    print()

def main():
    # super simple arg parsing
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help']:
            print(BANNER)
            print("""Usage: iplookup.py [IP/hostname]
            
Examples:
  iplookup.py              # your ip
  iplookup.py 8.8.8.8      # google dns
  iplookup.py google.com   # hostname
  
Set IPINFO_TOKEN env var for more requests.""")
            return
        
        target = sys.argv[1]
    else:
        # interactive - show banner
        print(BANNER)
        target = input("IP/hostname (Enter for your IP): ").strip()
    
    # do it
    data = lookup(target)
    if data:
        show(data)
    else:
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nbye")
