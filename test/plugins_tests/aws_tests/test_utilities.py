class TestUtitilies(object):
    @staticmethod
    def test_create_pipeline_definition():
        import plugins.aws.utilities
        from nose.tools import assert_list_equal
        # GIVEN
        pipeline_objects = [{
            "id": "id",
            "name": "name",
            "command": "echo hello world"
        }]

        expected_api_object = [{
            "id": "id",
            "name": "name",
            "fields": [{
                "key": "command",
                "stringValue": "echo hello world"
            }]
        }]

        # WHEN
        actual_api_object = plugins.aws.utilities.pipeline_objects_to_api_objects(pipeline_objects)

        # THEN
        assert_list_equal(expected_api_object, actual_api_object)

