# HostEditor
Quick Python Script to add hosts via command line without using vim or an editor

# Notes : 
to use this program without sudo append the following statment to your /etc/sudoers file, this should *not* be used on a standard system due to creating easy PrivEsc Vectors but I dont see an issue for a hacking/pentesting distribution but do switch out the /usr/bin/python3 for wherever the binary is and the Absoulute path for AddHost.py for instance mine looks something like this 

{NAME} ALL=(ALL) NOPASSWD:/usr/bin/python3 /home/nxtdaemon/Documents/HostEditor/AddHost.py
