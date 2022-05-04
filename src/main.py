import harvester
import builder
import spawn_struct
from template_room import room_template_build
from extension_struct import build_extension
from road_struct import build_road
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

def run_creeps():
    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        if(creep.memory.role == 'harvester'):
            harvester.run_harvester(creep)
        elif(creep.memory.role == 'builder'):
            builder.run_builder(creep)
        else:
            harvester.run_harvester(creep)

def clear_memory():
    # Delete memory of non-existing creeps
    for name in Object.keys(Memory.creeps):
        if not Game.creeps[name]:
            del Memory.creeps[name]
            console.log('Clearing non-existing creep memory:', name)

def run_spawns():
    # Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        spawn_struct.run_spawn(spawn)

def test_code():
    pos = __new__(RoomPosition(28, 26,'W1N7'))
    if pos.lookFor(LOOK_STRUCTURES) == '':
        console.log("Ca marche, ya rien!")
    pos = __new__(RoomPosition(34, 25,'W1N7'))
    if pos.lookFor(LOOK_STRUCTURES) != []:
        console.log("Ca marche, ya quelque chose!")

def main():
    """
    Main game logic loop.
    """
    # Run creeps logic
    run_creeps()

    # Delete memory of non-existing creeps
    clear_memory()

    # Build extensions if necessary
    build_extension()

    # Run each spawn
    run_spawns()

    # Build roads construction site when necessary
    build_road()

    # Build custom template for rooms
    room_template_build()

module.exports.loop = main
