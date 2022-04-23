from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

def run_hauler(creep):

    # !!! need to find a way to not hard code: close_to_ctrl
    ctrl_pos = creep.room.controller.pos
    close_to_ctrl = creep.room.getPositionAt(11, 33)


    # console test
    # console.log("Game.spawns['Spawn1'].store.getFreeCapacity([RESOURCE_ENERGY])" + Game.spawns['Spawn1'].store.getFreeCapacity([RESOURCE_ENERGY]))


    #If we have energy capacity, pick up dropped resources
    if creep.store[RESOURCE_ENERGY] < creep.store.getCapacity():
        target = (creep.room.find(FIND_DROPPED_RESOURCES))
        last_target = target[(len(target) - 1)]


        # !!! Taking the last of the list instead of the first as it will pick back up immediately when it drops its own resource.
        creep.moveTo(last_target)
        creep.pickup(last_target)

    # Otherwise, go to spawn if it is not full        
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


    
    