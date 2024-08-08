import os
from abc import ABC
import inspect
import importlib.util

def find_scheduled_classes(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                module_path = os.path.join(root, file)
                try:
                    spec = importlib.util.spec_from_file_location("gfg", module_path)
                    #spec = importlib.util.find_spec(module_path[:-3])
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                except ImportError:
                    continue
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if hasattr(obj, '__annotations__') and 'hello_decorator' in obj.__annotations__:
                        print(f"Found class {obj.__name__} decorated with @Scheduled in {module_path}")
