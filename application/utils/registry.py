from importlib import import_module
from ..settings import MODULES
import peewee as db
from traceback import print_exc

def configure_models(module):
    for obj in vars(module).values():
        obj: db.Model
        try:
            if hasattr(obj, 'create_table'):
                if (obj.__module__ == module.__name__):
                    obj.create_table(fail_silently=True)
                    print(f"Processing model {obj.__name__}")
        except Exception as e:
            print_exc()

def configure_modules(app):
    print("Configuring modules...")
    for path in MODULES:
        import_module(f'{path}.admin')
        
        blueprint = import_module(f'{path}.controller').blueprint
        app.register_blueprint(blueprint)
        
        models = import_module(f'{path}.models', '*')
        configure_models(models)
