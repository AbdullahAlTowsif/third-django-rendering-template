# Django Template Language (DTL) - README

## 1. If-Else Statements
Django templates support conditional statements using `{% if %}` tags.

### Syntax:
```django
{% if condition %}
    <!-- Code if condition is True -->
{% elif another_condition %}
    <!-- Code if another condition is True -->
{% else %}
    <!-- Code if none of the conditions are True -->
{% endif %}
```

### Example:
```django
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

---

## 2. For Loop
Django templates allow iteration over lists, dictionaries, or querysets using `{% for %}` loops.

### Syntax:
```django
{% for item in items %}
    <!-- Code to execute for each item -->
{% endfor %}
```

### Example:
```django
<ul>
    {% for product in products %}
        <li>{{ product.name }} - ${{ product.price }}</li>
    {% endfor %}
</ul>
```

### Using `forloop` Counter:
- `forloop.counter` → 1-based index
- `forloop.counter0` → 0-based index
- `forloop.first` → True if it's the first item
- `forloop.last` → True if it's the last item

Example:
```django
{% for student in students %}
    <p>{{ forloop.counter }}. {{ student.name }}</p>
{% endfor %}
```

---

## 3. Filtering in Templates
Django provides built-in template filters to modify values dynamically.

### Common Filters:

| Filter | Usage | Example |
|--------|-------|---------|
| `lower` | Converts text to lowercase | `{{ name|lower }}` |
| `upper` | Converts text to uppercase | `{{ name|upper }}` |
| `length` | Returns length of a list/string | `{{ items|length }}` |
| `default` | Sets default value if variable is empty | `{{ name|default:'Guest' }}` |
| `date` | Formats a datetime object | `{{ date|date:'Y-m-d' }}` |
| `truncatechars` | Truncates text after given chars | `{{ description|truncatechars:50 }}` |
| `add` | Adds a value to the variable | `{{ number|add:5 }}` |
| `divisibleby` | Checks if a number is divisible | `{{ number|divisibleby:3 }}` |
| `wordcount` | Counts words in a string | `{{ text|wordcount }}` |
| `truncatewords` | Truncates text after given words | `{{ text|truncatewords:10 }}` |
| `makelist` | Converts a string into a list | `{{ name|makelist }}` |
| `join` | Joins list elements with a separator | `{{ list|join:', ' }}` |

### Example:
```django
<p>{{ user.first_name|default:"Guest" }}</p>
<p>{{ description|truncatechars:100 }}</p>
<p>{{ price|add:10 }}</p>
<p>{{ number|divisibleby:5 }}</p>
```

---

## 4. Static Files in Templates

### Case 1: Inside Application
- We don't need to notify `settings.py` for static files and templates.

### Case 2: Outside Application
- We need to notify `settings.py` for static files and templates.

#### Example Configuration in `settings.py`:
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / "static" ]
```

### Loading Static Files in Templates
For both cases, we need to load static files in templates using:
```django
{% load static %}
```

Example usage:
```django
<img src="{% static 'images/logo.png' %}" alt="Logo">
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

### Using `get_static_prefix`
When using `{% get_static_prefix %}`, do not add whitespace after the closing bracket.

Example:
```django
<img src="{% get_static_prefix %}images/narutoXjiraiya.jpeg" alt="Naruto">
```

---

## 5. Media Files (Dynamic Files)
Django requires explicit settings to handle media files.

### TODO 1: Configure `settings.py`
```python
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = 'media/'
```

### TODO 2: Configure `urls.py`
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Conclusion
Django Template Language (DTL) provides powerful control structures such as `if-else`, `for loops`, filters, static files, and media file handling to dynamically render HTML content based on the context data passed from views.

