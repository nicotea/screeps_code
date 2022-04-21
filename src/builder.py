from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run_builder(creep):
    # if the creep is in building mode and have no more energy, he needs to harvest
    if(creep.memory.building and creep.store[RESOURCE_ENERGY] == 0):
        creep.memory.building = False
        creep.say('🔄 harvest')
    
    # if the creep is harversting and have no more free capacity, he needs to build
    if(not creep.memory.building and creep.store.getFreeCapacity() == 0):
        creep.memory.building = True
        creep.say('🚧 build')

    # if the creep is in build mode, find the first available construction site and build it
    if(creep.memory.building):
        targets = creep.room.find(FIND_CONSTRUCTION_SITES)
        if(targets.length):
            if(creep.build(targets[0]) == ERR_NOT_IN_RANGE):
                creep.moveTo(targets[0], {'visualizePathStyle': {'stroke': '#ffffff'}})
            
    # otherwise, find a source and harvest it
    else:
        sources = creep.room.find(FIND_SOURCES)
        if(creep.harvest(sources[0]) == ERR_NOT_IN_RANGE):
            creep.moveTo(sources[0], {'visualizePathStyle': {'stroke': '#ffaa00'}})