import re
from . import Lang

class LANGDecoderError(Exception): pass

class LANGDecoder:
    def __init__(self, **kw):
        pass

    def decode(self, s) -> Lang:
        remove = [r'\t', r'#.*'] # 
        result = Lang({})
        lines = str(s).split('\n')
        line = 1
        num = 0
        for ln in lines:
            text = ln.lstrip('\ufeff ')
            if text.startswith('##'): # save comments
                print(text)
                result.insert_comment(num, re.sub(r'^##\s', '', text))
                pass
            elif text == '': pass # ignore empty lines
            elif text.startswith('#'): 
                raise LANGDecoderError(f"Line: {line} - Invalid lang file format. New line character was found while parsing key: '{text}'.")
            else:
                kv = text.split('=',1)
                if len(kv) == 2:
                    v = kv[1]
                    for r in remove:
                        v = re.sub(r, '', v)
                    result[kv[0]] = v
                    num+=1
                else:
                    raise LANGDecoderError(f"Line: {line} - Invalid lang file format. New line character was found while parsing key: '{text}'.")


            line+=1
        return result