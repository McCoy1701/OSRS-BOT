from tasks.woodCutting import powerWoodcutting
# from tasks.mining import powerMiner
# from tasks.combat import powerAttack
# from tasks.fishing import powerFisher
from utils.window import setWindow



def main():
    setWindow('RuneLite')
    # powerFisher('salmon', 2)
    powerWoodcutting(1, 'willow')
    # powerAttack('cow')
    # powerMiner(3, True, 7)
    # screenshotColor()


if __name__ == '__main__':
    main()
