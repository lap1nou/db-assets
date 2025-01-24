import pytest

from dbassets.tui.db_hosts.db_hosts import DbHostsApp
from dbassets.db_api.hosts import get_hosts
from common_tui import (
    IP_TEST_VALUE,
    HOSTNAME_TEST_VALUE,
    ROLE_TEST_VALUE,
    select_input_and_enter_text,
)
from pykeepass import PyKeePass
from typing import Any


@pytest.mark.asyncio
async def test_delete_host_tui(
    open_keepass: PyKeePass, load_mock_config: dict[str, Any]
):
    config = load_mock_config
    kp = open_keepass
    app = DbHostsApp(config, kp)

    async with app.run_test() as pilot:
        await pilot.press("f3")
        await select_input_and_enter_text(pilot, "#ip", IP_TEST_VALUE)
        await pilot.click("#confirm_add")

        hosts = get_hosts(kp)

        assert hosts == [(IP_TEST_VALUE, "", "")]

        await pilot.press("f4")
        await pilot.click("#confirm")

        hosts = get_hosts(kp)

        assert len(hosts) == 0


@pytest.mark.asyncio
async def test_delete_host_full_tui(
    open_keepass: PyKeePass, load_mock_config: dict[str, Any]
):
    config = load_mock_config
    kp = open_keepass
    app = DbHostsApp(config, kp)

    async with app.run_test() as pilot:
        await pilot.press("f3")
        await select_input_and_enter_text(pilot, "#ip", IP_TEST_VALUE)
        await select_input_and_enter_text(pilot, "#hostname", HOSTNAME_TEST_VALUE)
        await select_input_and_enter_text(pilot, "#role", ROLE_TEST_VALUE)
        await pilot.click("#confirm_add")

        hosts = get_hosts(kp)

        assert hosts == [(IP_TEST_VALUE, HOSTNAME_TEST_VALUE, ROLE_TEST_VALUE)]

        await pilot.press("f4")
        await pilot.click("#confirm")

        hosts = get_hosts(kp)

        assert len(hosts) == 0


@pytest.mark.asyncio
async def test_delete_host_not_exist_tui(
    open_keepass: PyKeePass, load_mock_config: dict[str, Any]
):
    config = load_mock_config
    kp = open_keepass
    app = DbHostsApp(config, kp)

    async with app.run_test() as pilot:
        await pilot.press("f4")
        await pilot.click("#confirm")

    hosts = get_hosts(kp)

    assert len(hosts) == 0
