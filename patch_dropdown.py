import re

with open('template/dash/base.html', 'r') as f:
    content = f.read()

settings_item = """
                                    <!-- item-->
                                    <a href="{% url 'settings_view' %}" class="dropdown-item notify-item">
                                        <i class="mdi mdi-cog fs-16 align-middle"></i>
                                        <span>Settings</span>
                                    </a>
"""

# Insert before the logout item
content = content.replace('<!-- item-->\n                                    <a href="/logout_view"', settings_item + '                                    <!-- item-->\n                                    <a href="/logout_view"')

with open('template/dash/base.html', 'w') as f:
    f.write(content)
