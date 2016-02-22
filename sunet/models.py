from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText

class InterestPage(Page, RichText):
    """
    An Interest tree page
    """
    add_interest = models.BooleanField(_("Add Interest"), default=False,
                                  help_text=_("Include a list of child links"))
    class Meta:
        verbose_name = _("Interest Page")
        verbose_name_plural = _("Interest Pages")
