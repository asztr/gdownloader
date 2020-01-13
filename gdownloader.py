#!/usr/bin/env python
import sys, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", help="gdriveID or URL")
parser.add_argument("-l", "--large", default=False, action="store_true", help="large files")
parser.add_argument("-o", "--output", type=str, default=None, help="name of output filename")
args = parser.parse_args()

if 'drive.google.com' in args.input:
        driveid = args.input.split('id=')[-1]
else:
        driveid = args.input

if args.output is not None:
        out_cmd = " -O "+args.output
else:
        out_cmd = ""

if args.large is True:
        cmd = '''wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id='''
        cmd += driveid+"'"
        cmd += " -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/"
        cmd += r"\1\n"
        cmd += "/p')&id="
        cmd += driveid+'"'
        cmd += out_cmd
        cmd += " && rm -rf /tmp/cookies.txt"
else:
        cmd = "wget --no-check-certificate 'https://docs.google.com/uc?export=download&id="
        cmd += driveid+"'"
        cmd += out_cmd

print(os.popen(cmd).read())
