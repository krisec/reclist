"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def series(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'app/series.html',
        {
            'title':'Series 1',
            'season_count': 9,
            'episode_count': 81,
            'num_recs':150123,
            'num_dislikes':12312,
            'synopsis': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis interdum in eros nec laoreet. Nullam sagittis non ex nec tempus. Curabitur iaculis suscipit purus, a laoreet sem tincidunt non. Aenean vitae nulla ut lacus scelerisque cursus eu vel leo. Aenean interdum est dolor, eget consequat purus finibus eget. Praesent tincidunt purus vitae semper lacinia. Nullam ac metus massa. Nunc quis justo in orci fermentum gravida. Proin vitae fringilla tellus. Duis non massa vehicula, vulputate elit eu, dictum felis. Vivamus ultrices consectetur urna, a fringilla lorem commodo vitae. Nulla suscipit egestas interdum. Curabitur lobortis eros nec massa elementum congue vel eget nulla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Maecenas eu suscipit purus, vitae condimentum justo.",
            'year':datetime.now().year
        }
    )