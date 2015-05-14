class CommonViewTest():
    def test_url_ok(self):
        self.assertEqual(
            self.response.status_code, 200
            , "The view have an error"
        )


class CommonJSONViewTest():
    JSONMustBe = None

    def test_type_is_json_dict(self):
        self.assertEqual(
            self.response['Content-Type']
            , 'application/json'
            , "The response don't have a JSON content type"
        )

        self.assertIsInstance(
            self.dict_content
            , self.JSONMustBe
            , "The JSON response isn't a {0}".format(self.JSONMustBe.__name__)
        )
