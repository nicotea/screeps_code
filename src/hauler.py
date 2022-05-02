from defs import *


__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def drop_to_spawn(creep):
    if Game.spawns['Spawn1'].store.getFreeCapacity([RESOURCE_ENERGY]) != 0:
        creep.moveTo(Game.spawns['Spawn1'])
        creep.transfer(Game.spawns['Spawn1'], RESOURCE_ENERGY)



def run_hauler(creep):

    # !!! need to find a way to not hard code: close_to_ctrl
    ctrl_pos = creep.room.controller.pos
    close_to_ctrl = creep.room.getPositionAt(11, 33)

    # !!!!! Currently stop if this condition is true. Need to find how to create a source_test that is kept for the other condition so we can keep hauling.
    # find target and allocated to memory of creep
    if creep.memory.dropped_res_sourceId == None:
        # source_test = creep.room.source.findInRange(FIND_DROPPED_RESOURCES, 1) // Trying to improve using the range 1 of sources.
        source_test = creep.room.find(FIND_DROPPED_RESOURCES)[0]
        #creep.memory.dropped_res_source = source_test
        creep.memory.dropped_res_sourceId = source_test.id
        source_test = Game.getObjectById(creep.memory.dropped_res_sourceId)

        console.log(2)
        console.log(source_test)

        # creep.memory.dropped_res_source = creep.room.find(FIND_DROPPED_RESOURCES)
    
    if not creep.memory.dropped_res_sourceId == None:
        source_test = Game.getObjectById(creep.memory.dropped_res_sourceId)        
        
        #If we have energy capacity, pick up dropped resources
        if creep.store[RESOURCE_ENERGY] < creep.store.getCapacity():
            #target = (creep.room.find(FIND_DROPPED_RESOURCES))
            # last_target = target[(len(target) - 1)]

            # !!!!!!!!! UNFINISHED
            # dropped_res = creep.room.find(FIND_DROPPED_RESOURCES)
            # sources_list = creep.room.find(FIND_SOURCES)
            # for i in range(0, len(dropped_res)):
            # last_target = dropped_res[i].pos.findInRange(creep.room.find(FIND_SOURCES), 2)
            console.log(3)
            console.log(source_test)

            
            creep.moveTo(source_test)
            creep.pickup(source_test)

        # Otherwise, go to spawn if it is not full      
        # !!! Test: drop_to_spawn(creep) 
        
        # Current correct script       
        elif Game.spawns['Spawn1'].store.getFreeCapacity([RESOURCE_ENERGY]) != 0:
            creep.moveTo(Game.spawns['Spawn1'])
            creep.transfer(Game.spawns['Spawn1'], RESOURCE_ENERGY)
        
        elif not creep.pos.inRangeTo(ctrl_pos, 3):       
            creep.moveTo(ctrl_pos)

        elif creep.pos.inRangeTo(ctrl_pos, 3):
            console.log("drop zone")
            creep.drop(RESOURCE_ENERGY)




            # set controller as target inside the creep's memory
            # creep.memory.target = creep.room.controller



            # # console test
            # console.log("ctrl_pos is: " + ctrl_pos)
            # console.log("close_to_ctrl is: " + close_to_ctrl)
            # console.log("drop_site is: " + drop_site)


        
    
    
