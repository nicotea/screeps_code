from defs import *

def run_spawn(spawn):
    
    nr_harvester = _.filter(Game.creeps, lambda creep: creep.memory.role == 'harvester')
    console.log('number of harvester: ' + len(nr_harvester))
    nr_hauler = _.filter(Game.creeps, lambda creep: creep.memory.role == 'hauler')
    console.log('number of hauler: ' + len(nr_hauler))
    nr_upgrader = _.filter(Game.creeps, lambda creep: creep.memory.role == 'upgrader')
    console.log('number of upgrader: ' + len(nr_upgrader))


    
    # console test
    # console.log('len(nr_harvester) + len(nr_hauler) <= 5: is ' + (len(nr_harvester) + len(nr_hauler) <= 5))
    # console.log('len(nr_harvester) / 2 <= len(nr_hauler / 3) is: ' + (len(nr_harvester) / 2 <= len(nr_hauler) / 3))
    
    # limit creeps to 5 max
    if len(nr_harvester) + len(nr_hauler) < 5:
        # Keep ration of 2 harvesters for 3 haulers
        if len(nr_harvester) / 2 <= len(nr_hauler) / 3 or len(nr_harvester) == 0:
            # Spawn harvester
            creep_name = 'harvester' +  Game.time
            spawn.spawnCreep([WORK, WORK, MOVE], creep_name, { 'memory': {'role': 'harvester'}})    


        # Otherwise, build hauler  
        else:
            creep_name = 'hauler' +  Game.time
            spawn.spawnCreep([CARRY, CARRY, MOVE, MOVE], creep_name, { 'memory': {'role': 'hauler'}})

    # If less than 2 upgraders        
    elif len(nr_upgrader) < 2:
        creep_name = 'upgrader' +  Game.time
        spawn.spawnCreep([WORK, WORK, CARRY, MOVE], creep_name, { 'memory': {'role': 'upgrader'}})

    else:
        pass

    # for screeps
    # Game.spawns['Spawn1'].spawnCreep([CARRY, CARRY, MOVE, MOVE], 'Hauler' +  Game.time, { 'memory': {'role': 'hauler'}})

