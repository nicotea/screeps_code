from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def build_road():
    if not Memory.build_road:
        for room in Object.keys(Game.rooms):
            sources = Game.rooms[room].find(FIND_SOURCES)
            controller = Game.rooms[room].controller
            spawns = room.find(FIND_MY_SPAWNS)
            for i in range(0, len(sources)):
                path = sources[i].pos.findPathTo(controller.pos, opts = {'ignoreCreeps': True, 'range': 1, 'ignoreRoads': True})
                for j in range(0, len(path)):
                    pos = __new__(RoomPosition(path[j].x, path[j].y, room))
                    if not pos.look(LOOK_STRUCTURES).structure == STRUCTURE_ROAD:
                        pos.createConstructionSite(STRUCTURE_ROAD)
        Memory.build_road = True
    # if Memory.build_road and not Memory.build_road_reset:
    #     Memory.build_road = False
    #     Memory.build_road_reset = True