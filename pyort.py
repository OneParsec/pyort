#!/usr/bin/python3

import argparse
import requests
import os
from bs4 import BeautifulSoup
from os.path import expanduser
from git import Repo
from colors import *
from sys import exit

parser = argparse.ArgumentParser(description="Pyort - AUR Helper, written by Python")
parser.add_argument('-S', dest="package", required=True, help='Package to install')
args = parser.parse_args()

home = expanduser("~")
package = str(args.package)
folder = home + "/" + "." + package + ".Pyort"
link = "https://aur.archlinux.org/packages/" + package
print(G + "==> " + C + "Clearing cache " + W)
clearcmd = "sudo rm -r " + folder
os.system(clearcmd)


r = requests.get(link)
soup = BeautifulSoup(r.text, 'lxml')

try:
	dwnlink = soup.find('table', id = 'pkginfo').find_all("a")[0]
except AttributeError:
	print(G + "==> " + R + "ERROR: Package not found! " + W)
	exit(1)
dwnlink = str(dwnlink)
dwnlink = dwnlink.split(">")[1]
dwnlink = dwnlink.split("<")[0]

print(G + "==> " + C + "Downloading package: " + R + package + W)
Repo.clone_from(dwnlink, folder)
os.chdir(folder)
print(G + "==> " + C + "Building package: " + R + package + W)
os.system("makepkg -sri")
os.system(clearcmd)
