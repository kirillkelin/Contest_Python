import importlib
import sys
from io import StringIO


def force_load(module_name):
    try:
        module = importlib.import_module(module_name)
    except SyntaxError as e:
        print(f"SyntaxError during import: {e}")
        sys.exit(1)

    original_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        exec(open(f"{module_name}.py").read(), module.__dict__)
    except:
        print(f"Error during import: {sys.exc_info()[1]}")
        sys.exit(1)
    finally:
        sys.stdout = original_stdout

    objects = {}

    for item in dir(module):
        if not item.startswith("__"):
            objects[item] = getattr(module, item)

    return objects


m = force_load("broken")
print(m)
