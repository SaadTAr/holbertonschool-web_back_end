#!/usr/bin/env python3
"""Measure runtime for async comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Execute four async comprehensions and measure runtime."""
    start = time.perf_counter()

    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )

    return time.perf_counter() - start
