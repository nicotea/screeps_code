from defs import *
from itertools import permutations

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

extension_plan_v1 = [
    (1, 2), (1, -2), (-1, 2), (-1, -2), 
    (2, 1), (2, -1), (-2, 1), (-2, -1), 
    (1, 4), (1, -4), (-1, 4), (-1, -4), 
    (4, 1), (4, -1), (-4, 1), (-4, -1), 
    (2, 3), (2, -3), (-2, 3), (-2, -3), 
    (3, 2), (3, -2), (-3, 2), (-3, -2), 
    (1, 6), (1, -6), (-1, 6), (-1, -6), 
    (6, 1), (6, -1), (-6, 1), (-6, -1), 
    (2, 5), (2, -5), (-2, 5), (-2, -5), 
    (5, 2), (5, -2), (-5, 2), (-5, -2), 
    (3, 4), (3, -4), (-3, 4), (-3, -4), 
    (4, 3), (4, -3), (-4, 3), (-4, -3)
]

def build_extension():
    # if there are less than the max number of allowed extensions, build one else do nothing
    for name in Object.keys(Game.spawns):
        room = Game.spawns[name].room
        level_controller = room.controller.level
        nr_of_extensions = _.sum(Game.structure, lambda c: c.pos.roomName == room.roomName and c.structureType == STRUCTURE_EXTENSION)
        if nr_of_extensions < CONTROLLER_STRUCTURES[STRUCTURE_EXTENSION][level_controller]:
            for pos in extension_plan_v1:
                if room.createConstructionSite(Game.spawns[name].pos.x + pos[0], Game.spawns[name].pos.y + pos[1], STRUCTURE_EXTENSION) == OK:
                    break
                else:
                    pass