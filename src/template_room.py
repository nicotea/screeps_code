from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def build_towers(towers_list, room_name):
    for position in towers_list:
        pos = __new__(RoomPosition(position[0], position[1], room_name))
        if pos.lookFor(LOOK_STRUCTURES) == '':
            pos.createConstructionSite(STRUCTURE_TOWER)

def room_template_build():
    server_towers_list = {
        'W1N7': [(28,26)]
    }

    for room_name, towers_list in _.pairs(server_towers_list):
        build_towers(towers_list, room_name)
