from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from wagtail.search import index
from wagtail.api import APIField


class HomePage(Page):
    
    # About Me
    about_me_title = models.CharField(max_length=255, blank=True)
    about_me = RichTextField(default="Write about yourself in here!")
    my_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    # Resume Experience
    resume_experience = StreamField([
        ('resume_experience', blocks.StructBlock([
            ('job_title', blocks.CharBlock()),
            ('job_start_date', blocks.CharBlock()),
            ('job_end_date', blocks.CharBlock()),
            ('job_responsibilities', blocks.RichTextBlock()),
        ])),        
    ], default='')


    # Resume Education
    resume_education = StreamField([
        ('resume_education', blocks.StructBlock([
            ('edu_title', blocks.CharBlock()),
            ('edu_start_date', blocks.CharBlock()),
            ('edu_end_date', blocks.CharBlock()),
            ('edu_responsibilities', blocks.RichTextBlock()),
        ])),        
    ], default='')

    
    # Skills
    skill_discription = models.CharField(max_length=256, null=True)
    skills = StreamField([
        ('skill', blocks.StructBlock([
            ('skill_title', blocks.CharBlock()),
            ('skill_level', blocks.IntegerBlock()),
        ])),        
    ], default='')


    #Recent Projects
    recent_projects = StreamField([
        ('recent_projects', blocks.StructBlock([
            ('project_image', ImageChooserBlock(required=False)),
            ('project_date', blocks.CharBlock()),
            ('project_title', blocks.CharBlock()),
            ('project_github_url', blocks.URLBlock()),
        ])),        
    ], default='')
    
    #Areas Of Interest
    areas_of_interest = StreamField([
        ('areas_of_interest', blocks.StructBlock([
            ('areas_of_interest_title', blocks.CharBlock()),
            ('areas_of_interest_discription', blocks.RichTextBlock()),
        ])),        
    ], default='')

    
    #Social Network
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

    #My Services
    my_services = StreamField([
        ('my_services', blocks.StructBlock([
            ('my_services_title', blocks.CharBlock()),
        ])),        
    ], default='')

    #Contact Address
    address = models.CharField(max_length=256, blank=True)

    #Contact Call Me
    call_me = models.CharField(max_length=256, blank=True)

    #Contact Email Me
    email_me = models.CharField(max_length=256, blank=True)

    #Contact Open Hours
    open_hours = models.CharField(max_length=256, blank=True)

    #Footer About Me
    about_me_footer = RichTextField(default="Write about yourself in here!")


    # Editor panels configuration
    content_panels = Page.content_panels + [
        # About Me
        FieldPanel('about_me_title', classname="full"),
        FieldPanel('about_me', classname="full"),
        ImageChooserPanel('my_image'),

        # Resume Experience
        StreamFieldPanel('resume_experience'),

        # Resume Education
        StreamFieldPanel('resume_education'),

        # Skills skill_discription skills
        FieldPanel('skill_discription', classname="full"),
        StreamFieldPanel('skills'),

        # Recent Projects
        StreamFieldPanel('recent_projects'),

        # Area Of Interest
        StreamFieldPanel('areas_of_interest'),

        #Social Network
        FieldPanel('linkedin'),
        FieldPanel('github'),
        FieldPanel('telegram'),

        # My Services
        StreamFieldPanel('my_services'),

        # Contact Address
        FieldPanel('address', classname="full"),

        # Contact Call Me
        FieldPanel('call_me', classname="full"),

        # Contact Email Me
        FieldPanel('email_me', classname="full"),

        # Contact Open Hours
        FieldPanel('open_hours', classname="full"),

        # Footer About Me
        FieldPanel('about_me_footer', classname="full"), 

    ]


    #Fields On API
    api_fields = [

        # About Me 
        APIField('about_me_title'),
        APIField('about_me'),
        APIField('my_image'),

        # Resume Experience
        APIField('resume_experience'),

        # Resume Education
        APIField('resume_education'),
        
        # Skills
        APIField('skill_discription'),
        APIField('skills'),

        # Recent Projects
        APIField('recent_projects'),

        # Area Of Interest
        APIField('areas_of_interest'),

        #Social Network
        APIField('linkedin'),
        APIField('github'),
        APIField('telegram'),        

        # My Services
        APIField('my_services'),

        # Contact Address
        APIField('address'),

        # Contact Call Me
        APIField('call_me'),

        # Contact Email Me
        APIField('email_me'),

        # Contact Open Hours
        APIField('open_hours'),

        #Footer About Me
        APIField('about_me_footer')
    ]
