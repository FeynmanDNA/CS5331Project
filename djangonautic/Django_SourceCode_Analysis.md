## Test case for escape

`django/tests/template_tests/filter_tests/test_escape.py`

they all use python 3.2+ native:
In Python 3.2 a new html module was introduced, which is used for escaping reserved characters from HTML markup.
It has one function escape():

but in 1.11 still uses inhouse escape:
`&#39; (&#x27; hexadecimal)`

```py
@keep_lazy(six.text_type, SafeText)
def escape(text):
    """
    Returns the given text with ampersands, quotes and angle brackets encoded
    for use in HTML.

    This function always escapes its input, even if it's already escaped and
    marked as such. This may result in double-escaping. If this is a concern,
    use conditional_escape() instead.
    """
    return mark_safe(
        force_text(text).replace('&', '&amp;').replace('<', '&lt;')
        .replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')
    )
```

in template/base.py
```py
def render_value_in_context(value, context):
    """
    Converts any value to a string to become part of a rendered template. This
    means escaping, if required, and conversion to a unicode object. If value
    is a string, it is expected to have already been translated.
    """
    value = template_localtime(value, use_tz=context.use_tz)
    value = localize(value, use_l10n=context.use_l10n)
    value = force_text(value)
    if context.autoescape or isinstance(value, EscapeData):
        return conditional_escape(value)
    else:
        return value
```

## try CSP
Installing collected packages: django-csp
Successfully installed django-csp-3.6


```html
<div class="article-detail">
    <div class="article">
        <img
            src=/media/default.png
            class=smallIMG onload=javascript:alert(3)

        />
        <h2 style=color:yellow; onmouseover=javascript:alert(2);>
            XSS-demo
        </h2>
        <h3>
            Written by YKY
            <a href=javascript:alert(4)>
                <button>Author Homepage</button>
            </a>
        </h3>

        <p>&lt;script&gt;alert(1)&lt;/script&gt;</p>
        <p>April 13, 2020, 4:38 a.m.</p>


            <pre>NOTE:
                You are accessing an article that is of Access-level of alert(5).
                Proceed with caution.
            </pre>
            <script>
                var accessLevel = alert(5);
                document.write("User access level is: ", accessLevel)
            </script>

    </div>
</div>
```

```html

<div class="article-detail">
    <div class="article">
        <img
            src=/media/default.png
            class=smallIMG onload=javascript:alert(3)

        />
        <h2 style=color:yellow; onmouseover=javascript:alert(2);>
            XSS-demo
        </h2>
        <h3>
            Written by YKY
            <a href=javascript:alert(4)>
                <button>Author Homepage</button>
            </a>
        </h3>

        <p><script>alert(1)</script></p>
        <p>April 13, 2020, 4:38 a.m.</p>


            <pre>NOTE:
                You are accessing an article that is of Access-level of alert(5).
                Proceed with caution.
            </pre>
            <script>
                var accessLevel = alert(5);
                document.write("User access level is: ", accessLevel)
            </script>

    </div>
</div>
```

```html
<div class="article-detail">
    <div class="article">
        <img
            src="/media/default.png"
            class="smallIMG onload=javascript:alert(3)"

        />
        <h2 style="color:yellow; onmouseover=javascript:alert(2);">
            XSS-demo
        </h2>
        <h3>
            Written by YKY
            <a href="javascript:alert(4)">
                <button>Author Homepage</button>
            </a>
        </h3>

        <p>&lt;script&gt;alert(1)&lt;/script&gt;</p>
        <p>April 13, 2020, 4:38 a.m.</p>


            <pre>NOTE:
                You are accessing an article that is of Access-level of alert(5).
                Proceed with caution.
            </pre>
            <script>
                var accessLevel = alert(5);
                document.write("User access level is: ", accessLevel)
            </script>

    </div>
</div>
```

```html
<div class="article-detail">
    <div class="article">
        <img
            src="/media/default.png"
            class="smallIMG onload=javascript:alert(3)"

        />
        <h2 style="color:yellow; onmouseover=javascript:alert(2);">
            XSS-demo
        </h2>
        <h3>
            Written by YKY
            <a href="javascript:alert(4)">
                <button>Author Homepage</button>
            </a>
        </h3>

        <p>&lt;script&gt;alert(1)&lt;/script&gt;</p>
        <p>April 13, 2020, 4:38 a.m.</p>


            <pre>NOTE:
                You are accessing an article that is of Access-level of alert(5).
                Proceed with caution.
            </pre>
            <script>
                var accessLevel = alert(5);
                document.write("User access level is: ", accessLevel)
            </script>

    </div>
</div>
```
