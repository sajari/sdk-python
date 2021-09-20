# SchemaFieldMode

Mode is an enumeration of modes for a field.   - MODE_UNSPECIFIED: Mode not specified.  - NULLABLE: Nullable fields do not need to be specified.  - REQUIRED: Required fields must be specified and cannot be null.  - UNIQUE: Unique fields must be specified and must be unique.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Mode is an enumeration of modes for a field.   - MODE_UNSPECIFIED: Mode not specified.  - NULLABLE: Nullable fields do not need to be specified.  - REQUIRED: Required fields must be specified and cannot be null.  - UNIQUE: Unique fields must be specified and must be unique. | defaults to "MODE_UNSPECIFIED",  must be one of ["MODE_UNSPECIFIED", "NULLABLE", "REQUIRED", "UNIQUE", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


