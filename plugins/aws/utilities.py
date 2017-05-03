class AwsUtilitiesError(Exception):
    def __init__(self, msg, definition):
        full_msg = (
            "Error in pipeline definition: %s\n" % msg)
        super(AwsUtilitiesError, self).__init__(full_msg)
        self.msg = msg
        self.definition = definition


def definition_to_api_objects(definition):
    import json
    api_elements = []
    # To convert to the structure expected by the service,
    # we convert the existing structure to a list of dictionaries.
    # Each dictionary has a 'fields', 'id', and 'name' key.
    for element in definition:
        try:
            element_id = element.pop('id')
        except KeyError:
            raise AwsUtilitiesError('Missing "id" key of element: %s' %
                                    json.dumps(element), definition)
        api_object = {'id': element_id}
        # If a name is provided, then we use that for the name,
        # otherwise the id is used for the name.
        name = element.pop('name', element_id)
        api_object['name'] = name
        # Now we need the field list.  Each element in the field list is a dict
        # with a 'key', 'stringValue'|'refValue'
        fields = []
        for key, value in sorted(element.items()):
            fields.extend(_parse_each_field(key, value))
        api_object['fields'] = fields
        api_elements.append(api_object)
    return api_elements


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
