import mclang

lang = """
test=This is cool!
test2=It worked!
"""

doc = mclang.loads(lang)

res = doc.tl('test')
print(f'"{res}"')