from django.db import models
from wagtail.core import blocks
 
class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text to display",
    )
    class Meta :
        template ="streams/title_block.html",
        icon="edit",
        label="titre",
        help_text="Texte centré à afficher sur la page",