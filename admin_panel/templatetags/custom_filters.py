from django import template

register = template.Library()

@register.filter
def get_field_value(obj, field_name):
    """
    Возвращает значение поля объекта или связанного объекта (например, для ForeignKey).
    """
    try:
        value = getattr(obj, field_name)
        if callable(value):
            value = value()
        return value if value is not None else getattr(obj, f"{field_name}_id", "N/A")
    except AttributeError:
        return getattr(obj, f"{field_name}_id", "N/A")