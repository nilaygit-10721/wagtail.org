# Generated by Django 3.2.16 on 2022-12-08 21:24

from django.db import migrations

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks

import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0056_add_logo_block_to_content_page"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "get_started_block",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            "core.GetStartedSnippet", icon="th-list"
                        ),
                    ),
                    (
                        "headline",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(max_length=255)),
                                (
                                    "sub_heading",
                                    wagtail.blocks.TextBlock(required=False),
                                ),
                                ("intro", wagtail.blocks.TextBlock(required=False)),
                                (
                                    "cta",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.CharBlock(
                                                    label="CTA text",
                                                    max_length=255,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "cta_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    label="CTA page", required=False
                                                ),
                                            ),
                                            (
                                                "cta_url",
                                                wagtail.blocks.URLBlock(
                                                    label="CTA URL", required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "icon",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("arrow-alt", "Arrow alt"),
                                            ("arrow-in-circle", "Arrow in circle"),
                                            ("arrow-in-square", "Arrow in square"),
                                            ("arrows", "Arrows"),
                                            ("blog", "Blog"),
                                            ("bread", "Bread"),
                                            ("briefcase", "Briefcase"),
                                            ("building", "Building"),
                                            ("calendar", "Calendar"),
                                            ("code-file", "Code File"),
                                            ("document", "Document"),
                                            ("envelope", "Envelope"),
                                            ("explanation", "Explanation"),
                                            ("eye", "Eye"),
                                            ("flame", "Flame"),
                                            ("friends", "Friends"),
                                            ("github", "Github"),
                                            ("handshake", "Handshake"),
                                            ("heart", "Heart"),
                                            ("history", "History"),
                                            ("id-card", "ID Card"),
                                            ("image", "Image"),
                                            ("knife-fork", "Knife Fork"),
                                            ("leaf", "Leaf"),
                                            ("location-pin", "Location Pin"),
                                            ("map", "Map"),
                                            ("magnifying-glass", "Magnifying Glass"),
                                            ("money", "Money"),
                                            ("moon", "Moon"),
                                            ("one-two-steps", "One Two Steps"),
                                            ("padlock", "Padlock"),
                                            ("paper-plane", "Paper Plane"),
                                            ("paper-stack", "Paper Stack"),
                                            ("pen-checkbox", "Pen Checkbox"),
                                            ("person-in-tie", "Person in Tie"),
                                            ("python", "Python"),
                                            (
                                                "question-mark-circle",
                                                "Question Mark Circle",
                                            ),
                                            ("quotes", "Quotes"),
                                            ("release-cycle", "Release Cycle"),
                                            ("roadmap", "Roadmap"),
                                            ("rocket", "Rocket"),
                                            ("rollback", "Rollback"),
                                            ("slack", "Slack"),
                                            ("speech-bubble", "Speech Bubble"),
                                            ("sun-cloud", "Sun Cloud"),
                                            ("table-tennis", "Table Tennis"),
                                            ("tree", "Tree"),
                                            ("wordpress", "Wordpress"),
                                            ("world", "World"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "dark_background",
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "highlight",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(max_length=100)),
                                (
                                    "description",
                                    wagtail.blocks.TextBlock(required=False),
                                ),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "image_on_right",
                                    wagtail.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    "meta_text",
                                    wagtail.blocks.CharBlock(
                                        max_length=50, required=False
                                    ),
                                ),
                                (
                                    "meta_icon",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("arrow-alt", "Arrow alt"),
                                            ("arrow-in-circle", "Arrow in circle"),
                                            ("arrow-in-square", "Arrow in square"),
                                            ("arrows", "Arrows"),
                                            ("blog", "Blog"),
                                            ("bread", "Bread"),
                                            ("briefcase", "Briefcase"),
                                            ("building", "Building"),
                                            ("calendar", "Calendar"),
                                            ("code-file", "Code File"),
                                            ("document", "Document"),
                                            ("envelope", "Envelope"),
                                            ("explanation", "Explanation"),
                                            ("eye", "Eye"),
                                            ("flame", "Flame"),
                                            ("friends", "Friends"),
                                            ("github", "Github"),
                                            ("handshake", "Handshake"),
                                            ("heart", "Heart"),
                                            ("history", "History"),
                                            ("id-card", "ID Card"),
                                            ("image", "Image"),
                                            ("knife-fork", "Knife Fork"),
                                            ("leaf", "Leaf"),
                                            ("location-pin", "Location Pin"),
                                            ("map", "Map"),
                                            ("magnifying-glass", "Magnifying Glass"),
                                            ("money", "Money"),
                                            ("moon", "Moon"),
                                            ("one-two-steps", "One Two Steps"),
                                            ("padlock", "Padlock"),
                                            ("paper-plane", "Paper Plane"),
                                            ("paper-stack", "Paper Stack"),
                                            ("pen-checkbox", "Pen Checkbox"),
                                            ("person-in-tie", "Person in Tie"),
                                            ("python", "Python"),
                                            (
                                                "question-mark-circle",
                                                "Question Mark Circle",
                                            ),
                                            ("quotes", "Quotes"),
                                            ("release-cycle", "Release Cycle"),
                                            ("roadmap", "Roadmap"),
                                            ("rocket", "Rocket"),
                                            ("rollback", "Rollback"),
                                            ("slack", "Slack"),
                                            ("speech-bubble", "Speech Bubble"),
                                            ("sun-cloud", "Sun Cloud"),
                                            ("table-tennis", "Table Tennis"),
                                            ("tree", "Tree"),
                                            ("wordpress", "Wordpress"),
                                            ("world", "World"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "cta",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.CharBlock(
                                                    label="CTA text",
                                                    max_length=255,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "cta_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    label="CTA page", required=False
                                                ),
                                            ),
                                            (
                                                "cta_url",
                                                wagtail.blocks.URLBlock(
                                                    label="CTA URL", required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "icon_bullets",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "icon_bullets",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "icon",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            ("arrow-alt", "Arrow alt"),
                                                            (
                                                                "arrow-in-circle",
                                                                "Arrow in circle",
                                                            ),
                                                            (
                                                                "arrow-in-square",
                                                                "Arrow in square",
                                                            ),
                                                            ("arrows", "Arrows"),
                                                            ("blog", "Blog"),
                                                            ("bread", "Bread"),
                                                            ("briefcase", "Briefcase"),
                                                            ("building", "Building"),
                                                            ("calendar", "Calendar"),
                                                            ("code-file", "Code File"),
                                                            ("document", "Document"),
                                                            ("envelope", "Envelope"),
                                                            (
                                                                "explanation",
                                                                "Explanation",
                                                            ),
                                                            ("eye", "Eye"),
                                                            ("flame", "Flame"),
                                                            ("friends", "Friends"),
                                                            ("github", "Github"),
                                                            ("handshake", "Handshake"),
                                                            ("heart", "Heart"),
                                                            ("history", "History"),
                                                            ("id-card", "ID Card"),
                                                            ("image", "Image"),
                                                            (
                                                                "knife-fork",
                                                                "Knife Fork",
                                                            ),
                                                            ("leaf", "Leaf"),
                                                            (
                                                                "location-pin",
                                                                "Location Pin",
                                                            ),
                                                            ("map", "Map"),
                                                            (
                                                                "magnifying-glass",
                                                                "Magnifying Glass",
                                                            ),
                                                            ("money", "Money"),
                                                            ("moon", "Moon"),
                                                            (
                                                                "one-two-steps",
                                                                "One Two Steps",
                                                            ),
                                                            ("padlock", "Padlock"),
                                                            (
                                                                "paper-plane",
                                                                "Paper Plane",
                                                            ),
                                                            (
                                                                "paper-stack",
                                                                "Paper Stack",
                                                            ),
                                                            (
                                                                "pen-checkbox",
                                                                "Pen Checkbox",
                                                            ),
                                                            (
                                                                "person-in-tie",
                                                                "Person in Tie",
                                                            ),
                                                            ("python", "Python"),
                                                            (
                                                                "question-mark-circle",
                                                                "Question Mark Circle",
                                                            ),
                                                            ("quotes", "Quotes"),
                                                            (
                                                                "release-cycle",
                                                                "Release Cycle",
                                                            ),
                                                            ("roadmap", "Roadmap"),
                                                            ("rocket", "Rocket"),
                                                            ("rollback", "Rollback"),
                                                            ("slack", "Slack"),
                                                            (
                                                                "speech-bubble",
                                                                "Speech Bubble",
                                                            ),
                                                            ("sun-cloud", "Sun Cloud"),
                                                            (
                                                                "table-tennis",
                                                                "Table Tennis",
                                                            ),
                                                            ("tree", "Tree"),
                                                            ("wordpress", "Wordpress"),
                                                            ("world", "World"),
                                                        ]
                                                    ),
                                                ),
                                                (
                                                    "heading",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=255
                                                    ),
                                                ),
                                                (
                                                    "description",
                                                    wagtail.blocks.RichTextBlock(
                                                        features=[
                                                            "bold",
                                                            "italic",
                                                            "link",
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "cta",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "text",
                                                                wagtail.blocks.CharBlock(
                                                                    label="CTA text",
                                                                    max_length=255,
                                                                    required=False,
                                                                ),
                                                            ),
                                                            (
                                                                "cta_page",
                                                                wagtail.blocks.PageChooserBlock(
                                                                    label="CTA page",
                                                                    required=False,
                                                                ),
                                                            ),
                                                            (
                                                                "cta_url",
                                                                wagtail.blocks.URLBlock(
                                                                    label="CTA URL",
                                                                    required=False,
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ],
                            icon="list-alt",
                        ),
                    ),
                    (
                        "logos",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "logos",
                                    wagtail.blocks.ListBlock(
                                        wagtail.images.blocks.ImageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "multiple_quotes",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.TextBlock(required=True)),
                                (
                                    "quotes",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "quote",
                                                    wagtail.blocks.TextBlock(
                                                        required=True
                                                    ),
                                                ),
                                                (
                                                    "author",
                                                    wagtail.blocks.RichTextBlock(
                                                        features=["link"], required=True
                                                    ),
                                                ),
                                                (
                                                    "author_image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        ),
                                        min_num=2,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "standalone_cta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cta",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.CharBlock(
                                                    label="CTA text",
                                                    max_length=255,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "cta_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    label="CTA page", required=False
                                                ),
                                            ),
                                            (
                                                "cta_url",
                                                wagtail.blocks.URLBlock(
                                                    label="CTA URL", required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.TextBlock(
                                        label="Short description",
                                        max_length=100,
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "teaser",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "page",
                                    wagtail.blocks.PageChooserBlock(
                                        page_type=["blog.BlogPage"], required=False
                                    ),
                                ),
                                (
                                    "url_chooser",
                                    wagtail.blocks.URLBlock(required=False),
                                ),
                                (
                                    "image_for_external_link",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "heading_for_external_link",
                                    wagtail.blocks.TextBlock(required=False),
                                ),
                                (
                                    "subheading_for_ext_link",
                                    wagtail.blocks.TextBlock(
                                        label="Subheading for external link",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video",
                        wagtail.blocks.StructBlock(
                            [
                                ("heading", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "autoplay",
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text="Automatically start and loop the video. Autoplay only works for items in the media library.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "video",
                                    wagtailmedia.blocks.VideoChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "embed",
                                    wagtail.embeds.blocks.EmbedBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
