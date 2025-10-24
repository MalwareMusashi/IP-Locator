How to Install and Run it Anywhere

Download the script

1.) Grab it straight to your terminal:
```
curl -O https://raw.githubusercontent.com/MalwareMusashi/IP-Locator/main/iplookup.py
```

Or clone the repo:
```
git clone https://github.com/MalwareMusashi/IP-Locator.git
cd iplookup
```

2.) Make it executable

Give the file permission to run:
```
chmod +x iplookup.py
```

3.) Move it somewhere in your PATH

This lets you run it from anywhere:
```
sudo mv iplookup.py /usr/local/bin/iplookup
```

Now the command is simply iplookup no matter what folder you’re in.

4.) Test it

Open a new terminal window and run:
```
iplookup
```

You should see the banner pop up and get prompted for an IP or hostname.

5.) (Optional) Add your ipinfo token

If you have an API token from ipinfo.io, export it like this:
```
export IPINFO_TOKEN="your_token_here"
```

To make it permanent, add that line to the end of your ~/.bashrc or ~/.zshrc and reload your shell.

6.) Use it

Examples:
```
iplookup            # your current IP
iplookup 8.8.8.8    # Google DNS
iplookup google.com # hostname lookup
```

That’s it. It’s a single-file tool—no installs, no libraries, just curl and Python.
