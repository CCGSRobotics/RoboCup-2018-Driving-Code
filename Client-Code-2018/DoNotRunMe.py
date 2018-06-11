print('1. Flipper Bot')
print('2. Emu Bot')
print('enter the number of the robot you wish to drive: ')
robot = input('')


if robot == 1:
    import CurrentFlipperCode.client as cl

elif robot == 2:
    import CurrentEmuBotCode.client as cl
