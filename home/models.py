from django import forms
from django.db import models

from wagtail.core.models import Page, PageRevision
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]


class SectionPage(Page):
    CL = 'cl'
    CR = 'cr'

    ALIGN_CHOICES = [
        (CL, 'center-left'),
        (CR, 'center-right')
    ]

    body = RichTextField(blank=True)
    align = models.CharField(max_length=2,
                             choices=ALIGN_CHOICES,
                             default=CL)

    position = models.IntegerField()

    content_panels = Page.content_panels + [
        FieldPanel('align'),
        FieldPanel('position'),
        FieldPanel('body', classname='full')
    ]

    parent_page_types = [HomePage]

    class Meta:
        ordering = ['position']


class SlidePage(SectionPage):
    parent_page_types = ['home.SectionPage']
