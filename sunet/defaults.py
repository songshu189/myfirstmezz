from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

register_setting(
    name="RICHTEXT_ALLOWED_STYLES",
    description=_("List of inline CSS styles that won't be stripped from ``RichTextField`` instances."),
    editable=False,
    #default=("margin-top", "margin-bottom", "margin-left", "margin-right",
    #    "float", "vertical-align", "border", "margin", "height", "width"),
    default=("height", "width", ),
    append=True,
)

register_setting(
    name="RICHTEXT_ALLOWED_TAGS",
    description=_("List of HTML tags that won't be stripped from ``RichTextField`` instances."),
    editable=False,
    #default=("margin-top", "margin-bottom", "margin-left", "margin-right",
    #    "float", "vertical-align", "border", "margin", "height", "width"),
    default=("iframe", ),
    append=True,
)
