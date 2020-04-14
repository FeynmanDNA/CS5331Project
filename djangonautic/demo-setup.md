## URL
```sh
127.0.0.1:8000/articles/xss-demo?accessLevel=alert(5)
```

## 1. with HTML escape

```sh
git checkout XSS-attr-inject && python manage.py runserver
```

## 2. quoting attributes

```sh
git checkout XSS-with-quotes && python manage.py runserver
```

## 3. CSP

```sh
git checkout CSP && python manage.py runserver
```
