from collections import OrderedDict
import json

rangeName = [ '无', '短', '中', '长', '超长' ]

simpleTypes = [ '', '航空母舰', '轻型航空母舰', '装甲航母', '战列舰', '航空战列舰', '战列巡洋舰', '重巡洋舰', \
        'CAV', '重雷装巡洋舰', '轻巡洋舰', '浅水重炮舰', '驱逐舰', 'SSV', '潜艇', '重炮潜艇', '补给舰' ]

def typeName(t):
    if t < len(simpleTypes):
        return simpleTypes[t]
    else:
        return '航空战列舰'

def run():
    ret = 'ships = { }\n\n'
    #fleets = json.load(open('fleets.json'), object_pairs_hook = OrderedDict)
    ships = json.load(open('ships.json'), object_pairs_hook = OrderedDict)

    for id_, ship in ships.items():
        ret += "ships['%s'] = {\n    " % id_
        ret += "title='%s', " % ship['title']
        ret += "rarity=%d, " % ship['rarity']
        ret += "image=%d, " % ship['image']
        ret += "type='%s',\n    " % typeName(ship['type'])
        ret += "level=%d, " % ship['level']
        ret += "hp=%d, " % ship['hp']
        ret += "atk=%d, " % ship['atk']
        ret += "tpd=%d, " % ship['tpd']
        ret += "def=%d, " % ship['def']
        ret += "aa=%d, " % ship['aa']
        ret += "eva=%d, " % ship['eva']
        ret += "as=%d, " % ship['as']
        ret += "rec=%d, " % ship['rec']
        ret += "speed=%d, " % ship['speed']
        ret += "range='%s',\n    " % rangeName[ship['range']]
        ret += "eq1='%s', " % ship['eq'][0]
        ret += "eq2='%s', " % ship['eq'][1]
        ret += "eq3='%s', " % ship['eq'][2]
        ret += "eq4='%s', " % ship['eq'][3]
        ret += "cap1=%d, " % ship['cap'][0]
        ret += "cap2=%d, " % ship['cap'][1]
        ret += "cap3=%d, " % ship['cap'][2]
        ret += "cap4=%d\n}\n\n" % ship['cap'][3]

    ret += 'return ships'
    return ret

if __name__ == '__main__':
    open('enemy.lua', 'w').write(run())
