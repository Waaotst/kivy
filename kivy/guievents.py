from asyncio.events import AbstractEventLoop
from asyncio.base_events import BaseEventLoop
from asyncio import events
import asyncio
import concurrent
import threading
from asyncio import futures

_MAX_WORKERS = 10


class GuiEventLoop(BaseEventLoop):
    pass
