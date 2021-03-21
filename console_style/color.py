

class ConsoleColors:
    __BASE = '\033['
    CLEAR = f'{__BASE}0m'
    BOLD = f'{__BASE}1m'
    ITALIC = f'{__BASE}4=3m'
    UNDERLINE = f'{__BASE}4m'

    TEXT_GREY = f'{__BASE}90m'
    TEXT_RED = f'{__BASE}91m'
    TEXT_GREEN = f'{__BASE}92m'
    TEXT_YELLOW = f'{__BASE}93m'
    TEXT_BLUE = f'{__BASE}94m'
    TEXT_PURPLE = f'{__BASE}95m'
    TEXT_CIAN = f'{__BASE}96m'
    TEXT_WHITE = f'{__BASE}97m'

    BACKGROUND_GREY = f'{__BASE}100m'
    BACKGROUND_RED = f'{__BASE}101m'
    BACKGROUND_GREEN = f'{__BASE}102m'
    BACKGROUND_YELLOW = f'{__BASE}103m'
    BACKGROUND_BLUE = f'{__BASE}104m'
    BACKGROUND_PURPLE = f'{__BASE}105m'
    BACKGROUND_CIAN = f'{__BASE}106m'
    BACKGROUND_WHITE = f'{__BASE}107m'

    REFERENCE_GREY = 'grey'
    REFERENCE_RED = 'red'
    REFERENCE_GREEN = 'green'
    REFERENCE_YELLOW = 'yellow'
    REFERENCE_BLUE = 'blue'
    REFERENCE_PURPLE = 'purple'
    REFERENCE_CIAN = 'cian'
    REFERENCE_WHITE = 'white'

    REFERENCE_BOLD = 'bold'
    REFERENCE_UNDERLINE = 'underline'
    REFERENCE_ITALIC = 'italic'
