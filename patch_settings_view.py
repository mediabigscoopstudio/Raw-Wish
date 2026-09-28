with open('dash/views.py', 'a') as f:
    f.write("\n\n@login_required(login_url='login_view')\ndef settings_view(request):\n    return render(request, 'dash/settings.html', {})\n")
