from utils.window import setWindow
from utils.support import moveToWithVar
from tasks.woodCutting import powerWoodcutting
from tasks.combat import powerAttack
from tasks.gatherPickaxe import gatherPickaxes
from tasks.smithing import smithItems
from tasks.trader import threadTrader, eyeTrader
# from tasks.mining import powerMiner
# from tasks.fishing import powerFisher


def main():
    setWindow('RuneLite')
    moveToWithVar(437, 198, 5, True)
    # smithItems(4, 1)
    # threadTrader()
    # eyeTrader()
    # gatherPickaxes()
    # powerWoodcutting(3, 'willow')
    # powerAttack('cow')
    # powerFisher('salmon', 2)
    # powerMiner(3, True, 7)


if __name__ == '__main__':
    main()
