from src.utils.window import setWindow, mouseClickImage
from src.tasks.woodCutting import powerWoodcutting
from src.tasks.combat import powerAttack
from src.tasks.gatherPickaxe import gatherPickaxes
from src.tasks.smithing import smithItems
from src.tasks.trader import threadTrader, eyeTrader
# from src.tasks.mining import powerMiner
# from src.tasks.fishing import powerFisher


def main():
    setWindow('RuneLite')
    # moveToWithVar(437, 198, 5, True)
    # smithItems(4, 1)
    # threadTrader()
    # eyeTrader()
    # gatherPickaxes()
    # powerWoodcutting(1, 'log')
    # powerAttack('cow')
    # powerFisher('salmon', 2)
    # powerMiner(3, True, 7)


if __name__ == '__main__':
    main()
