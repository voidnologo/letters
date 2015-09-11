class Colorize:
    """Color ANSI codes"""
    colors = {
        'FG_BLACK': '\033[30m',
        'FG_RED': '\033[31m',
        'FG_GREEN': '\033[32m',
        'FG_YELLOW': '\033[33m',
        'FG_BLUE': '\033[34m',
        'FG_MAGENTA': '\033[35m',
        'FG_CYAN': '\033[36m',
        'FG_WHITE': '\033[37m',
        'FG_BOLD_BLACK': '\033[90m',
        'FG_BOLD_RED': '\033[91m',
        'FG_BOLD_GREEN': '\033[92m',
        'FG_BOLD_YELLOW': '\033[93m',
        'FG_BOLD_BLUE': '\033[94m',
        'FG_BOLD_MAGENTA': '\033[95m',
        'FG_BOLD_CYAN': '\033[96m',
        'FG_BOLD_WHITE': '\033[97m',
    }

    ENDC = '\033[0m'

    @classmethod
    def colorize(self, color, text):
        return ('{}{}{}'.format(self.colors[color], text, self.ENDC))
