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
                print("key pressed!")
            else:
                pass

        # issue: for some reason for loops in unusable? making the program laggy, and impossible to finish

        # compute the superposition of samples
        sample = 0
        for i in range(20):
            if (strings[i].is_plucked()):
                sample += strings[i].sample()
        
        # play the sample on standard audio
        play_sample(sample)

        # advance the simulation of each guitar string by one step
        # note: if it does tick() for too long, the program would inevitably crash
        # a reset method can help with this error
        for i in range(20):
            if (strings[i].is_plucked()):
                strings[i].tick()
                if (strings[i].time() > 141120): # 3.2 seconds * 44100 sample rate
                    print("key unpressed!")
                    strings[i].reset()

        '''
        time until string is unhearable = 3.2 seconds
        get sample rate
        string x sample rate = 141120
        
        get time ticks is called using time()
        compare value of time() and string x sample rate

        if time() > string x sample rate
        reset ticks 
        '''

