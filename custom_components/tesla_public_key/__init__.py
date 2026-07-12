from __future__ import annotations

import logging
from pathlib import Path

from aiohttp import web

from .public_key import TeslaPublicKeyView

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    """Set up the Tesla Public Key integration."""

    pem_file = (
        Path(hass.config.config_dir)
        / "tesla"
        / "com.tesla.3p.public-key.pem"
    )

    hass.http.register_view(TeslaPublicKeyView(pem_file))

    _LOGGER.info(
        "Tesla Public Key endpoint available at "
        "/.well-known/appspecific/com.tesla.3p.public-key.pem"
    )

    return True