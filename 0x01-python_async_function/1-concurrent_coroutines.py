#!/usr/bin/env python3
import asyncio
'''an async routine called wait_n that imports the wait_random
coroutine from the previous Python file and takes in two integer
arguments n and max_delay. It spawns the wait_random coroutine
n times with the specified max_delay, and returns the list of
all the delays in ascending order
'''


async def wait_n(n, max_delay):
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
