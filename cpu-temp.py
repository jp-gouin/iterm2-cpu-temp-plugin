#!/usr/bin/env python3.7

import iterm2
import re
from subprocess import check_output

def GetTemp():
    return check_output(["/usr/local/bin/osx-cpu-temp"]).decode("utf-8").rstrip('\n')

def GetFan():
    fans = re.findall(r"(\d{1,4}) RPM", check_output(["/usr/local/bin/osx-cpu-temp", "-f"]).decode("utf-8").replace("\n", " "))
    # On Catalina , the fan speed is not yet managed by "/usr/local/bin/osx-cpu-temp" see https://github.com/lavoiesl/osx-cpu-temp/issues/28
    if len(fans) >= 1 :
        avg = int(sum(map(int, fans)) / len(fans))
        return str(avg) + " RPM"
    else :
        return "Unknown"

async def main(connection):
    await iterm2.async_get_app(connection)

    icon2x = iterm2.StatusBarComponent.Icon(2, "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")
    icon1x = iterm2.StatusBarComponent.Icon(1, "iVBORw0KGgoAAAANSUhEUgAAABAAAAARCAYAAADUryzEAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAlmVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSATEAAgAAABEAAABah2kABAAAAAEAAABsAAAAAAAAAGAAAAABAAAAYAAAAAF3d3cuaW5rc2NhcGUub3JnAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAEKADAAQAAAABAAAAEQAAAAAWaVyHAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAComlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx4bXA6Q3JlYXRvclRvb2w+d3d3Lmlua3NjYXBlLm9yZzwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjE3PC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjE2PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CvGU6sAAAAEcSURBVDgRrZK7agJBFIZX10saRRC0sAmkTZXa1sYiraWCD+Fj5FFSWfoAEru8gY0QQtDCEJKgfr87J2x2ZsDCA9+enXP5Z87spkncSqTK8fSVMmlARzvLHmAEG/iEBvzCEf4sJKBkCyYwhyH04BbeQGK2iTejJboUreEVtGsHZN6deIGsLjngTUxH/nEo/s9iAiqqu8oqXnUV5104czEBHXsKLzCAD9Du3gmkGrJvgnfQhBXs4CIBza2Z287jkhvQJSpXg6jZpWnmZ5CQffdZrsvqcqHs1f6JPss95AXeWUvYaw5dopq/QCYR2Rb0KW2tWNBM8Imsio2xq/ZOUAxobbs88n4PC1jCxVYUVWModhaMJsjaODbGuaH4OAEUkzSDoz1zAAAAAABJRU5ErkJggg==")

    component = iterm2.StatusBarComponent(
        short_description="Temp CPU",
        detailed_description="Shows the temperature of the CPU",
        knobs=[],
        exemplar=GetTemp(),
        update_cadence=10,
        identifier="com.iterm2.example.cpu-temp",
        icons=[icon1x,icon2x])

    # This function gets called once per second.
    @iterm2.StatusBarRPC
    async def coro(knobs, cputemp=iterm2.Reference("iterm2.user.cputemp?")):
        return GetTemp() + "    ☢  " + GetFan()

    # Register the component.
    await component.async_register(connection, coro)

# This instructs the script to run the "main" coroutine and to keep
# running even after it returns.
iterm2.run_forever(main)

