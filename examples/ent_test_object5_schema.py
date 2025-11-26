from entpy import Field, Schema, StringField, Action, AllowAll, PrivacyRule


class EntTestObject5Schema(Schema):
    def get_fields(self) -> list[Field]:
        return [
            StringField("obj5_field", 100).not_null().example("blah!"),
        ]

    def get_privacy_rules(self, action: Action) -> list[PrivacyRule]:
        return [AllowAll()]
