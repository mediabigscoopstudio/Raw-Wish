from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www|', 'main.urls', name='main'),  # Matches the root domain (e.g., example.com)
    host(r'dash', 'dash.urls', name='dash'),  # Matches dash subdomain
)
