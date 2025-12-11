from __future__ import annotations

from datetime import time

from entpy.framework.fields.core import (
    Field,
    FieldWithDynamicExample,
    FieldWithExample,
)


class TimeField(Field, FieldWithExample[time], FieldWithDynamicExample[time]):
    def get_python_type(self) -> str:
        return "time"

    def get_example_as_string(self) -> str | None:
        if self._example is None:
            return None
        return (
            f'time.fromisoformat("{self._example.isoformat()}")'
            if self._example is not None
            else None
        )
