#!/usr/bin/env python3

from ringbuffer import *
import random
from math import ceil

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        self.capacity = ceil(44100/frequency)
       
        self.buffer = RingBuffer(self.capacity)
        self._ticks = 0

        for _ in range (self.capacity):
            self.buffer.enqueue(0)
    
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
        self._ticks = 0

        for _ in range(self.capacity):
            self.buffer.dequeue()
            self.buffer.enqueue(random.uniform(-0.5, 0.5))  # Add white noise

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''  
        firstSample = self.buffer.dequeue()
        secondSample = self.buffer.peek()
        energyAve = ((firstSample+secondSample)/2) * 0.996
        self.buffer.enqueue(energyAve)
        self._ticks += 1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        if self.buffer.is_empty():
            return 0
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self._ticks
    
    def reset(self):
        '''
        Resets the number of ticks when the sound becomes faint
        '''
        # clears the string of any of its content until it is plucked again
        self._ticks = 0
