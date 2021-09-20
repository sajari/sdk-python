# SchemaFieldType

Type represents the underlying data type of the field.   - TYPE_UNSPECIFIED: Type not specified.  - STRING: String values.  - INTEGER: Integer values (64-bit).  - FLOAT: Floating point values (32-bit).  - DOUBLE: Double floating point values (64-bit).  - BOOLEAN: Boolean values.  - TIMESTAMP: Timestamp values.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Type represents the underlying data type of the field.   - TYPE_UNSPECIFIED: Type not specified.  - STRING: String values.  - INTEGER: Integer values (64-bit).  - FLOAT: Floating point values (32-bit).  - DOUBLE: Double floating point values (64-bit).  - BOOLEAN: Boolean values.  - TIMESTAMP: Timestamp values. | defaults to "TYPE_UNSPECIFIED",  must be one of ["TYPE_UNSPECIFIED", "STRING", "INTEGER", "FLOAT", "DOUBLE", "BOOLEAN", "TIMESTAMP", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


