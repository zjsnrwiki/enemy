from collections import OrderedDict
import json
import sys
import jsonformat

fleetDb = None
shipDb = None
equiptName = None
shipData = None

label = '__ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def sortDict(d):
    return OrderedDict(sorted(d.items()))

def init():
    global fleetDb, shipDb, equiptName, shipData
    fleetDb = json.load(open('fleets.json'), object_pairs_hook = OrderedDict)
    shipDb = json.load(open('ships.json'), object_pairs_hook = OrderedDict)
    t = json.load(open('static.json'))
    equiptName = t['equiptName']
    shipData = t['shipData']

def formatNode(node):
    n = str(node)
    if len(n) == 5:
        return n[0] + '-' + n[2] + '/' + label[int(n[3:])]
    else:
        return n[:-2] + '/' + label[int(n[-2:])]

def load(filename):
    f = open(filename)
    lastLine = ''
    curNode = None
    for line in f:
        if lastLine.startswith('GET /pve/newNext/'):
            curNode = formatNode(json.loads(line[:-1])['node'])

        elif lastLine.startswith('GET /pve/deal/'):
            node = formatNode(lastLine.split('/')[3])
            data = json.loads(line[:-1])
            if 'warReport' in data:
                save(node, data['warReport'])

        elif lastLine.startswith('GET /pve/spy/'):
            if curNode is None:
                continue
            data = json.loads(line[:-1])
            if 'enemyVO' in data:
                save(curNode, data['enemyVO'])

        elif lastLine.startswith('GET /campaign/challenge/'):
            node = lastLine.split('/')[3]
            node = 'C' + node[0] + '-' + node[2]
            data = json.loads(line[:-1])['warReport']
            save(node, data)

        lastLine = line

def end():
    jsonformat.save(sortDict(fleetDb), 'fleets.json')
    jsonformat.save(sortDict(shipDb), 'ships.json')

def save(node, data):
    fleet = data['enemyFleet']
    ships = data['enemyShips']

    f = OrderedDict()
    f['title'] = fleet['title']
    f['formation'] = int(fleet['formation'])
    f['ships'] = [ int(s['shipCid']) for s in ships ]
    f['shipNames'] = [ s['title'] for s in ships ]

    if node[0] == 'C':
        fleetDb[node] = f
    else:
        if node not in fleetDb:
            fleetDb[node] = { }
        fid = str(fleet['id'])
        if fid not in fleetDb[node]:
            fleetDb[node][fid] = f
            fleetDb[node] = sortDict(fleetDb[node])
        elif fleetDb[node][fid] != f:
            print('!!!!! unmatch fleet data ' + node + ' !!!!!')

    for ship in ships:
        s = OrderedDict()
        data = shipData[str(ship['shipCid'])]
        s['title']  = data['title']
        s['rarity'] = data['rarity']
        s['image']  = data['image']
        if ship['title'] != data['title']:
            print('!!!!! unmatch ship name ' + s['title'] + ' !!!!!')

        s['type']   = int(ship['type'])
        s['level']  = int(ship['level'])
        s['hp']     = int(ship['hp'])
        s['atk']    = int(ship['atk'])
        s['tpd']    = int(ship['torpedo'])
        s['def']    = int(ship['def'])
        s['aa']     = int(ship['airDef'])
        s['eva']    = int(ship['miss'])
        s['as']     = int(ship['antisub'])
        s['rec']    = int(ship['radar'])
        s['speed']  = int(ship['speed'])
        s['range']  = int(ship['range'])

        s['eq'] = [ None, None, None, None ]
        s['cap'] = [ None, None, None, None ]
        for i in range(4):
            s['eq'][i] = equiptName[str(ship['equipment'][i])]
            s['cap'][i] = int(ship['capacitySlotMax'][i])
        id_ = str(ship['shipCid'])
        if id_ not in shipDb:
            shipDb[id_] = s
        elif shipDb[id_] != s:
            print('!!!!! unmatch ship data ' + ship['title'] + '!!!!!')

if __name__ == '__main__':
    init()
    for i in range(1, len(sys.argv)):
        load(sys.argv[i])
    end()
