import harvester
import builder
import spawn_struct
import extension_struct
import road_struct
# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.
from defs import *
#import command

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def main():
    """
    Main game logic loop.
    """

    # Run each creep
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        if(creep.memory.role == 'harvester'):
            harvester.run_harvester(creep)
        elif(creep.memory.role == 'builder'):
            builder.run_builder(creep)
        else:
            harvester.run_harvester(creep)

    extension_struct.build_extension()

    # Delete memory of non-existing creeps
    for name in Object.keys(Memory.creeps):
        if not Game.creeps[name]:
            del Memory.creeps[name]
            console.log('Clearing non-existing creep memory:', name)

    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        spawn_struct.run_spawn(spawn)

    road_struct.build_road()

module.exports.loop = main
