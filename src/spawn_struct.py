from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run_spawn(spawn):
    if not spawn.spawning:
        # Get the number of our creeps in the room.
        num_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName)
        # If there are no creeps, spawn a creep once energy is at 250 or more
        if num_creeps < 0 and spawn.room.energyAvailable >= 250:
            spawn.createCreep([WORK, CARRY, MOVE, MOVE])
        # If there are less than 15 creeps but at least one, wait until all spawns and extensions are full before
        # spawning.
        elif spawn.room.energyAvailable >= spawn.room.energyCapacityAvailable:
            # Define role of creep to spawn
            harvesters = _.filter(Game.creeps, lambda creep: creep.memory.role == 'harvester')
            builder = _.filter(Game.creeps, lambda creep: creep.memory.role == 'builder')
            role = None
            if len(builder) < 2:
                role = 'builder'
            elif len(harvesters) < 13:
                role = 'harvester'
            # If we have more energy, spawn a bigger creep.
            if role is not None:
                if spawn.room.energyCapacityAvailable >= 350:
                    spawn.createCreep([WORK, CARRY, CARRY, MOVE, MOVE, MOVE], role= role)
                else:
                    spawn.createCreep([WORK, CARRY, MOVE, MOVE], role= role)