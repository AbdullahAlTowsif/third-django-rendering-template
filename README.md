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

### Example:
```django
<p>{{ user.first_name|default:"Guest" }}</p>
<p>{{ description|truncatechars:100 }}</p>
```

---

## Conclusion
Django Template Language (DTL) provides powerful control structures such as `if-else`, `for loops`, and filters to dynamically render HTML content based on the context data passed from views.

