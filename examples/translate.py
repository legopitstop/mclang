from mclang import tl, init

# initilize builtin translator.
init('texts')

# Translate and print text.
res = tl('language.name')
print(f'"{res}"')