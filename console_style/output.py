from console_style.color import ConsoleColors


class Output:
    COLORS = {
        ConsoleColors.REFERENCE_GREY:     ConsoleColors.TEXT_GREY,
        ConsoleColors.REFERENCE_RED:      ConsoleColors.TEXT_RED,
        ConsoleColors.REFERENCE_GREEN:    ConsoleColors.TEXT_GREEN,
        ConsoleColors.REFERENCE_YELLOW:   ConsoleColors.TEXT_YELLOW,
        ConsoleColors.REFERENCE_BLUE:     ConsoleColors.TEXT_BLUE,
        ConsoleColors.REFERENCE_PURPLE:   ConsoleColors.TEXT_PURPLE,
        ConsoleColors.REFERENCE_CIAN:     ConsoleColors.TEXT_CIAN,
        ConsoleColors.REFERENCE_WHITE:    ConsoleColors.TEXT_WHITE,
    }

    BACKGROUNDS = {
        ConsoleColors.REFERENCE_GREY:     ConsoleColors.BACKGROUND_GREY,
        ConsoleColors.REFERENCE_RED:      ConsoleColors.BACKGROUND_RED,
        ConsoleColors.REFERENCE_GREEN:    ConsoleColors.BACKGROUND_GREEN,
        ConsoleColors.REFERENCE_YELLOW:   ConsoleColors.BACKGROUND_YELLOW,
        ConsoleColors.REFERENCE_BLUE:     ConsoleColors.BACKGROUND_BLUE,
        ConsoleColors.REFERENCE_PURPLE:   ConsoleColors.BACKGROUND_PURPLE,
        ConsoleColors.REFERENCE_CIAN:     ConsoleColors.BACKGROUND_CIAN,
        ConsoleColors.REFERENCE_WHITE:    ConsoleColors.BACKGROUND_WHITE,
    }

    OPTIONS = {
        ConsoleColors.REFERENCE_BOLD:         ConsoleColors.BOLD,
        ConsoleColors.REFERENCE_UNDERLINE:    ConsoleColors.ITALIC,
        ConsoleColors.REFERENCE_ITALIC:       ConsoleColors.UNDERLINE,
    }

    def __init__(
            self,
            color: str = None,
            background: str = None,
            options: str or list = None
    ):
        self.__background_style = ""
        self.__text_style = ""

        self.__prepare_style(
            color=color,
            background=background,
            options=options,
        )

    def write(
            self,
            text: str,
            color: str = None,
            background: str = None,
            options: str or list = None
    ) -> None:
        style = self.__prepare_style(
            color=color,
            background=background,
            options=options,
        )

        print(f"{style}{text}{ConsoleColors.CLEAR}")

    def title(
            self,
            text: str,
            color: str = None,
            background: str = None,
            options: str or list = None
    ) -> None:
        self.__prepare_style(
            color=color,
            background=background,
            options=options,
        )

        print(f'{self.__background_style}\n')

        text_style_reset = f'{ConsoleColors.CLEAR}{self.__background_style}'

        print(f'\t\t\t{self.__text_style}{text}{text_style_reset}')

        print(f'\n\n{ConsoleColors.CLEAR}')

    def section(
            self,
            texts: list,
            color: str = None,
            background: str = None,
            options: str or list = None
    ) -> None:
        self.__prepare_style(
            color=color,
            background=background,
            options=options,
        )

        print(f'{self.__background_style}\n')

        text_style_reset = f'{ConsoleColors.CLEAR}{self.__background_style}'

        for text in texts:
            print(f'\t{self.__text_style}{text}{text_style_reset}')

        print(f'\n\n{ConsoleColors.CLEAR}')

    def __prepare_style(
            self,
            color: str = None,
            background: str = None,
            options: str or list = None,
    ) -> None:
        self.__select_multiple_options(options)

        if color is not None:
            if color not in self.COLORS:
                raise Exception("Color selected is not valid.")

            self.__text_style += self.COLORS[color]

        if background is not None:
            if background not in self.COLORS:
                raise Exception("Background selected is not valid.")

            self.__background_style = self.BACKGROUNDS[background]

    def __select_multiple_options(self, options: str or list or None):
        if options is None:
            return None

        opt = ""
        all_options = Output.OPTIONS
        if type(options) is list:
            for option in options:
                opt += self.__select_multiple_options(option)

            self.__text_style = opt
            return opt

        if options not in all_options:
            raise Exception("Option selected is not valid.")

        self.__text_style = all_options[options]
        return self.__text_style
