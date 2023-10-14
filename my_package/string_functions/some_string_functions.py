__all__ = ["reverse_string", "add_exclamation_mark"]


def reverse_string(s: str) -> str:
    """Reverses a string.

    Parameters
    ----------
    s : str
        The string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    return s[::-1]


def add_exclamation_mark(s: str) -> str:
    """Adds an exclamation mark to the end of a string.

    Parameters
    ----------
    s : str
        The string to add an explanation mark to.

    Returns
    -------
    str
        The string with an explanation mark added.
    """
    return s + "!"
