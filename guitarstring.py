#!/usr/bin/env python3

from ringbuffer import *
import random

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        # TO-DO: implement this
        self.capacity = 44100/frequency
        if (self.capacity != int(self.capacity)): # if capacity is not a whole number
            self.capacity = int(self.capacity) + 1 # round up the value         
        self.buffer = RingBuffer(self.capacity)
        self._ticks = 0
    
    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        # TO-DO: implement this
        self.buffer.enqueue(random.uniform(-0.5,0.5))

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        # TO-DO: implement this
        
        ## steps:
        # deleting the sample at the front of the ring buffer
        # adding to the end of the ring buffer the average of the first two samples multiplied by energy decay factor
        firstSample = self.buffer.dequeue()
        secondSample = self.buffer.peek()
        energyAve = ((firstSample+secondSample)/2) * 0.996
        self.buffer.enqueue(energyAve)
        self._ticks += 1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        # TO-DO: implement this
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        # TO-DO: implement this
        return self._ticks
        
