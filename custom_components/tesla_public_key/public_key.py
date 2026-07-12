from __future__ import annotations

from pathlib import Path

from aiohttp import web

from homeassistant.components.http import HomeAssistantView


class TeslaPublicKeyView(HomeAssistantView):
    """Serve Tesla public key."""

    url = "/.well-known/appspecific/com.tesla.3p.public-key.pem"
    name = "tesla_public_key"
    requires_auth = False

    def __init__(self, pem_path: Path):
        self._pem_path = pem_path

    async def get(self, request):
        if not self._pem_path.exists():
            return web.Response(
                status=404,
                text="Public key not found",
                content_type="text/plain",
            )

        return web.FileResponse(
            path=self._pem_path,
            headers={
                "Content-Type": "application/x-pem-file",
                "Cache-Control": "public, max-age=3600",
            },
        )