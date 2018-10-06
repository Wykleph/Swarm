import random
from time import sleep
from datetime import datetime


class ClockControl(object):
    shutdown = False


class Clock(object):
    now = (-1, -1, -1)


class QueueControl(object):
    shutdown = False
    threads = []
    queues = []


class Queue(object):
    def __init__(self):
        self.data = []
        self.alive = False

    def push(self, function, args=None, kwargs=None):
        self.data.append((function, args, kwargs))

    def main(self):
        self.alive = True
        while not QueueControl.shutdown:
            while self.data:
                try:
                    function, args, kwargs = self.data.pop(0)
                    function(*args, **kwargs if kwargs else {})
                except IndexError:
                    continue
        self.alive = False


def chunks(itterable, size):
    output = []

    while itterable:
        rng = itterable[:size]
        output.append(rng)
        del itterable[:size]
    return output


def chunks_fit(l, n):
    """Yield successive n-sized chunks from l."""

    for i in range(0, len(l), n):
        yield l[i:i + n]


def chunks_fit2(itterable, lists):
    ilen = len(itterable)
    slen = int(ilen / lists)

    output = []
    while itterable:
        rng = itterable[:slen]
        output.append(rng)
        del itterable[:slen]
    return output


if __name__ == '__main__':
    pass
