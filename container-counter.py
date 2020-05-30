#!/usr/bin/env python3

import subprocess
import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Container Counter",
        detailed_description="Show Number of Containers",
        knobs=[],
        exemplar="[Container Counter]",
        update_cadence=30,
        identifier="koh-sh.container-counter"
    )

    @iterm2.StatusBarRPC
    async def container_counter(knobs):
        whale = '🐳 '
        stoped = '⚫ '

        try:
            cmd = subprocess.run(["/usr/local/bin/docker", "container", "ls", "-a"],
                                 encoding='utf-8',
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            if cmd.returncode != 0:
                return "Cannot connect to docker daemon"
            else:
                containers = cmd.stdout.split("\n")[1:-1]
                all_num = len(containers)
                run_num = len([1 for x in containers if x.count("Up ") > 0])
                return (whale * run_num) + (stoped * (all_num - run_num))
        except Exception:
            return "Cannot connect to docker daemon"

    await component.async_register(connection, container_counter)

iterm2.run_forever(main)
