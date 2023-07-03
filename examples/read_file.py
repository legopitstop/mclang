import mclang

with open('output.lang', 'r') as r:
    doc = mclang.load(r)
    res = doc.tl('test')
    print(f'"{res}"')