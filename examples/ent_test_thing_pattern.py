from entpy import Field, Pattern, StringField, EnumField, FieldValidator
from enum import Enum
import re


class ThingStatus(Enum):
    GOOD = "GOOD"
    BAD = "BAD"


class MyValidator(FieldValidator[str | None]):
    def validate(self, value: str | None) -> bool:
        if value is None:
            return True
        if len(value) < 1 or len(value) > 100:
            return False
        return bool(re.match(r"^[a-z0-9-]+$", value))


class EntTestThingPattern(Pattern):
    def get_fields(self) -> list[Field]:
        return [
            StringField("a_good_thing", 100).not_null().example("A sunny day"),
            EnumField("thing_status", ThingStatus),
            StringField("a_pattern_validated_field", 100)
            .example("vdurmont")
            .validators([MyValidator()]),
        ]
