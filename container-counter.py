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
        switch_view = 10

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
                stp_num = all_num - run_num
                if all_num <= switch_view:
                    return (whale * run_num) + (stoped * stp_num)
                else:
                    return "{0} x {1}  | {2} x {3}".format(whale,
                                                           str(run_num),
                                                           stoped,
                                                           str(stp_num))
        except Exception:
            return "Cannot connect to docker daemon"

    await component.async_register(connection, container_counter)

iterm2.run_forever(main)
