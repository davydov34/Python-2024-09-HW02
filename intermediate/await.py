from typing import Awaitable
from asyncio import Queue


def intermediate_await(func: Awaitable[int]): ...


queue: Queue[int] = Queue()
queue2: Queue[str] = Queue()


async def async_func() -> int:
    return await queue.get()


async def async_func2() -> str:
    return await queue2.get()


intermediate_await(async_func())
intermediate_await(1) #type: ignore  #expect-type-error
intermediate_await(async_func2) #type: ignore  #expect-type-error