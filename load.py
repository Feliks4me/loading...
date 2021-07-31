#!/usr/bin/env python3

#clear screen
#print text
#sleep, repeat

import os
import time


def period(key, reps = 3):
    for r in range(reps):
        for i in range(4):
            os.system('clear')
            dot = '.'*i
            print(key,dot)
            time.sleep(0.5)

#example:
# period('Fucking', 3)
