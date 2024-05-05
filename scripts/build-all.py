import os

print("Building packages for all architectures...")

print("Building for arm64...")
print("Working in...")
print(os.getcwd())
os.chdir("scripts/builds/arm64")
os.system("python3 build-arm64.py py2app")

print("Building for x86...")
os.chdir("scripts/builds/x86")
os.system("python3 build-x86.py py2app")
