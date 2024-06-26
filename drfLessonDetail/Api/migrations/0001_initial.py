# Generated by Django 4.2.12 on 2024-05-13 11:42

import Api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_time_all', models.ImageField(blank=True, null=True, upload_to=Api.models.picture_upload_path, verbose_name='圖_時間(全部)')),
                ('task_1_1_1', models.BooleanField(default=False, verbose_name='第 1.1.1 個 任務')),
                ('task_1_1_2', models.BooleanField(default=False, verbose_name='第 1.1.2 個 任務')),
                ('task_1_1_3', models.BooleanField(default=False, verbose_name='第 1.1.3 個 任務')),
                ('task_1_1_4', models.BooleanField(default=False, verbose_name='第 1.1.4 個 任務')),
                ('task_1_1_5', models.BooleanField(default=False, verbose_name='第 1.1.5 個 任務')),
                ('task_1_1_6', models.BooleanField(default=False, verbose_name='第 1.1.6 個 任務')),
                ('task_1_1_7', models.BooleanField(default=False, verbose_name='第 1.1.7 個 任務')),
                ('task_1_1_8', models.BooleanField(default=False, verbose_name='第 1.1.8 個 任務')),
                ('task_1_1_9', models.BooleanField(default=False, verbose_name='第 1.1.9 個 任務')),
                ('task_1_1_10', models.BooleanField(default=False, verbose_name='第 1.1.10 個 任務')),
                ('task_1_1_11', models.BooleanField(default=False, verbose_name='第 1.1.11 個 任務')),
                ('task_1_1_12', models.BooleanField(default=False, verbose_name='第 1.1.12 個 任務')),
                ('task_1_1_13', models.BooleanField(default=False, verbose_name='第 1.1.13 個 任務')),
                ('task_1_1_14', models.BooleanField(default=False, verbose_name='第 1.1.14 個 任務')),
                ('task_1_1_15', models.BooleanField(default=False, verbose_name='第 1.1.15 個 任務')),
                ('task_1_2_1_1', models.BooleanField(default=False, verbose_name='第 1.2.1.1 個 任務')),
                ('task_1_2_1_2', models.BooleanField(default=False, verbose_name='第 1.2.1.2 個 任務')),
                ('task_1_2_1_3', models.BooleanField(default=False, verbose_name='第 1.2.1.3 個 任務')),
                ('task_1_2_1_4', models.BooleanField(default=False, verbose_name='第 1.2.1.4 個 任務')),
                ('task_1_2_1_5', models.BooleanField(default=False, verbose_name='第 1.2.1.5 個 任務')),
                ('task_1_2_1_6', models.BooleanField(default=False, verbose_name='第 1.2.1.6 個 任務')),
                ('task_1_2_1_7', models.BooleanField(default=False, verbose_name='第 1.2.1.7 個 任務')),
                ('task_1_2_2_1', models.BooleanField(default=False, verbose_name='第 1.2.2.1 個 任務')),
                ('task_1_2_2_2', models.BooleanField(default=False, verbose_name='第 1.2.2.2 個 任務')),
                ('task_1_2_2_3', models.BooleanField(default=False, verbose_name='第 1.2.2.3 個 任務')),
                ('task_1_2_2_4', models.BooleanField(default=False, verbose_name='第 1.2.2.4 個 任務')),
                ('task_1_2_2_5', models.BooleanField(default=False, verbose_name='第 1.2.2.5 個 任務')),
                ('task_1_2_2_6', models.BooleanField(default=False, verbose_name='第 1.2.2.6 個 任務')),
                ('task_1_2_2_7', models.BooleanField(default=False, verbose_name='第 1.2.2.7 個 任務')),
                ('task_1_2_2_8', models.BooleanField(default=False, verbose_name='第 1.2.2.8 個 任務')),
                ('task_1_2_3_1', models.BooleanField(default=False, verbose_name='第 1.2.3.1 個 任務')),
                ('task_1_2_3_2', models.BooleanField(default=False, verbose_name='第 1.2.3.2 個 任務')),
                ('task_1_2_3_3', models.BooleanField(default=False, verbose_name='第 1.2.3.3 個 任務')),
                ('task_1_2_3_4', models.BooleanField(default=False, verbose_name='第 1.2.3.4 個 任務')),
                ('task_1_2_3_5', models.BooleanField(default=False, verbose_name='第 1.2.3.5 個 任務')),
                ('task_1_2_4_1', models.BooleanField(default=False, verbose_name='第 1.2.4.1 個 任務')),
                ('task_1_2_4_2', models.BooleanField(default=False, verbose_name='第 1.2.4.2 個 任務')),
                ('task_1_2_4_3', models.BooleanField(default=False, verbose_name='第 1.2.4.3 個 任務')),
                ('task_1_2_4_4', models.BooleanField(default=False, verbose_name='第 1.2.4.4 個 任務')),
                ('task_1_2_4_5', models.BooleanField(default=False, verbose_name='第 1.2.4.5 個 任務')),
                ('task_1_2_4_6', models.BooleanField(default=False, verbose_name='第 1.2.4.6 個 任務')),
                ('task_1_2_4_7', models.BooleanField(default=False, verbose_name='第 1.2.4.7 個 任務')),
                ('task_1_2_4_8', models.BooleanField(default=False, verbose_name='第 1.2.4.8 個 任務')),
                ('task_1_2_4_9', models.BooleanField(default=False, verbose_name='第 1.2.4.9 個 任務')),
                ('task_1_2_4_10', models.BooleanField(default=False, verbose_name='第 1.2.4.10 個 任務')),
                ('task_1_2_4_11', models.BooleanField(default=False, verbose_name='第 1.2.4.11 個 任務')),
                ('task_1_2_5_1', models.BooleanField(default=False, verbose_name='第 1.2.5.1 個 任務')),
                ('task_1_2_5_2', models.BooleanField(default=False, verbose_name='第 1.2.5.2 個 任務')),
                ('task_1_2_5_3', models.BooleanField(default=False, verbose_name='第 1.2.5.3 個 任務')),
                ('task_1_2_5_4', models.BooleanField(default=False, verbose_name='第 1.2.5.4 個 任務')),
                ('task_1_2_5_5', models.BooleanField(default=False, verbose_name='第 1.2.5.5 個 任務')),
                ('task_1_2_5_6', models.BooleanField(default=False, verbose_name='第 1.2.5.6 個 任務')),
                ('task_1_2_5_7', models.BooleanField(default=False, verbose_name='第 1.2.5.7 個 任務')),
                ('task_2_1', models.BooleanField(default=False, verbose_name='第 2.1 個 任務')),
                ('task_2_2', models.BooleanField(default=False, verbose_name='第 2.2 個 任務')),
                ('task_3_1', models.BooleanField(default=False, verbose_name='第 3.1 個 任務')),
                ('task_3_2', models.BooleanField(default=False, verbose_name='第 3.2 個 任務')),
                ('task_3_3', models.BooleanField(default=False, verbose_name='第 3.3 個 任務')),
                ('task_3_4', models.BooleanField(default=False, verbose_name='第 3.4 個 任務')),
                ('task_3_5', models.BooleanField(default=False, verbose_name='第 3.5 個 任務')),
                ('task_3_6', models.BooleanField(default=False, verbose_name='第 3.6 個 任務')),
                ('task_3_7', models.BooleanField(default=False, verbose_name='第 3.7 個 任務')),
                ('task_6_time', models.DateField(verbose_name='時間')),
                ('task_6_other', models.TextField(blank=True, null=True, verbose_name='第 6 個任務其他')),
                ('task_8', models.ImageField(blank=True, null=True, upload_to=Api.models.stamp_upload_path)),
                ('signature_saler', models.ImageField(blank=True, null=True, upload_to='sign_saler', verbose_name='店員簽名')),
                ('signature_manager', models.ImageField(blank=True, null=True, upload_to='sign_manager', verbose_name='經理簽名')),
                ('signature_owener', models.ImageField(blank=True, null=True, upload_to='sign_owener', verbose_name='經營者簽名')),
                ('stamp', models.ImageField(blank=True, null=True, upload_to=Api.models.stamp_upload_path)),
            ],
            options={
                'db_table': 'BookInfo',
            },
        ),
        migrations.CreateModel(
            name='BookName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booklName', models.TextField(blank=True, null=True, verbose_name='書名')),
            ],
            options={
                'db_table': 'BookName',
            },
        ),
        migrations.CreateModel(
            name='Bookseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookseller', models.TextField(blank=True, null=True, verbose_name='書商')),
            ],
            options={
                'db_table': 'Bookseller',
            },
        ),
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookstore', models.TextField(blank=True, null=True, verbose_name='書店')),
            ],
            options={
                'db_table': 'Bookstore',
            },
        ),
        migrations.CreateModel(
            name='PictureTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=Api.models.picture_upload_path, verbose_name='圖')),
                ('picture_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='上傳圖的時間')),
            ],
            options={
                'db_table': 'PictureTime',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField(blank=True, null=True, verbose_name='地點')),
            ],
            options={
                'db_table': 'Place',
            },
        ),
        migrations.CreateModel(
            name='PrintingManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printingManager', models.TextField(blank=True, null=True, verbose_name='印刷廠商經理')),
            ],
            options={
                'db_table': 'MachineryManager',
            },
        ),
        migrations.CreateModel(
            name='PrintingManufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printingManufacturer', models.TextField(blank=True, null=True, verbose_name='印刷廠商')),
            ],
            options={
                'db_table': 'PrintingManufacturerr',
            },
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishingHouse', models.TextField(blank=True, null=True, verbose_name='出版社')),
            ],
            options={
                'db_table': 'ElectricalCoOrganizer',
            },
        ),
        migrations.CreateModel(
            name='PublishingHouseManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publishingHouseManager', models.TextField(blank=True, null=True, verbose_name='出版社經理')),
            ],
            options={
                'db_table': 'ElectricalManager',
            },
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.ImageField(blank=True, null=True, upload_to=Api.models.signature_upload_path, verbose_name='簽名')),
            ],
            options={
                'db_table': 'Signature',
            },
        ),
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp', models.ImageField(blank=True, null=True, upload_to=Api.models.signature_upload_path, verbose_name='書局大章')),
            ],
            options={
                'db_table': 'Stamp',
            },
        ),
        migrations.CreateModel(
            name='Task5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task5', models.TextField(blank=True, null=True, verbose_name='第 5 個 任務')),
            ],
            options={
                'db_table': 'Task5',
            },
        ),
        migrations.CreateModel(
            name='Task7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task7', models.TextField(blank=True, null=True, verbose_name='第7個任務')),
            ],
            options={
                'db_table': 'Task7',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('action', models.IntegerField(choices=[(1, '新增'), (2, '刪除'), (3, '修改'), (4, '查詢')])),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.bookinfo')),
            ],
            options={
                'db_table': 'Log',
            },
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='bookName_all',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.bookname'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='bookseller_all',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.bookseller'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='task_5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.task5'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='task_6_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.place'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='task_6_printingManager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.printingmanager'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='task_6_printingManufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.printingmanufacturer'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='task_6_publishingHouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.publishinghouse'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='task_6_publishingHouseManager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.publishinghousemanager'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='task_7',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Api.task7'),
        ),
    ]
