from entpy import Action, AllowAll, BoolField, Field, PrivacyRule, Schema, StringField


class EntTestObject5Schema(Schema):
    def get_fields(self) -> list[Field]:
        return [
            StringField("obj5_field", 100).not_null().example("blah!"),
            BoolField("is_it_true").not_null().default(True),
        ]

    def get_privacy_rules(self, action: Action) -> list[PrivacyRule]:
        return [AllowAll()]
