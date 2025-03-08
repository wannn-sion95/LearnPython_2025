import pyfiglet

# ANSI color codes with correct syntax
ORANGE = '\033[38;2;255;103;31m'
WHITE = '\033[38;2;255;255;255m'
GREEN = '\033[38;2;0;255;0m'
BLUE = '\033[38;2;0;0;255m'
RESET = '\033[0m'  # Reset color to default

# Create the ASCII art banner with the 'slant' font
banner = pyfiglet.figlet_format('PENS JOSS', font='speed')

# Print the banner with blue color, then reset to white
print(f"{BLUE}{banner}")
