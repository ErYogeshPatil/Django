# Generated by Django 4.1.3 on 2022-11-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0006_alter_product_discount_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=50)),
                ('U_Email', models.CharField(max_length=50)),
                ('U_Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='emp_details',
            old_name='U_Email',
            new_name='E_Name',
        ),
        migrations.RenameField(
            model_name='emp_details',
            old_name='U_Password',
            new_name='E_Password',
        ),
        migrations.RenameField(
            model_name='emp_details',
            old_name='User_Name',
            new_name='E_Role',
        ),
    ]
