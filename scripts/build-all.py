import os

print("Building packages for all architectures...")

print("Building for arm64...")
os.chdir("scripts/builds/arm64")
os.system("python3 build-arm64.py py2app")

print("Building for x86...")
os.chdir("../x86")
os.system("python3 build-x86.py py2app")
