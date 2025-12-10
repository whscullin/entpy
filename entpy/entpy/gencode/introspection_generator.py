def generate(base_name: str) -> str:
    return f"""def _get_field(field_name: str) -> Field:
        schema = {base_name}Schema()
        fields = schema.get_all_fields()
        field = next(
            filter(
                lambda field: field.name == field_name,
                fields,
            )
        )
        if not field:
            raise ValueError(f"Unknown field: {{field_name}}")
        return field
"""
