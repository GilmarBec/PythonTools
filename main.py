from console_style.output import Output, ConsoleColors


class Main:
    TOOLS = [
        "List:From types.list import List",
        "Tree:From types.tree import Tree",
        "Console Style:from console_style.output import Output, ConsoleColors"
    ]

    @staticmethod
    def start() -> None:
        console_style = Output(
            color=ConsoleColors.REFERENCE_RED,
            background=ConsoleColors.REFERENCE_WHITE,
            options=ConsoleColors.REFERENCE_BOLD,
        )

        console_style.title("TOOLS")

        section = []

        for tool in Main.TOOLS:
            name, description = tool.split(':', 2)
            section += [f'{name}: {description}']

        console_style.section(section)


if __name__ == '__main__':
    Main.start()
