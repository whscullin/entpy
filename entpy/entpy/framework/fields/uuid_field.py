from __future__ import annotations

from uuid import UUID

from entpy.framework.fields.core import (
    Field,
    FieldWithDynamicExample,
    FieldWithExample,
)


class UuidField(Field, FieldWithExample[UUID], FieldWithDynamicExample[UUID]):
    def get_python_type(self) -> str:
        return "UUID"

    def get_example_as_string(self) -> str | None:
        if self._example is None:
            return None
        return f'UUID("{self._example}")'
