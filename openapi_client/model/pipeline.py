"""
    Sajari API

    Sajari is a smart, highly-configurable, real-time search service that enables thousands of businesses worldwide to provide amazing search experiences on their websites, stores, and applications.  # noqa: E501

    The version of the OpenAPI document: v4
    Contact: support@sajari.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.pipeline_step import PipelineStep
    from openapi_client.model.pipeline_type import PipelineType
    globals()['PipelineStep'] = PipelineStep
    globals()['PipelineType'] = PipelineType


class Pipeline(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'type': (PipelineType,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'create_time': (datetime,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'pre_steps': ([PipelineStep],),  # noqa: E501
            'post_steps': ([PipelineStep],),  # noqa: E501
            'collection_default': (bool,),  # noqa: E501
            'default_version': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'name': 'name',  # noqa: E501
        'version': 'version',  # noqa: E501
        'create_time': 'create_time',  # noqa: E501
        'description': 'description',  # noqa: E501
        'pre_steps': 'pre_steps',  # noqa: E501
        'post_steps': 'post_steps',  # noqa: E501
        'collection_default': 'collection_default',  # noqa: E501
        'default_version': 'default_version',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, type, name, version, *args, **kwargs):  # noqa: E501
        """Pipeline - a model defined in OpenAPI

        Args:
            type (PipelineType):
            name (str): The pipeline's name.  Must start with an alphanumeric character followed by one or more alphanumeric, `_`, `-` or `.` characters. Strictly speaking, it must match the regular expression: `^[a-zA-Z0-9][a-zA-Z0-9_\\-\\.]+$`.
            version (str): The pipeline's version.  Must start with an alphanumeric character followed by one or more alphanumeric, `_`, `-` or `.` characters. Strictly speaking, it must match the regular expression: `^[a-zA-Z0-9][a-zA-Z0-9_\\-\\.]+$`.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            create_time (datetime): Output only. Creation time of the pipeline.. [optional]  # noqa: E501
            description (str): Description of the pipeline.. [optional]  # noqa: E501
            pre_steps ([PipelineStep]): Pre-steps are run before an indexing operation or query request is sent to the search index.. [optional]  # noqa: E501
            post_steps ([PipelineStep]): Post-steps are run after an indexing operation or query request has been sent to the search index.  For indexing operations, the post-steps only run when creating new records. They do not run when updating records.  For querying, the post-steps have access to the result-set. This makes it possible to act on the results before sending them back to the caller.. [optional]  # noqa: E501
            collection_default (bool): Output only. Indicates if the pipeline is the collection default pipeline.. [optional]  # noqa: E501
            default_version (bool): Output only. Indicates if the pipeline is the default version.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.type = type
        self.name = name
        self.version = version
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
