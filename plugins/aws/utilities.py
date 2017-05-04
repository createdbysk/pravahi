class AwsUtilitiesError(Exception):
    def __init__(self, msg, definition):
        full_msg = (
            "Error in pipeline definition: %s\n" % msg)
        super(AwsUtilitiesError, self).__init__(full_msg)
        self.msg = msg
        self.definition = definition


def pipeline_object_to_api_object(pipeline_object):
    """
    GIVEN an object in a data pipeline in the data pipeline definition format
    WHEN pipeline_object_to_api_object() runs
    THEN it returns the equivalent object in the format required by the boto3 api.

    Example input:
    {
        "type": "type",
        "name": "name",
        "command": "echo hello world"
    }

    Example return:
    {
        "id": "name",
        "name": "name",
        "fields": [{
            "key": "command",
            "stringValue": "echo hello world"
        }]
    }

    :param pipeline_object: Object in the pipeline objects format.
    :return: Object in the api objects format.
    """
    import json
    import copy
    element = copy.copy(pipeline_object)
    # Remove the type because it is not required.
    # Do not error if the type is not present.
    element.pop('type', None)
    try:
        element_name = element.pop('name')
    except KeyError:
        raise AwsUtilitiesError('Missing "name" key of element: %s' %
                                json.dumps(element), pipeline_object)
    api_object = {'id': element_name,
                  'name': element_name}
    # Now we need the field list.  Each element in the field list is a dict
    # with a 'key', 'stringValue'|'refValue'
    fields = []
    for key, value in sorted(element.items()):
        fields.extend(_parse_each_field(key, value))
    api_object['fields'] = fields
    return api_object


def definition_to_parameter_objects(self, parameters):
    if 'parameters' not in parameters:
        return None
    parameter_objects = []
    for element in parameters['parameters']:
        try:
            parameter_id = element.pop('id')
        except KeyError:
            raise AwsUtilitiesError('Missing "id" key of parameter: %s' %
                                    json.dumps(element), parameters)
        parameter_object = {'id': parameter_id}
        # Now we need the attribute list.  Each element in the attribute list
        # is a dict with a 'key', 'stringValue'
        attributes = []
        for key, value in sorted(element.items()):
            attributes.extend(self._parse_each_field(key, value))
        parameter_object['attributes'] = attributes
        parameter_objects.append(parameter_object)
    return parameter_objects


def definition_to_parameter_values(self, values):
    if 'values' not in values:
        return None
    parameter_values = []
    for key in values['values']:
        parameter_values.extend(
            self._convert_single_parameter_value(key, values['values'][key]))

    return parameter_values


def _parse_each_field(key, value):
    values = []
    if isinstance(value, list):
        for item in value:
            values.append(_convert_single_field(key, item))
    else:
        values.append(_convert_single_field(key, value))
    return values


def _convert_single_field(key, value):
    field = {'key': key}
    if isinstance(value, dict) and list(value.keys()) == ['ref']:
        field['refValue'] = value['ref']
    else:
        field['stringValue'] = value
    return field


def _convert_single_parameter_value(key, values):
    parameter_values = []
    if isinstance(values, list):
        for each_value in values:
            parameter_value = {'id': key, 'stringValue': each_value}
            parameter_values.append(parameter_value)
    else:
        parameter_value = {'id': key, 'stringValue': values}
        parameter_values.append(parameter_value)
    return parameter_values
