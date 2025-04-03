import cowsay
import sys

if len(sys.argc) == 2:
    cowsay.cow(" ".join(sys.argv[1:]))