#!/usr/bin/env python3

import docker
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
            client = docker.from_env()
            all_num = len(client.containers.list(all))
            run_num = len(client.containers.list())
            return (whale * run_num) + (stoped * (all_num - run_num))
        except Exception:
            return "Cannot connect to docker daemon"

    await component.async_register(connection, container_counter)

iterm2.run_forever(main)
