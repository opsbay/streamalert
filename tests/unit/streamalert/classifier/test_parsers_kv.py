"""
Copyright 2017-present, Airbnb Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from nose.tools import assert_equal

from stream_alert.classifier.parsers import KVParser


class TestKVParser(object):
    """Test class for KVParser"""
    # pylint: disable=no-self-use

    def test_parse(self):
        """KV Parser - Parse"""
        options = {
            'schema': {
                'name': 'string',
                'result': 'string'
            },
            'configuration': {
                'separator': ':',
                'delimiter': ',',
            }
        }
        data = 'name:joe bob,result:success'

        # get parsed data
        parser = KVParser(options)
        result = parser.parse(data)
        assert_equal(result, True)

        expected_result = [
            {
                'name': 'joe bob',
                'result': 'success'
            }
        ]

        assert_equal(parser.parses, expected_result)
