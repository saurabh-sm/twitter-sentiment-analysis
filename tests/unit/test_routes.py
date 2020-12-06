def test_home(client, captured_templates):
    response = client.get('/')
    template, context = captured_templates[0]
    assert template.name == "index.html"

def test_static_analysis(client, captured_templates):
    """GET request."""
    response = client.get('/static-analysis/')
    template, context = captured_templates[0]
    assert template.name == "static-analysis.html"

def test_static_summary_report(client, captured_templates):
    """GET request."""
    response = client.get('/static-analysis/summary-report')
    template, context = captured_templates[0]
    assert template.name == "summary-report.html"

def test_static_piechart(client, captured_templates):
    """GET request."""
    response = client.get('/static-analysis/piechart')
    template, context = captured_templates[0]
    assert template.name == "piechart.html"

def test_dynamic_analysis(client, captured_templates):
    response = client.get('/dynamic-analysis/')
    template, context = captured_templates[0]
    assert template.name == "dynamic-analysis.html"
