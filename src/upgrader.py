from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run_upgrader(creep):
    target_refill = creep.room.find(FIND_DROPPED_RESOURCES)
    target_upgrade = creep.room.controller

    # Console log testing
    # console.log('target_refill is: ' + target_refill)
    # console.log('target_upgrade is: ' + target_upgrade)
    # console.log('creep.store.getUsedCapacity() == 0 is: ' + (creep.store.getUsedCapacity() == 0))

    if creep.store.getUsedCapacity() == 0:
        creep.moveTo(target_refill[0])
        creep.pickup(target_refill[0])

    else:
        if creep.upgradeController(creep.room.controller) == ERR_NOT_IN_RANGE:
            creep.moveTo(target_upgrade)
        else:
            creep.upgradeController(creep.room.controller)
