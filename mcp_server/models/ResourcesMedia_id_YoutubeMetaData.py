# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:29:54+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel

from . import Meta, YoutubeMetadata


class JsonGetResponse(BaseModel):
    callback: Optional[str] = None
    meta: Optional[Meta] = None
    results: Optional[List[YoutubeMetadata]] = None
