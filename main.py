#!/usr/bin/env python

import wxversion
wxversion.select(['2.8.12'])

#import wx

import subprocess

print "\n", subprocess.Popen('ps -c -o pid,ppid,user', shell=True)

print "\033[31;44mTEXT\033[39;49m"
