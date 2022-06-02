import re

def font(name, aspect, location, desc):
    aspect = aspect[0].upper() + aspect[1:]
    return '      {' + f'''
        "name": "{name}",
        "aspect": "{aspect}",
        "location": {location}''' + (f''',
        "desc": "{desc}"''' if desc else '') + '''
      }'''

def dx(dir): return 1 if 'East' in dir else -1 if 'West' in dir else 0
def dy(dir): return 1 if 'South' in dir else -1 if 'North' in dir else 0
def LL(source, start, dir):
    [x, y] = start
    return '      {' + f'''
        "source": "{source}",
        "start": {start},
        "end": [{x+dx(dir)}, {y+dy(dir)}]''' + '''
      }'''

def planeJSON(planematches, planename):
    fonts = []
    LLs = []
    for match in planematches:
        data = match.groupdict()
        name = data['name']
        aspect = data['aspect'] if 'aspect' in data else data['aspect2'] if 'aspect2' in data else '???'
        x, y = data['x'], data['y']
        desc = data['desc'] if 'desc' in data else None
        dir = data['dir'] if 'dir' in data else ''
        loc = [int(x), int(y)]
        fonts.append(font(name, aspect, loc, desc))
        LLs.append(LL(name, loc, dir))
    
    json = '{\n' + f'  "{planename}":' + '{\n'
    
    json += '    "Fonts":['
    for f in fonts:
        json += '\n' + f + ','
    json = json[:-1]
    json += '\n    ],\n'
    
    json += '    "Ley Lines":['
    for l in LLs:
        json += '\n' + l + ','
    json = json[:-1]
    json += '\n    ]\n'
    
    json += '  }\n'
    json += '}'
    
    return json

# aren't regexes fucking beautiful?
# of course not!
fontRegex = '''\
(?P<name>.*)(( \((?P<aspect>.*)-aspected\))|(\n(?P<aspect2>.*)-aspected))
.* \((?P<x>\d*), (?P<y>\d*) .*
((?P<desc>.*)\n)?Leyline direction: (?P<dir>.*)\
'''

tiledescRegex = '''\
.* \((?P<x>\d*), (?P<y>\d*) .*\)
(.*\n)*?(?P<name>.*): (?P<desc>.*)'''

def convert(planematches, planename, filename):
    with open(filename, 'wb') as file:
        file.write(planeJSON(planematches, planename).encode('utf-8'))
