# import win10colors

# c = win10colors.Win10Colors()
# print c.colored('TEST1', 'white', 'red')
# print c.colored('TEST2', 'white', 'green')

from win10colors import make_colors
print make_colors('TEST1', 'white', 'red')
print make_colors('TEST2', 'white', 'on_magenta') + make_colors('TEST3', 'white', 'on_blue')

# print "-"*100
# data = "TEST COLORAMA"
# import colorama
# print colorama.Back.RED + data
# import termcolor
# print termcolor.colored('TEST termcolor', 'white', 'on_red')

print "\x1b[31mThis text has a red foreground using SGR.31.\r\n"

class bcolors:
     HEADER = '\033[95m'
     OKBLUE = '\033[94m'
     OKGREEN = '\033[92m'
     WARNING = '\033[93m'
     FAIL = '\033[91m'
     ENDC = '\033[0m'
     BOLD = '\033[1m'
     UNDERLINE = '\033[4m'

print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC