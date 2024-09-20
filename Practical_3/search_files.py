import subprocess

dir1 = input("Enter the directory full path : ")
search = input("Enter file or folder name : ")

command = f'dir "{dir1}\\*{search}*" /s'
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print("\nSearch results:\n")
print(result.stdout)

if "Directory of" in result.stdout:
    print("File or folder Found...")
else:
    print("File or folder NOT FOUND...")