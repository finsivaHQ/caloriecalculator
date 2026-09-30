import os
import glob

def fix_utf8(path):
    with open(path, 'rb') as f:
        content = f.read()
    
    # If it contains the exact utf-8 bytes for A (which was how powerShell mangled it?)
    # Wait, if I read it in python as bytes, earlier I saw:
    # b' "\xc2\xbfC\xc3\xb3mo calculo mi cantidad '
    # Which means the file on disk is PERFECT UTF-8. 
    # But wait! Why did the LIVE SITE (Cloudflare) show broken text for some pages earlier?
    # Because Cloudflare Pages deployed the files that were pushed.
    pass

