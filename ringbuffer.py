#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        self.MAX_CAP = capacity
        self._front = 0
        self._rear =  0
        self.buffer = [None] * capacity
        self._size = 0

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        return self._size

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        if (self.size() == 0):
            return True
        else:
            return False
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        if (self.size() == self.MAX_CAP):
            return True
        else:
            return False

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        if (self.is_full()):
            raise RingBufferFull("RingBuffer is currently full!")
        else:
            self.buffer[self._rear] = x

        self._rear = (self._rear + 1) % self.MAX_CAP
        self._size += 1

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if (self.is_empty()):
            raise RingBufferEmpty("RingBuffer is empty!")
        else:
            item = self.buffer[self._front]
            self._front = (self._front + 1) % self.MAX_CAP
            self._size -= 1
            return item
        
    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        if (self.is_empty()):
            raise RingBufferEmpty("RingBuffer is empty!")
        else:
            return self.buffer[self._front]
            
class RingBufferFull(Exception):
    '''
    The exception raised when the ring buffer is full when attempting to
    enqueue.
    '''
    pass

class RingBufferEmpty(Exception):
    '''
    The exception raised when the ring buffer is empty when attempting to
    dequeue or peek.
    '''   
    pass
