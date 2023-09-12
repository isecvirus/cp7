"""
* Author  = virus
* Version = 1.0.0

- https://www.github.com/isecvirus/cpd
@ All rights reserved for virus (c) 2023
"""

from util import CiscoPassword
from argparse import ArgumentParser

parser = ArgumentParser(prog="cpd", usage="%(prog)s [options]", description="Cisco password type 7 decipher.")
parser.add_argument("-e", "--encrypt", action="store_true", dest="encrypt", default=False, help="Encrypt the password.")
parser.add_argument("-d", "--decrypt", action="store_true", dest="decrypt", default=True, help="Decrypt the password.")
parser.add_argument("password", action="store", nargs="?")
args = parser.parse_args()

if args.password:
    args.decrypt = False if args.encrypt else True

    cp = CiscoPassword(args.password)

    if args.decrypt:
        try:
            password = cp.decrypt()
            print(password)
        except (AttributeError, IndexError):
            print("\033[91m\033[1mError\033[0m: this isn't looking like a cisco password.")
    elif args.encrypt:
        print(cp.encrypt())
else:
    print("\033[93m\033[1mWarning\033[0m: give me a password.")