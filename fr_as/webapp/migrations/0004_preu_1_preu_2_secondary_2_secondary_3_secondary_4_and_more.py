# Generated by Django 4.1 on 2022-09-12 08:12

from django.db import migrations, models
import django.db.models.deletion
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_secondary_1_alter_student_face_photo1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreU_1',
            fields=[
                ('student_face_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.student_face')),
            ],
            bases=('webapp.student_face',),
        ),
        migrations.CreateModel(
            name='PreU_2',
            fields=[
                ('student_face_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.student_face')),
            ],
            bases=('webapp.student_face',),
        ),
        migrations.CreateModel(
            name='Secondary_2',
            fields=[
                ('student_face_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.student_face')),
            ],
            bases=('webapp.student_face',),
        ),
        migrations.CreateModel(
            name='Secondary_3',
            fields=[
                ('student_face_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.student_face')),
            ],
            bases=('webapp.student_face',),
        ),
        migrations.CreateModel(
            name='Secondary_4',
            fields=[
                ('student_face_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webapp.student_face')),
            ],
            bases=('webapp.student_face',),
        ),
        migrations.AlterField(
            model_name='student_face',
            name='photo1',
            field=models.ImageField(upload_to=webapp.models.Rename.save),
        ),
        migrations.AlterField(
            model_name='student_face',
            name='photo2',
            field=models.ImageField(blank=True, upload_to=webapp.models.Rename.save),
        ),
        migrations.AlterField(
            model_name='student_face',
            name='photo3',
            field=models.ImageField(blank=True, upload_to=webapp.models.Rename.save),
        ),
    ]
