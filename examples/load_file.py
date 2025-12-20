"""
Load en_US.lang file
"""

import mclang


with mclang.open("tests/texts/en_US.lang") as lang:
    print(lang)
