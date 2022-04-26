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

    # If the creep is not in build mode, find a source to harvest
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
            creep.moveTo(source, {'visualizePathStyle': {'stroke': '#ffaa00'}})
    else:
        # If we have a saved target, use it
        if creep.memory.target:
            target = Game.getObjectById(creep.memory.target)
        else:
            # Get a random new target.
            target = _(creep.room.find(FIND_CONSTRUCTION_SITES)).filter(lambda cs: cs.progress > 0).sample()
            console.log(target.id)
            if target == undefined:
                target = _(creep.room.find(FIND_CONSTRUCTION_SITES)).sample()
                # if there are no more construction sites at all, the creep becomes a harvester
                if target == undefined:
                    creep.memory.role = 'harvester'
            creep.memory.target = target.id

        # if in range of target, then build otherwise move towards it
        if creep.pos.inRangeTo(target, 3):
            result = creep.build(target)
            if not result == OK:
                print("[{}] Unknown result from creep.build({}): {}".format(
                    creep.name, target, result))
        else:
            creep.moveTo(target, {'visualizePathStyle': {'stroke': '#ffffff'}})