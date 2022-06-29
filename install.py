#!/usr/bin/env python3
import os

def cp(what,where): os.system('cp ' + what + " " + where)
def aptI(pkg): os.system('apt install '+ pkg)

def install():
    cp("./.bashrc", "~/.bashrc")
    cp("./.bash_aliases", "~/.bash_aliases")
    cp("./.gitconfig", "~/.gitconfig")
    cp("./.gitconfig.local", "~/.gitconfig.local")
    cp("./.startup", "~/.startup")
    cp("./.startup.txt","~/.startup.txt")
    cp("./.zcompdump", "~/.zcompdump")
    cp("./.zshrc","~/.zshrc")
    cp("./.config/htop/htoprc","~/.config/htop/htoprc")
    cp("./workspace/.codio","~/workspace/.codio")

def main():
    a = input("Are you sure? (y/n)")
    if a == "n": print('goodbye')
    if a == 'y': install()

if __name__ == "__main__": main()
