from defs import *

def run_spawn(spawn):
    
    # nr_harvester = _.filter(Game.creeps, Game.creeps.memory.role == 'harvester')
    # console.log(nr_harvester)
    # nr_hauler =
    # If nr_harvester <=  2 * nr_hauler, build harvester

    # Spawn harvester
    creep_name = 'Harvester' +  Game.time
    spawn.spawnCreep([WORK, WORK, MOVE], creep_name, { 'memory': {'role': 'harvester'}})
    # console.log('Spawn:' + creep_name)

    # Otherwise, build hauler  
    # creep_name = 'Hauler' +  Game.time
    # spawn.spawnCreep([CARRY, CARRY, MOVE, MOVE], creep_name, { 'memory': {'role': 'hauler'}})

