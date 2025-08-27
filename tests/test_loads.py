"""
Converts a .lang string to a Lang.
"""

import mclang


def test_loads():
    lang = """
    test=This is cool!
    test2=It worked!
    """

    doc = mclang.loads(lang)

    res = doc.tl("test")
    print(f'"{res}"')
