#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keyboard = "q2we4r5ty7u8i9op-[=]"

    strings = []
    for i in range (20):
        strings.append(GuitarString(440*(1.059463**(i-12))))
    
    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key in keyboard:
                index = keyboard.index(key)
                strings[index].pluck()
                # add strings[index] to the set of currently plucked strings
            else:
                pass


        # compute the superposition of samples
        # only compute for the "plucked strings"
        # can add a diff array to be checked!
        sample = strings[12].sample()
        
        # play the sample on standard audio
        play_sample(sample)

        # advance the simulation of each guitar string by one step
        strings[12].tick()

