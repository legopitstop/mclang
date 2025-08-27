"""
Builds .lang files from en_US.lang
"""

import mclang
import os


with mclang.open("tests/texts/en_US.lang") as lang:
    for k, v in mclang.LANGUAGES.items():
        print(k)
        lang2 = lang.translate_language(target=v)
        os.makedirs("build/texts", exist_ok=True)
        lang2.save(f"build/texts/{k}.lang")
