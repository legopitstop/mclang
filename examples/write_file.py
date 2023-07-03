import mclang

obj = {
    'test': 'This is cool!',
    'test2': 'It worked!',
}

with open('output.lang', 'w') as w:
    mclang.dump(obj, w)