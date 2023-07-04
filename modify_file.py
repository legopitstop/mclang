import mclang

with open('output.lang', 'r') as r:
    obj = mclang.load(r)

    res = obj.tl('test')
    print(f'"{res}"')

with open('output.lang', 'w') as w:
    mclang.dump(obj, w)