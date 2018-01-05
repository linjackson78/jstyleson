# jstyleson

![](https://travis-ci.org/linjackson78/jstyleson.svg?branch=master)

jstyleson is a python library to parse JSON with js-style comments. Trailing comma is also supported.

JSON by standard does not allow comments and trailing comma, and the python standard json module does not offer options to parse such informal JSON.

```python
import json
invalid_json_str = """{
    // Single-line comment
    "foo": "bar", // Behold that trailing comma
    /*
    Multi-line comment
     */
}
"""
json.loads(invalid_json_str) # Raise Exception
```

jstyleson try to make it happy with your js-style commented JSON, by first removing all elements inside (comments and trailing comma), then hand it to the standard json module.

jstyleson supports parsing JSON with:

* single-line comment
* multi-line comment
* inline comment
* trailing comma

# Installation

`pip install jstyleson`

# Usage

jstyleson provide some wrapper function around the standard json module:

```python
import jstyleson
result_dict = jstyleson.loads(invalid_json_str) # OK
jstyleson.dumps(result_dict)
```

Under the hood, jstyleson do nothing but remove all invalid elements via the `dispose` function. So you can invoke it manually like this:

`valid_json_str = jstyleson.dispose(invalid_json_str)`

# Testing

`python setup.py test`

# License

The MIT License (MIT)
Copyright (c) 2016 linjackson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
