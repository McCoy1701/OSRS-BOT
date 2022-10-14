from utils.window import setWindow
# from tasks.woodCutting import powerWoodcutting
# from tasks.mining import powerMiner
# from tasks.combat import powerAttack
# from tasks.fishing import powerFisher
# from tasks.gatherPickaxe import gatherPickaxes
from tasks.smithing import smithItems
from tasks.rommikTrader import trader


def main():
    setWindow('RuneLite')
    smithItems(4, 1)
    # trader()
    # gatherPickaxes()
    # powerWoodcutting(3, 'willow')
    # powerAttack('cow')
    # powerFisher('salmon', 2)
    # powerMiner(3, True, 7)



if __name__ == '__main__':
    main()
