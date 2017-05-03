class TestUtitilies(object):
    @staticmethod
    def test_create_pipeline_definition():
        import plugins.aws.utilities
        from nose.tools import assert_list_equal
        # GIVEN
        definition = [
            {
                "id": "id",
                "name": "name",
                "key": "value"
            }
        ]

        expected_api_object = [{
            "id": "id",
            "name": "name",
            "fields": [{
                "key": "key",
                "stringValue": "value"
            }]
        }]

        # WHEN
        actual_api_object = plugins.aws.utilities.definition_to_api_objects(definition)

        # THEN
        assert_list_equal(expected_api_object, actual_api_object)

