#!/usr/bin/env python3
"""Measure the runtime of async comprehensions."""

import asyncio
from time import perf_counter

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel."""
    start = perf_counter()

    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )

    end = perf_counter()
    return end - start
