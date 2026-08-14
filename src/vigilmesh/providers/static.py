"""A deterministic provider for examples, local development, and tests."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

from ..models import Observation


class StaticProvider:
    name = "static"

    def __init__(self, items: Sequence[Mapping[str, Any]]) -> None:
        self._items = tuple(dict(item) for item in items)

    def collect(self, context: Mapping[str, Any]) -> tuple[Observation, ...]:
        return tuple(
            Observation(
                source=str(item.get("source", self.name)),
                content=str(item.get("content", "")),
                attributes={
                    **dict(item.get("attributes", {})),
                    "trigger": context.get("trigger", "manual"),
                },
            )
            for item in self._items
        )
