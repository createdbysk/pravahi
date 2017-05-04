class TestUtitilies(object):
    @staticmethod
    def test_create_pipeline_definition():
        import plugins.aws.utilities
        from nose.tools import assert_dict_equal
        # GIVEN
        pipeline_object = {
            "id": "id",
            "name": "name",
            "command": "echo hello world"
        }

        expected_api_object = {
            "id": "id",
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

