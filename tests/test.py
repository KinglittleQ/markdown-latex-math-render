import unittest
from render import render, API


MARKDOWN_TEXT = '''
# header 1

test test test

## header 2

### code blocks

```
$$ y = \\alpha * x + y $$  # this should not be rendered
```

### formula

single line: $ s = \\beta * z $

mutiple lines:

$$
s = \sum x + y
$$

'''

RENDERED_TEXT = f'''
# header 1

test test test

## header 2

### code blocks

```
$$ y = \\alpha * x + y $$  # this should not be rendered
```

### formula

single line: ![]({API}s%20=%20\\beta%20*%20z)

mutiple lines:

![]({API}s%20=%20\sum%20x%20+%20y)

'''


class TestRender(unittest.TestCase):

    def test_render(self):
        output = render(MARKDOWN_TEXT)
        assert output == RENDERED_TEXT


if __name__ == '__main__':
    unittest.main()
