from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel

from home.models import HomePage


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

    content_panels = Page.content_panels + [
        FieldPanel('align'),
        FieldPanel('body', classname='full'),
        InlinePanel('gallery_images', label="Gallery images"),
        InlinePanel('section_slides', label="Section slides"),
    ]

    parent_page_types = ['home.HomePage']


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


class SectionPageSlides(Orderable):
    section = ParentalKey(SectionPage, on_delete=models.CASCADE,
                          related_name='section_slides')

    slide = models.ForeignKey(
        'slides.SlidePage', on_delete=models.CASCADE, related_name='+'
    )

    content_panels = [
        PageChooserPanel('slide')
    ]
