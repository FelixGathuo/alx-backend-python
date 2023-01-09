#!/usr/bin/env python3
import asyncio
import random
'''This coroutine takes a random value between
0 and 10 and sets it as the delay vale
'''


async def wait_random(max_delay=10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
