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
    """
    Runs a creep as a generic builder.
    :param creep: The creep to run
    """
    # if(creep.memory.building and creep.store[RESOURCE_ENERGY] == 0):
    #     creep.memory.building = False
    #     creep.say('🔄 harvest')
    
    # if(not creep.memory.building and creep.store.getFreeCapacity() == 0):
    #     creep.memory.building = True
    #     creep.say('🚧 build')
    
    # if(creep.memory.building):
    #     targets_in_progress = creep.room.find(FIND_CONSTRUCTION_SITES, { filter: lambda cs: cs.progress > 0 })
    #     console.log(targets_in_progress)
    #     console.log(targets_in_progress[0])
    #     if len(targets_in_progress) > 0:
    #         targets = targets_in_progress
    #     else:
    #         targets = creep.room.find(FIND_CONSTRUCTION_SITES)
    #     if(targets.length):
    #         if(creep.build(targets[0]) == ERR_NOT_IN_RANGE):
    #             creep.moveTo(targets[0], {'visualizePathStyle': {'stroke': '#ffffff'}})
    # else:
    #     sources = creep.room.find(FIND_SOURCES)
    #     if(creep.harvest(sources[0]) == ERR_NOT_IN_RANGE):
    #         creep.moveTo(sources[0], {'visualizePathStyle': {'stroke': '#ffaa00'}})

    # If we're full, stop filling up and remove the saved source
    if not creep.memory.building and _.sum(creep.carry) >= creep.carryCapacity:
        creep.memory.building = True
        creep.say('🚧 build')
        del creep.memory.source
    # If we're empty, start filling again and remove the saved target
    elif creep.memory.building and creep.carry.energy <= 0:
        creep.memory.building = False
        creep.say('🔄 harvest')
        del creep.memory.target

    if not creep.memory.building:
        # If we have a saved source, use it
        if creep.memory.source:
            source = Game.getObjectById(creep.memory.source)
        else:
            # Get a random new source and save it
            source = _.sample(creep.room.find(FIND_SOURCES))
            creep.memory.source = source.id

        # If we're near the source, harvest it - otherwise, move to it.
        if creep.pos.isNearTo(source):
            result = creep.harvest(source)
            if result != OK:
                print("[{}] Unknown result from creep.harvest({}): {}".format(creep.name, source, result))
        else:
            creep.moveTo(source)
    else:
        # If we have a saved target, use it
        if creep.memory.target:
            target = Game.getObjectById(creep.memory.target)
        else:
            # Get a random new target.
            target = _(creep.room.find(FIND_CONSTRUCTION_SITES)).filter(lambda cs: cs.progress < 0).sample()
            if target is None:
                console.log('Hello')
            elif target is not None:
                console.log('Au revoir')
            target = _(creep.room.find(FIND_CONSTRUCTION_SITES)).sample()
            creep.memory.target = target.id

        # If we are targeting a spawn or extension, we need to be directly next to it - otherwise, we can be 3 away.
        if target.energyCapacity:
            is_close = creep.pos.isNearTo(target)
        else:
            is_close = creep.pos.inRangeTo(target, 3)

        if is_close:
            # If we are targeting a spawn or extension, transfer energy. Otherwise, use upgradeController on it.
            if target.energyCapacity:
                result = creep.build(target)
                if result == OK or result == ERR_FULL:
                    del creep.memory.target
                else:
                    print("[{}] Unknown result from creep.build({}): {}".format(
                        creep.name, target, result))
            # else:
            #     result = creep.upgradeController(target)
            #     if result != OK:
            #         print("[{}] Unknown result from creep.upgradeController({}): {}".format(
            #             creep.name, target, result))
            #     # Let the creeps get a little bit closer than required to the controller, to make room for other creeps.
            #     if not creep.pos.inRangeTo(target, 2):
            #         creep.moveTo(target)
        else:
            creep.moveTo(target)