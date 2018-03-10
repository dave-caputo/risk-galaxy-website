from django.db import models

from wagtail.core.models import Page, PageRevision
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]


def new_position():
    return SectionPage.objects.count() + 1


#  TO DO: Move this to field panel form choices if possible.
# def get_position_choices():
#     available_ps = new_position()

#     return [(pos, pos) for pos in range(1, available_ps + 1)]


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
    position = models.IntegerField(default=new_position)

    content_panels = Page.content_panels + [
        FieldPanel('align'),
        FieldPanel('position'),
        FieldPanel('body', classname='full')
    ]

    parent_page_types = [HomePage]

    class Meta:
        ordering = ['position']

    def save(self, *args, shift=True, latest_revision=None, **kwargs):
        '''When updating position, shift the position of other sections.'''

        # commit = kwargs.get('commit', None)
        # print('saving once...')
        # print(f'commit={commit}')

        # for k, v in kwargs.items():
        #     print(f'key={k}, value={v}')

        # for i in args:
        #     print(f'arg={i}')

        if self.live and shift:
            try:
                latest_revision = PageRevision.objects.filter(
                    page=self, page__live=True).order_by('-created_at')[:2][1]
            except Exception:
                latest_revision = []

        if kwargs and latest_revision and shift:

            last_position = latest_revision.as_page_object().position
            new_position = self.position

            # print('saving once...')

            # print(f'Last position={last_position}')
            # print(f'New position={new_position}')

            if new_position < last_position:

                intersect = SectionPage.objects.filter(
                    position__gte=new_position,
                    position__lt=last_position,
                    live=True)

                # print(f'down intersect count={intersect.count()}')

                if intersect:
                    for section in intersect:
                        section.position += 1
                        section.save(shift=False)

            elif new_position > last_position:

                intersect = SectionPage.objects.filter(
                    position__gt=last_position,
                    position__lte=new_position,
                    live=True)

                # print(f'up intersect count={intersect.count()}')

                if intersect:
                    for section in intersect:
                        section.position -= 1
                        section.save(shift=False)

        super().save(*args, **kwargs)
