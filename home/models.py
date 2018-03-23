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
    motto = models.CharField(max_length=255, blank=True)
    login_url = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('motto'),
        FieldPanel('login_url'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('home_sections', label="Home sections"),
    ]

    parent_page_types = ['wagtailcore.Page']


class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class HomePageSections(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name='home_sections')

    section = models.ForeignKey(
        'sections.SectionPage', on_delete=models.CASCADE, related_name='+'
    )

    content_panels = [
        PageChooserPanel('section')
    ]
