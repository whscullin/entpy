from __future__ import annotations

from entpy.framework.fields.core import (
    Field,
    FieldWithDynamicExample,
    FieldWithExample,
)


class BoolField(Field, FieldWithExample[bool], FieldWithDynamicExample[bool]):
    def get_python_type(self) -> str:
        return "bool"

    def get_example_as_string(self) -> str | None:
        if self._example is None:
            return None
        return "True" if self._example else "False"
