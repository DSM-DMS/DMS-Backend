import pkgutil

from flask_restful import Api

from app.views import admin, student


class ViewInjector(object):
    def __init__(self, app=None):
        self._global_resources = set()

        if app is not None:
            self.init_app(app)

    def _modules(self, packages):
        modules = set()

        def search(target):
            for loader, name, is_package in pkgutil.iter_modules(target.__path__):
                if is_package:
                    search(loader.find_module(name).load_module(name))
                else:
                    modules.add((loader, name))

        for pkg in packages:
            search(pkg)

        return modules

    def _factory(self, api, packages):
        resources = set()

        for loader, name in self._modules(packages):
            module_ = loader.find_module(name).load_module(name)
            try:
                for res in module_.Resource.__subclasses__():
                    if res not in self._global_resources:
                        resources.add(res)
                        self._global_resources.add(res)
            except AttributeError:
                pass

        for res in resources:
            api.add_resource(res, res.uri)

    def init_app(self, app):
        api = Api(app)
        self._factory(api, [admin, student])
