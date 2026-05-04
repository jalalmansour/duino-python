from .._exceptions import DuinoError

INSTRUCTIONS = """

Duino error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install Duino[{extra}]

"""


def format_instructions(*, library: str, extra: str) -> str:
    return INSTRUCTIONS.format(library=library, extra=extra)


class MissingDependencyError(DuinoError):
    pass
