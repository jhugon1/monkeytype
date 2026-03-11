import re, os

def sf(path, pat=None, rng=None):
    try:
        lines = open(path, encoding='utf-8').readlines()
    except:
        return f'NOT FOUND: {path}\n'
    if rng:
        s,e=rng; return ''.join(f'{s+i}: {l}' for i,l in enumerate(lines[s-1:e]))
    rx=re.compile(pat)
    r=[f'{i+1}: {l}' for i,l in enumerate(lines) if rx.search(l)]
    return ''.join(r) or '(no matches)\n'

out=[]

out.append('=== event-handlers/test.ts 35-60 ===\n')
out.append(sf('frontend/src/ts/event-handlers/test.ts', rng=(35,60)))

out.append('\n=== test-logic.ts 1418-1440 ===\n')
out.append(sf('frontend/src/ts/test/test-logic.ts', rng=(1418,1440)))

out.append('\n=== config-metadata.ts 115-145 ===\n')
out.append(sf('frontend/src/ts/config-metadata.ts', rng=(115,145)))

out.append('\n=== ModeSchema - find dictionary mode ===\n')
out.append(sf('packages/schemas/src/shared.ts', r'dictionary|Mode'))

out.append('\n=== words-generator.ts getDictionaryWordList 315-325 ===\n')
out.append(sf('frontend/src/ts/test/words-generator.ts', rng=(315,325)))

out.append('\n=== test-config.ts 260-285 ===\n')
out.append(sf('frontend/src/ts/test/test-config.ts', rng=(260,285)))

out.append('\n=== test-config.ts 1-20 (imports) ===\n')
out.append(sf('frontend/src/ts/test/test-config.ts', rng=(1,20)))

out.append('\n=== event-handlers/test.ts 1-45 ===\n')
out.append(sf('frontend/src/ts/event-handlers/test.ts', rng=(1,45)))

txt=''.join(out)
print(txt)
open('grep_results.txt','w',encoding='utf-8').write(txt)
print('Saved.')