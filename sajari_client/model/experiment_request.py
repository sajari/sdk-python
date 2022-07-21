"""
    Search.io API

    The version of the OpenAPI document: 4.0.0
    Contact: support@search.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from sajari_client.model_utils import (  # noqa: F401
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
    OpenApiModel
)
from sajari_client.exceptions import ApiAttributeError


def lazy_import():
    from sajari_client.model.experiment_request_pipeline import ExperimentRequestPipeline
    from sajari_client.model.pipeline import Pipeline
    from sajari_client.model.promotion import Promotion
    globals()['ExperimentRequestPipeline'] = ExperimentRequestPipeline
    globals()['Pipeline'] = Pipeline
    globals()['Promotion'] = Promotion


class ExperimentRequest(ModelNormal):
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

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'variables': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'custom_pipeline': (Pipeline,),  # noqa: E501
            'pipeline': (ExperimentRequestPipeline,),  # noqa: E501
            'promotions': ([Promotion],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'variables': 'variables',  # noqa: E501
        'custom_pipeline': 'custom_pipeline',  # noqa: E501
        'pipeline': 'pipeline',  # noqa: E501
        'promotions': 'promotions',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, variables, *args, **kwargs):  # noqa: E501
        """ExperimentRequest - a model defined in OpenAPI

        Args:
            variables ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The initial values for the variables the pipeline operates on and transforms throughout its steps.  The most important variable is `q` which is the query the user entered, for example:  ```json { \"q\": \"search terms\" } ```  To paginate through results, set the variables `page` and `resultsPerPage`, for example:  ```json { \"q\": \"search terms\", \"page\": 5, \"resultsPerPage\": 20 } ```  To sort results, set the variable `sort` to the name of one of your collection's schema fields, for example:  ```json { \"q\": \"search terms\", \"sort\": \"name\" } ```  To sort in reverse, prefix the schema field with a minus sign `-`, for example:  ```json { \"q\": \"search terms\", \"sort\": \"-name\" } ```

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
            custom_pipeline (Pipeline): [optional]  # noqa: E501
            pipeline (ExperimentRequestPipeline): [optional]  # noqa: E501
            promotions ([Promotion]): The promotions to consider active when running the search.  Provided promotions override existing promotions with the same ID.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

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

        self.variables = variables
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, variables, *args, **kwargs):  # noqa: E501
        """ExperimentRequest - a model defined in OpenAPI

        Args:
            variables ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): The initial values for the variables the pipeline operates on and transforms throughout its steps.  The most important variable is `q` which is the query the user entered, for example:  ```json { \"q\": \"search terms\" } ```  To paginate through results, set the variables `page` and `resultsPerPage`, for example:  ```json { \"q\": \"search terms\", \"page\": 5, \"resultsPerPage\": 20 } ```  To sort results, set the variable `sort` to the name of one of your collection's schema fields, for example:  ```json { \"q\": \"search terms\", \"sort\": \"name\" } ```  To sort in reverse, prefix the schema field with a minus sign `-`, for example:  ```json { \"q\": \"search terms\", \"sort\": \"-name\" } ```

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
            custom_pipeline (Pipeline): [optional]  # noqa: E501
            pipeline (ExperimentRequestPipeline): [optional]  # noqa: E501
            promotions ([Promotion]): The promotions to consider active when running the search.  Provided promotions override existing promotions with the same ID.. [optional]  # noqa: E501
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

        self.variables = variables
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
