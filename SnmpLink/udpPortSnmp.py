#!/usr/bin/python3
import subprocess
import nmap3
from subprocess import Popen, PIPE

# def subPro(ip):
#     shell = subprocess.run(
#         ["sudo",'nmap','-p','161',ip,'-sU'], check=True, capture_output=True)
# #     udpPort = shell.stdout.decode()
# #     return udpPort
# # # subPro()


def subPro(ip):
    cmd = ['sudo', '-S','./udp.sh',ip]
    sudopass = 'Sudo Password'
    # print(sudopass)
    p = Popen(cmd, stdin=PIPE, stderr=PIPE,universal_newlines=True, stdout=PIPE)
    # print(sudopass)
    output = p.communicate(sudopass + '\n')
    for l in output:
        asm = l[0:4]
        print(asm)
        return asm
