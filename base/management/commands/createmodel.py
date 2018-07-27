from django.core.management.base import BaseCommand, CommandError
import base
import os
from inflect import engine


class Command(BaseCommand):
    help = 'Creates a model on the given app'
    EXTENDS_MODELS_CLASS_IMPORT = 'from .{app}_base_model import {app_base_model}'
    BASE_MODEL_CLASS_IMPORT = 'from base.models.base_model import BaseModel'
    BASE_MODEL_NAME = 'BaseModel'
    MODEL_IMPORT_ON_INIT_STR = '\nfrom .{model_file_name} import {model_name}'
    MODEL_MANAGER_IMPORT_ON_INIT_STR = '\nfrom .{model_manager_file_name} import {model_manager_name}'
    MODEL_ARGS_DICT = {
        'extended_model_class_module': '',
        'model': '',
        'extended_model': '',
        'model_lowercase_plural': '',
        'model_title': '',
        'model_title_plural': '',
        'id': 'id',
        'app': '',
    }
    BASE_MODEL_MANAGER_NAME = 'BaseModelManager'
    MODEL_MANAGER_ARGS_DICT = {
        'model_manager': '',
        'extended_model_manager': '',
    }

    def _get_model_template_format(self):
        base_path = os.path.dirname(base.__file__)
        model_template_path = os.path.join(
            base_path, 'management/templates/model_template.txt')

        with open(model_template_path, 'r') as model_template:
            model_template_format = model_template.read()
        return model_template_format

    def _get_model_manager_template_format(self):
        base_path = os.path.dirname(base.__file__)
        model_manager_template_path = os.path.join(
            base_path, 'management/templates/model_manager_template.txt')

        with open(model_manager_template_path, 'r') as model_template:
            model_manager_template_format = model_template.read()
        return model_manager_template_format

    def _write_on_file(self, file_path, file_content, mode='w'):
        if not os.path.exists(file_path):
            open(file_path, mode).close()
        with open(file_path, mode) as model_file:
            model_file.write(file_content)
        return True

    def _write_model_file(self, file_path, file_content):
        return self._write_on_file(file_path, file_content)

    def _get_app_and_model_path(self, app, model_file_name):
        app_module = __import__(app)
        app_path = os.path.dirname(app_module.__file__)
        model_path = app_path + "/models/" + model_file_name + '.py'
        return app_path, model_path

    def _get_apps_init_file_path(self, app, folder_name):
        app_module = __import__(app)
        app_path = os.path.dirname(app_module.__file__)
        init_file_path = app_path + '/' + folder_name + '/' + '__init__.py'
        return init_file_path

    def _get_app_base_model_with_module_path(self, app):
        app_title = app.title()
        app_base_model = app_title + 'BaseModel'
        app_models_module = self.EXTENDS_MODELS_CLASS_IMPORT.format(
            app=app, app_base_model=app_base_model)
        return app_base_model, app_models_module

    def _create_model_manager(self,
                              app,
                              app_path,
                              model_name,
                              model_file_name):
        # create managers variables Value
        model_manager_name = model_name + 'Manager'
        model_manger_file_name = model_file_name + '_manager'
        model_manger_file_path = app_path + \
            '/models/managers/' + model_manger_file_name + '.py'
        base_model_manger_name = self.BASE_MODEL_MANAGER_NAME

        # create model managers template
        model_manager_format = self._get_model_manager_template_format()
        managers_formats_value = self.MODEL_MANAGER_ARGS_DICT
        managers_formats_value['model_manager'] = model_manager_name
        managers_formats_value['extended_model_manager'] = base_model_manger_name

        manager_file_content = model_manager_format.format(
            **managers_formats_value)

        # create model manager
        model_manager_created = self._write_on_file(
            file_path=model_manger_file_path, file_content=manager_file_content, mode='w')
        # append the init file
        manger_init_files_folder = 'models/managers'
        manager_init_file_path = self._get_apps_init_file_path(app=app,
                                                               folder_name=manger_init_files_folder)
        manager_init_content = self.MODEL_MANAGER_IMPORT_ON_INIT_STR
        manager_init_file_content = manager_init_content.format(model_manager_file_name=model_manger_file_name,
                                                                model_manager_name=model_manager_name)

        manager_file_appended = self._write_on_file(file_path=manager_init_file_path,
                                                    file_content=manager_init_file_content,
                                                    mode='a+')
        return manager_file_appended and model_manager_created

    def add_arguments(self, parser):
        parser.add_argument('app', type=str)
        parser.add_argument('model', type=str)

    def handle(self, *args, **options):
        app = options['app']
        model = options['model']
        app_base_model, app_models_module = self._get_app_base_model_with_module_path(
            app=app)
        model_name_lowercase = model.lower()
        model_title = model.title()
        model_name = model_title + 'Model' if 'Model' not in model else model
        model_file_name = model_name_lowercase + '_model'
        model_name_plural = engine().plural(model_name_lowercase)
        model_title_plural = engine().plural(model_name_lowercase).title()
        app_path, model_file_path = self._get_app_and_model_path(
            app=app, model_file_name=model_file_name)

        formats_value = self.MODEL_ARGS_DICT
        formats_value['extended_model_class_module'] = self.BASE_MODEL_CLASS_IMPORT
        formats_value['model'] = model_name
        formats_value['extended_model'] = self.BASE_MODEL_NAME
        formats_value['model_lowercase_plural'] = model_name_plural
        formats_value['model_title'] = model_title
        formats_value['model_title_plural'] = model_title_plural
        formats_value['app'] = app

        model_template_format = self._get_model_template_format()
        model_template = model_template_format.format(**formats_value)

        model_is_created = self._write_model_file(
            file_path=model_file_path, file_content=model_template)

        # import the model in models/__init__.py file
        init_file_path = self._get_apps_init_file_path(app=app,
                                                       folder_name='models')
        init_file_str = self.MODEL_IMPORT_ON_INIT_STR.format(model_file_name=model_file_name,
                                                             model_name=model_name)
        init_file_appended = self._write_on_file(
            file_path=init_file_path, file_content=init_file_str, mode='a+')

        # creating the model manager
        model_manager_created = self._create_model_manager(app=app,
                                                           app_path=app_path,
                                                           model_name=model_name,
                                                           model_file_name=model_file_name)
        if model_is_created:
            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully Created Model "%s"' % model_name))
