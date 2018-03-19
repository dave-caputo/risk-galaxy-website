from django import forms
from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    motto = models.CharField(max_length=255, default='')
    content_panels = Page.content_panels + [
        FieldPanel('motto'),
        FieldPanel('body', classname='full'),
        InlinePanel('home_sections', label="Home page sections"),
    ]


class HomePageSections(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name='home_sections')

    section = models.ForeignKey(
        'home.SectionPage', on_delete=models.CASCADE, related_name='+'
    )

    content_panels = [
        PageChooserPanel('section')
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
        FieldPanel('body', classname='full'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    parent_page_types = [HomePage]


class SectionPageGalleryImage(Orderable):
    page = ParentalKey(SectionPage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class SlidePage(SectionPage):
    parent_page_types = ['home.SectionPage']
