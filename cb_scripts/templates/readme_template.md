# Python scripts

These are python scripts I have created, modified or used. Some scripts are for fun, while others have valuable use in production.

There's now {{scripts|length}} python file{%if scripts|length > 1%}s{% endif %} in this repo.

| Script  | DocString |
| ------------- | ------------- |
{% for x in scripts %}|<a href="./{{x.name}}">{{x.display}}</a>|{{x.docstring}}|
{% endfor %}
