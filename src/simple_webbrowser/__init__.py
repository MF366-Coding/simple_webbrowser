import importlib.machinery, os

def __join_file_with_cur_dir(file: str):
    """
    __join_file_with_cur_dir is an internal function
    """
    return os.path.join(os.path.dirname(__file__), file)

def __load_module_from_source(module_name: str, source_path: str):
    """
    __load_module_from_source is an internal function
    """
    loader = importlib.machinery.SourceFileLoader(module_name, source_path)
    spec = importlib.util.spec_from_loader(module_name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module

swb = __load_module_from_source("simple_webbrowser", __join_file_with_cur_dir("simple_webbrowser.py"))
