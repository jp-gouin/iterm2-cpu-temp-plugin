#!/usr/bin/env python3.7

import iterm2
import re
from subprocess import check_output

def GetTemp():
    return check_output(["/usr/local/bin/smctemp","-c"]).decode("utf-8").rstrip('\n')

async def main(connection):
    await iterm2.async_get_app(connection)

    icon1x = iterm2.StatusBarComponent.Icon(1, "iVBORw0KGgoAAAANSUhEUgAAABAAAAARCAYAAADUryzEAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAlmVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSATEAAgAAABEAAABah2kABAAAAAEAAABsAAAAAAAAAGAAAAABAAAAYAAAAAF3d3cuaW5rc2NhcGUub3JnAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAEKADAAQAAAABAAAAEQAAAAAWaVyHAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAComlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx4bXA6Q3JlYXRvclRvb2w+d3d3Lmlua3NjYXBlLm9yZzwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjE3PC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjE2PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CvGU6sAAAAEcSURBVDgRrZK7agJBFIZX10saRRC0sAmkTZXa1sYiraWCD+Fj5FFSWfoAEru8gY0QQtDCEJKgfr87J2x2ZsDCA9+enXP5Z87spkncSqTK8fSVMmlARzvLHmAEG/iEBvzCEf4sJKBkCyYwhyH04BbeQGK2iTejJboUreEVtGsHZN6deIGsLjngTUxH/nEo/s9iAiqqu8oqXnUV5104czEBHXsKLzCAD9Du3gmkGrJvgnfQhBXs4CIBza2Z287jkhvQJSpXg6jZpWnmZ5CQffdZrsvqcqHs1f6JPss95AXeWUvYaw5dopq/QCYR2Rb0KW2tWNBM8Imsio2xq/ZOUAxobbs88n4PC1jCxVYUVWModhaMJsjaODbGuaH4OAEUkzSDoz1zAAAAAABJRU5ErkJggg==")

    component = iterm2.StatusBarComponent(
        short_description="Temp CPU",
        detailed_description="Shows the temperature of the CPU",
        knobs=[],
        exemplar=GetTemp(),
        update_cadence=10,
        identifier="com.iterm2.example.cpu-temp",
        icons=[icon1x])

    # This function gets called once per second.
    @iterm2.StatusBarRPC
    async def coro(knobs, cputemp=iterm2.Reference("iterm2.user.cputemp?")):
        return GetTemp() + "°C"

    # Register the component.
    await component.async_register(connection, coro)

# This instructs the script to run the "main" coroutine and to keep
# running even after it returns.
iterm2.run_forever(main)

