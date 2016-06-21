# -*- coding: utf-8 -*-

import unittest
import json

import jstyleson

json_test_case = """
{
    /*asterisk style comment with escape inside\*/
    "string": "string",
    "string_with_comment_inside": "//single line comment and /*multi-line comment*/",
    "number": 2,
    "foo": "bar", //inline comment
    "array": [1,2, /*comments inside array*/ 3],
    "nested_casual_array": [1, [2.0, 2.5,], 3, {"key_in_arr": "value_in_arr",},/*trailing comma*/],
    //single line comment
    /*multi
    line
    "comment with many "quotes"quotes"quotes"
    */
    "object": {
        "key": "中文"
    },
    "nested_casual_object": {
        "key": "中文",
        "key_in_obj": ["1_in_obj", "2_in_obj",/*trailing comma*/],
        "casual_object": {
            "key1": "value1",
            "key2": "value2",/*trailing comma*/
        },//trailing comma
    }
    //comment with 中文
}
"""

json_expected = {
    "string": "string",
    "string_with_comment_inside": "//single line comment and /*multi-line comment*/",
    "number": 2,
    "foo": "bar",
    "array": [1, 2, 3],
    "nested_casual_array": [1, [2.0, 2.5], 3, {"key_in_arr": "value_in_arr"}],
    "object": {
        "key": u"中文"
    },
    "nested_casual_object": {
        "key": u"中文",
        "key_in_obj": ["1_in_obj", "2_in_obj"],
        "casual_object": {
            "key1": "value1",
            "key2": "value2"
        }
    }
}


class TestDispose(unittest.TestCase):
    def test_dispose(self):
        disposed_json = jstyleson.dispose(json_test_case)
        result = json.loads(disposed_json)
        self.assertDictEqual(json_expected, result)
        # import timeit
        # print timeit.timeit("dispose(json_test_case)", setup="from __main__ import dispose, json_test_case", number=10000)

    def test_loads(self):
        result = jstyleson.loads(json_test_case)
        self.assertDictEqual(json_expected, result)


if __name__ == '__main__':
    unittest.main()
