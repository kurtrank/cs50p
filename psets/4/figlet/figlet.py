import sys
from pyfiglet import Figlet
from random import choice

arglen = len(sys.argv)

figlet = Figlet()
fontsList = figlet.getFonts()

if arglen in [1, 3]:
    font = choice(fontsList)

    if arglen == 3:
        arg = sys.argv[1]
        font = sys.argv[2]

        if font not in fontsList or arg not in ['-f', '--font']:
            sys.exit('Invalid usage')

    figlet.setFont(font=font)
    print(figlet.renderText(input('Input: ')))
else:
    sys.exit('Invalid usage')
