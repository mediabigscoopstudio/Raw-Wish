import re

with open('template/dash/base.html', 'r') as f:
    content = f.read()

new_sidebar = """<div id="sidebar-menu">

    <div class="logo-box">
        <a href="/" class="logo logo-light">
            <span class="logo-sm">
                <h3 class="text-white mt-3">RAW WISH</h3>
            </span>
            <span class="logo-lg">
                <h2 class="text-white mt-3">RAW WISH</h2>
            </span>
        </a>
        <a href="/" class="logo logo-dark">
            <span class="logo-sm">
                <h3 class="mt-3" style="color: var(--bs-primary);">RAW WISH</h3>
            </span>
            <span class="logo-lg">
                <h2 class="mt-3" style="color: var(--bs-primary);">RAW WISH</h2>
            </span>
        </a>
    </div>

    <ul id="side-menu">

        <li class="menu-title">Command Center</li>
        <li>
            <a href="{% url 'index' %}" class="tp-link">
                <i data-feather="activity"></i>
                <span> Dashboard </span>
            </a>
        </li>
        <li>
            <a href="{% url 'intelligence' %}" class="tp-link">
                <i data-feather="pie-chart"></i>
                <span> Intelligence </span>
            </a>
        </li>

        <li class="menu-title">Commerce</li>
        <li>
            <a href="{% url 'orders_kanban' %}" class="tp-link">
                <i data-feather="shopping-cart"></i>
                <span> Orders </span>
            </a>
        </li>
        <li>
            <a href="{% url 'customers' %}" class="tp-link">
                <i data-feather="users"></i>
                <span> Customers </span>
            </a>
        </li>
        <li>
            <a href="{% url 'support_kanban' %}" class="tp-link">
                <i data-feather="headphones"></i>
                <span> Support </span>
            </a>
        </li>

        <li class="menu-title">Catalogue</li>
        <li>
            <a href="{% url 'category' %}" class="tp-link">
                <i data-feather="grid"></i>
                <span> Categories </span>
            </a>
        </li>
        <li>
            <a href="{% url 'sub_category_list' %}" class="tp-link">
                <i data-feather="layers"></i>
                <span> Sub Categories </span>
            </a>
        </li>
        <li>
            <a href="{% url 'product' %}" class="tp-link">
                <i data-feather="package"></i>
                <span> Products </span>
            </a>
        </li>

        <li class="menu-title">Marketing</li>
        <li>
            <a href="{% url 'offers' %}" class="tp-link">
                <i data-feather="tag"></i>
                <span> Offers </span>
            </a>
        </li>

        <li class="menu-title">Content</li>
        <li>
            <a href="{% url 'article_category_list' %}" class="tp-link">
                <i data-feather="folder"></i>
                <span> Categories </span>
            </a>
        </li>
        <li>
            <a href="{% url 'author_list' %}" class="tp-link">
                <i data-feather="user"></i>
                <span> Authors </span>
            </a>
        </li>
        <li>
            <a href="{% url 'article_list' %}" class="tp-link">
                <i data-feather="file-text"></i>
                <span> Articles </span>
            </a>
        </li>

    </ul>
</div>"""

content = re.sub(r'<div id="sidebar-menu">.*?</div>\s*<div class="clearfix">', new_sidebar + '\n<div class="clearfix">', content, flags=re.DOTALL)

with open('template/dash/base.html', 'w') as f:
    f.write(content)
