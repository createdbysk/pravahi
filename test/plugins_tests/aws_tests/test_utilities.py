class TestUtitilies(object):
    @staticmethod
    def test_pipeline_object_to_api_object():
        import plugins.aws.utilities
        from nose.tools import assert_dict_equal
        # GIVEN
        pipeline_object = {
            "type": "type",
            "name": "name",
            "command": "echo hello world"
        }

        expected_api_object = {
            "id": "name",
            "name": "name",
            "fields": [{
                "key": "command",
                "stringValue": "echo hello world"
            }]
        }

        # WHEN
        actual_api_object = plugins.aws.utilities.pipeline_object_to_api_object(pipeline_object)

        # THEN
        assert_dict_equal(expected_api_object, actual_api_object)

    @staticmethod
    def test_field_dict_to_field_key_value_list():
        import plugins.aws.utilities
        from nose.tools import assert_list_equal
        # GIVEN
        pipeline_fields = {
            "key1": "value1",
            "key2": "value2"
        }

        expected_api_fields_list = [{
            "key": "key1",
            "stringValue": "value1"
        }, {
            "key": "key2",
            "stringValue": "value2"
        }]

        # WHEN
        actual_api_fields_list = plugins.aws.utilities.field_dict_to_field_key_value_list(pipeline_fields)

        # THEN
        assert_list_equal(expected_api_fields_list, actual_api_fields_list)

