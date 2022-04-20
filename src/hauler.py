from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run_hauler(creep):
    #If we have energy capacity, pick up dropped resources
    if creep.store[RESOURCE_ENERGY] < creep.store.getCapacity():
        target = (creep.room.find(FIND_DROPPED_RESOURCES))
        console.log('Has free capacity' + len(target))
        creep.moveTo(target[0])
        creep.pickup(target[0])
        # if creep.pickup(target) == ERR_NOT_IN_RANGE:
        #     creep.moveTo(target)
        # else:
        #     creep.pickup(target)

    # Otherwise, go to spawn        
    else:
        creep.moveTo(Game.spawns['Spawn1'])
        creep.transfer(Game.spawns['Spawn1'], RESOURCE_ENERGY)

        console.log('Is full')
    
    