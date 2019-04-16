import os
import sys

from django.utils.crypto import get_random_string

def get_settings_file_name():
    return get_project_file_name('settings.py')


def get_project_file_name(file_name):
    return os.path.join(project_name, file_name)


def generate_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)


def update_settings_file():
    with open(get_settings_file_name()) as f:
        file_data = f.read()

    for placeholder, value in (
        ('<secret_key>', generate_secret_key()),
        ('<project_name>', project_name),
        ('<app_name>', app_name),
        ('<db_name>', db_name),
        ('<db_user>', db_user),
        ('<db_password>', db_password),
    ):
        file_data = settings_file.replace(placeholder, value)

    with open(get_settings_file_name(), 'w') as f:
        f.write(file_data)


def update_file(file_name, replace_list):
    with open(file_name) as f:
        file_data = f.read()

    for placeholder, value in replace_list:
        file_data = file_data.replace(placeholder, value)

    with open(file_name, 'w') as f:
        f.write(file_data)


if __name__ == '__main__':
    # app_name = input('app name: ')
    app_name = sys.argv[1]
    project_name = app_name + '_project'
    db_name = app_name
    db_user = app_name
    # db_password = input('database password: ')
    db_password = sys.argv[2]
    os.rename('template/static/template', 'template/static/' + app_name)
    os.rename('template/templates/template', 'template/templates/' + app_name)
    os.rename('template', app_name)
    os.rename('template_project', project_name)

    file_names = (
        'manage.py',
        '.gitignore',
        'gulpfile.js',
        'reset_db.sh',
        project_name + '/settings.py',
        project_name + '/urls.py',
        project_name + '/wsgi.py',
        app_name + '/apps.py',
        app_name + '/urls.py',
        app_name + '/views.py',
        app_name + '/templates/' + app_name + '/base.html',
        app_name + '/templates/' + app_name + '/home.html',
    )

    secret_key = generate_secret_key()
    replace_list = (
        ('<secret_key>', secret_key),
        ('<project_name>', project_name),
        ('<app_name>', app_name),
        ('<app_name_title>', app_name.title()),
        ('<db_name>', db_name),
        ('<db_user>', db_user),
        ('<db_password>', db_password),
    )

    for file_name in file_names:
        update_file(file_name, replace_list)
