"""
Converts a dict to a .lang string.
"""

import mclang


def test_dumps():
    obj = {
        "test": "This is cool!",
        "test2": "It worked!",
    }

    result = mclang.dumps(obj)
    print(result)
