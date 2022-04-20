from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run_harvester(creep):
    target = creep.room.find(FIND_SOURCES)
    if creep.harvest(target) == ERR_NOT_IN_RANGE:
        creep.moveTo(target)
    
    else:
        creep.harvest(target)


def run_hauler(creep):
    #If we have energy capacity, pick up dropped resources
    # if creep.store.getFreeCapacity[RESOURCE_ENERGY] > 0:
    #     target = (creep.room.find(FIND_DROPPED_RESOURCES))
    #     if creep.pickup(target) == ERR_NOT_IN_RANGE:
    #         creep.moveTo(target)
    #     else:
    #         creep.pickup(target)
    # Otherwise, go to spawn        
    # else:
        creep.moveTo(Game.spawns['Spawn1'])

