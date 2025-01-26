""" from django import template


register = template.Library()

@register.filter(name="addclass")
def addclass(value, arg):
    return value.as_widget(attrs={"class": arg})

 """

from django import template

register = template.Library()


@register.filter(name="addclass")
def addclass(value, arg):
    if hasattr(value, "as_widget"):  # Verifica se o valor tem o método 'as_widget'
        attrs = {}
        classes = arg.split(",")
        for cls in classes:
            if "=" in cls:
                key, val = cls.split("=")
                attrs[key] = val
            else:
                attrs["class"] = cls  # Se for apenas uma classe
        return value.as_widget(attrs=attrs)
    return value  # Retorna o valor original se não for um campo do formulário
