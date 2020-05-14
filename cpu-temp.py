#!/usr/bin/env python3.7

import asyncio
import iterm2
import os
from subprocess import check_output
def GetTemp():
     output = check_output(["/usr/local/bin/osx-cpu-temp"])
     return output.decode("utf-8").rstrip('\n') 

async def main(connection):
    app = await iterm2.async_get_app(connection)

    component = iterm2.StatusBarComponent(
        short_description="Temp CPU",
        detailed_description="Shows the temperature of the CPU",
        knobs=[],
        exemplar="🌡 " + GetTemp(),
        update_cadence=10,
        identifier="com.iterm2.example.cpu-temp")

    # This function gets called once per second.
    @iterm2.StatusBarRPC
    async def coro(knobs, cputemp=iterm2.Reference("iterm2.user.cputemp?")):
        return "🌡" + GetTemp()

    # Register the component.
    await component.async_register(connection, coro)

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)
