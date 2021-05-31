from example_py_project import __version__, get_page


def test_version():
    assert __version__ == '0.1.0'

def test_get_page():
    url = "https://httpbin.org/status/200"
    res = get_page(url=url)
    assert res.status_code == 200
