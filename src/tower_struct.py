from defs import *

__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')


def run_individual_tower(tower):
    console.log(tower)

def run_tower():
    towers_list = _(Game.structures).filter(lambda s: s.structureType == STRUCTURE_TOWER)
    console.log(towers_list)
    _.forEach(towers_list, lambda tower: run_individual_tower(tower))
        # if there is an enemy, attack
        # console.log(tower)
        # if tower.room.find(FIND_HOSTILE_CREEPS) == '':
        #     console.log('No enemies')
        # # else, if there is a damaged creeps heal
        # # else, if there is a damaged structure repair
        # # otherwise do nothing
        # pass