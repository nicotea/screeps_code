from defs import *

def run_spawn(spawn):
    
    nr_harvester = _.filter(Game.creeps, lambda creep: creep.memory.role == 'harvester')
    console.log('number of harvester:' + len(nr_harvester))

    nr_hauler = _.filter(Game.creeps, lambda creep: creep.memory.role == 'hauler')
    console.log('number of hauler:' + len(nr_hauler))

    console.log(nr_harvester <= nr_hauler)

    # If nr_harvester <=  2 * nr_hauler, build harvester
    if len(nr_harvester) <= len(nr_hauler / 2) or len(nr_harvester) == 0 :
        # Spawn harvester
        creep_name = 'Harvester' +  Game.time
        spawn.spawnCreep([WORK, WORK, MOVE], creep_name, { 'memory': {'role': 'harvester'}})    


    # Otherwise, build hauler  
    else:
        creep_name = 'Hauler' +  Game.time
        spawn.spawnCreep([CARRY, CARRY, MOVE, MOVE], creep_name, { 'memory': {'role': 'hauler'}})

    # for screeps
    # Game.spawns['Spawn1'].spawnCreep([CARRY, CARRY, MOVE, MOVE], 'Hauler' +  Game.time, { 'memory': {'role': 'hauler'}})

