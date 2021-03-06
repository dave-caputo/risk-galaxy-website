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


class SlidePage(Page):
    CL = 'cl'
    CR = 'cr'
    FL = 'fl'
    FR = 'fr'

    ALIGN_CHOICES = [
        (CL, 'center-left'),
        (CR, 'center-right'),
        (FL, 'full-left'),
        (FR, 'full-right')
    ]

    body = RichTextField(blank=True)
    summary = RichTextField(blank=True)
    align = models.CharField(max_length=2,
                             choices=ALIGN_CHOICES,
                             default=CL)

    content_panels = Page.content_panels + [
        FieldPanel('align'),
        FieldPanel('body', classname='full'),
        FieldPanel('summary', classname='full'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    parent_page_types = ['sections.SectionPage']


class SlidePageGalleryImage(Orderable):
    page = ParentalKey(SlidePage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
