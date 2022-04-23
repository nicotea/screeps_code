import harvester
import hauler
import upgrader
import spawn_struct

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

# Update new function


def main():
    """
    Main game logic loop.
    """

    # Run each creep
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        if creep.memory.role == 'harvester':
            harvester.run_harvester(creep)
        elif creep.memory.role == 'hauler':
            hauler.run_hauler(creep)
        elif creep.memory.role == 'upgrader':
            upgrader.run_upgrader(creep)
        else:
            pass


    # Delete memory of non-existant creeps
    for name in Object.keys(Memory.creeps):
        if not Game.creeps[name]:
            del Memory.creeps[name]
            console.log('Clearing non-existing creep memory:', name)

    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        spawn_struct.run_spawn(spawn)

module.exports.loop = main