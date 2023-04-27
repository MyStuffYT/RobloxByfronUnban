filerecovery = open("hwidbackup.txt", "r")
new_hwid = filerecovery.read()
filerecovery.close()

subprocess.call('reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SystemInformation /v SystemProductName /t REG_SZ /d "{0}" /f'.format(new_hwid), shell=True)
subprocess.call('reg add HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion /v ProductId /t REG_SZ /d "{0}" /f'.format(new_hwid), shell=True)

p = subprocess.Popen('wmic csproduct get uuid', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()
spoofed_hwid = out.decode().split('\n')[1].strip()

if spoofed_hwid == new_hwid:
    print('HWID backed up')
    print("Press enter to exit")
    input()
    pass
else:
    print('HWID backup failed (you may reboot and rerun this program)')
    print("Press enter to exit")
    input()
    exit()
exit()
