import re
import subprocess
import unicodedata
import json

with open('pan-farmazon.txt') as f:
  text = f.read() 

words = list(set(re.sub(r'[^\w\s]', '', text).lower().split()))

#result = subprocess.check_output('your_command', shell=True, text=True)

def translate(w, lang='en'):
  return subprocess\
         .check_output(f't -b :{lang} "{w}"', shell=True)\
         .decode('utf-8')\
         .lower()\
         .strip()


pchr = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ź': 'z',
    'ż': 'z',
}

def bleh(w):
  return ''.join(map(lambda x: x if x not in pchr else pchr[x], w))


pl_fz = {}

for w in words:
  t = translate(w)
  if t != w and t != bleh(w):
    t2 = translate(t, 'pl')
    if  t2 != w:
      pl_fz[t2] = w
      print(f'{t2} - {w}')


for k, v in en_fz.items():
  t = translate(k, 'pl')
  if  t != v:
    pl_fz[t] = v
    print(f'{t} - {v}')

with open('pl_fz.json', 'w') as f:
  json.dump(pl_fz, f)

#nodsfjsdifkosfndsfjoaesidfnokm

letters = sorted(set(map(lambda x: x[0], pl_fz.keys())))

html = ''
html += f'<head><meta charset="utf-8"></head>\n'
for l in letters:
  html += f'<h2>{l.upper()}</h2>\n'
  keys = sorted([k for k in pl_fz.keys if k[0] == l])
  for k in keys:
    if k[0] == l:
      v = pl_fz[k]
      html += f'  <div style="margin-left: 2em">{k} - {v}</div>\n'


with open('index.html', 'w') as f:
  f.write(html)

