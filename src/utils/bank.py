from ..utils.support import moveToWithVar, randomBreaks, logMsg


J = 0


def doBanking():
    global J
    logMsg(f'Depositing', True)
    depositAllItems()
    randomBreaks(1, 2)

    logMsg(f'Exited Bank', True)
    exitBank()
    randomBreaks(1, 2)
    logMsg(f'Banked {J + 1} times', True)
    J += 1


def exitBank():
    moveToWithVar(499, 90, False, False, 10, 'left')
    randomBreaks(0.3, 0.7)


def depositSecondItem():
    moveToWithVar(629, 304, False, False, 10, 'left')
    randomBreaks(0.3, 0.7)


def depositAllItems():
    moveToWithVar(456, 380, False, False, 10, 'left')
    randomBreaks(0.3, 0.7)


def pickGold():
    moveToWithVar(294, 171, False, False, 10, 'left')
    randomBreaks(0.5, 0.7)


def pickBucket():
    moveToWithVar(506, 307, False, False, 10, 'left')
    randomBreaks(0.5, 1.5)


def pickBronzeBar():
    moveToWithVar(219, 511, False, False, 10, 'left')
    randomBreaks(0.5, 1.5)


def pickIronBar():
    moveToWithVar(269, 516, False, False, 10, 'left')
    randomBreaks(0.5, 1.5)


def pickSteelBar():
    moveToWithVar(317, 517, False, False, 10, 'left')
    randomBreaks(0.5, 1.5)


def pickMithrilBar():
    moveToWithVar(362, 513, False, False, 10, 'left')
    randomBreaks(0.5, 1.5)

