
## {{virtualenv}} ##

* {{version}}

|Package  |
| ------------- |{% for package in packages %}
|{{package.strip()}}|{% endfor %}
