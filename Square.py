import sys
import math
from pyautogui import press, hotkey
import launchpad_py as launchpad
from pygame import time

def main():

    mode = None

    lp = launchpad.Launchpad()

    if lp.Check( 1, "minimk3" ):
        lp = launchpad.LaunchpadMiniMk3()
        if lp.Open( 1, "minimk3" ):
            print("Launchpad Mk3")
            mode = "Mk3"

    elif lp.Check( 1, "launchpad x" ) or lp.Check( 1, "lpx" ):
        lp = launchpad.LaunchpadLPX()
        if lp.Open( 1 ):
            print("Launchpad X")
            mode = "LPX"

    if mode is None:
        print("Bro connect.")
        return

    lp.LedCtrlBpm(240)
    lp.Reset()

    def loop():
#       Purple/pink colors
        colors = {
            0:54,
            1:81,
            2:48,
            3:94,
            4:53,
            5:52,
        }
        while True:
            for c in range(len(colors)):
                for r in range(8):
                    time.wait(100)
                    for x in range(9):
                        for y in range(9):
                            buts = lp.ButtonStateXY()
                            if buts != []:
                                if buts[0] == 6 and buts[1] == 8 and buts[2] == 0:
                                    hotkey('command', ' ')
                                if buts[0] == 7 and buts[1] == 0 and buts[2] == 0:
                                    return
                                if buts[0] == 7 and buts[1] == 8 and buts[2] == 0:
                                    hotkey('command', 'ctrl', 'q')
                                if buts[0] == 8 and buts[1] == 6 and buts[2] == 0:
                                    hotkey('escape')
                                if buts[0] == 8 and buts[1] == 7 and buts[2] == 0:
                                    hotkey('command', 'shift', '4')
                            if max(abs(4-y),abs(4-x)) < r and max(abs(4-y),abs(4-x)) > r-2:
                                lp.LedCtrlPulseXYByCode(x,y,colors[c])
                            else:
                                lp.LedCtrlXYByCode(x,y,3)
                    
    loop()
    
    lp.Reset()
    lp.Close()

    
if __name__ == '__main__':
    main()
