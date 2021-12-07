import inspect

from swagger_client import models as swagger_models


def init_adapter(self, config=None):
    if config is None:
        config = {}
    super(self.__class__, self).__init__(**config)


swagger_models = inspect.getmembers(swagger_models, predicate=inspect.isclass)

for model_name, model_class in swagger_models:
    model = type(model_name, (model_class,), {'__init__': init_adapter})
    globals()[model.__name__] = model

