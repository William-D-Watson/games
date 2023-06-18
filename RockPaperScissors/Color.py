class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    def print_bold(self, userinput):
        print(self.BOLD + userinput + self.END)

    def print_underline(self, userinput):
        print(self.UNDERLINE + userinput + self.END)

    def print_red(self, userinput):
        print(self.RED + userinput + self.END)

    def print_green(self, userinput):
        print(self.GREEN + userinput + self.END)

    def print_yellow(self, userinput):
        print(self.YELLOW + userinput + self.END)
