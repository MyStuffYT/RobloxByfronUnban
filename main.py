import uuid
import subprocess
import os
print("Byfron anti-cheat unbanner (Run recover.exe to recover your hwid back.)")

aa = input("type 'start' to start:")


if aa == "start":
    pass
else:
    exit()

print("""

---MyStuffYT is not responsible for the damages---

For any damages done to your Windows Installation, MyStuffYT (me) is not responsible at all
I recommend you to backup your Windows Installation before running this program
Do not use to hack. Only use it for other stuff like bypassing false bans because of having cheat engine running in the background or something
USE IT FOR EDUCATIONAL PURPOSES ONLY, NO EVIL!
I repeat: I recommend you to backup your Windows Installation before running this program


(fun tip: use proxies and new accounts when you run byfron anti-ban)


---MyStuffYT is not responsible for the damages---
""")

notrep = input('Type "MyStuffYT is not responsible for any damage done.": ')

if notrep == "MyStuffYT is not responsible for any damage done.":
    print("Passed. MYSTUFFYT ISN'T RESPONSIBLE TEAM JOINED.")
    pass
else:
    exit()

print("generating hwid")

guid = uuid.uuid4()

hwid = str(guid).upper()

print("New hwid that will be applied: " + hwid)

p = subprocess.Popen('wmic csproduct get uuid', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()
current_hwid = out.decode().split('\n')[1].strip()

print("Checked current hwid.")

print("Backing up current hwid...")

recoverfile = open("hwidbackup.txt", "w")
recoverfile.write(current_hwid)
recoverfile.close()
recoverfile = open("hwidbackup.txt", "r")
if recoverfile.read() == current_hwid:
    print("Backed up HWID!")
else:
    print("Failed to backup!!!")
    usure = input("Would you like to not backup your HWID? (Yes/n): ")
    if usure == "Yes":
        print("You still sure bro? type yes and press enter! This cannot be reversible!")
        urealysure = input()
        if urealysure == "yes":
            pass
        else:
            print("Press enter to exit (you aren't sure.)")
            input()
            exit()
        pass
    else:
        print("You aint sure boy")
        input("Press enter to exit. ")
        exit()


new_hwid = hwid

print("Applied hwid variable")

print("Applying HWID to windows installation...")

subprocess.call('reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SystemInformation /v SystemProductName /t REG_SZ /d "{0}" /f'.format(new_hwid), shell=True)
subprocess.call('reg add HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion /v ProductId /t REG_SZ /d "{0}" /f'.format(new_hwid), shell=True)

print("Applied HWID")

p = subprocess.Popen('wmic csproduct get uuid', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()
spoofed_hwid = out.decode().split('\n')[1].strip()

print("Checking if HWID has changed yet...")

if spoofed_hwid == new_hwid:
    print('Bypassed hwid ban! (reboot to apply changes, then use new account and new proxy or vpn)')
    input("press enter to exit\n")
else:
    print('Hwid ban not bypassed! press enter to exit (YOU CAN REBOOT AND RERUN THIS PROGRAM IF YOU WANT MORE ACCURATE RESULTS)')
    input()
