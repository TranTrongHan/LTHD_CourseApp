# Generated by Django 5.1.6 on 2025-02-20 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_tag_rename_subject_course_name_lesson_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='image',
        ),
    ]
