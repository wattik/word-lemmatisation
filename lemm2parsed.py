# -*- coding: utf-8 -*-
#!/usr/bin/python

from sys import argv

if __name__ == "__main__":
    with open(argv[1]) as dictionary:
        with open(argv[2], "w") as out:
            for line in dictionary:
                bits = line.split('|')
                bits = bits[0:-1]
                if len(bits) <= 2:
                    continue

                root = bits[1]

                for word in bits[2:]:
                    out.write(word + " " + root + "\n")
