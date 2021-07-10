from contextlib import contextmanager

from cookiecutter.utils import rmtree


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):

    result = cookies.bake(*args, **kwargs)

    try:
        yield result
    finally:
        rmtree(str(result.project))


def test_bake_with_defaults(cookies):

    with bake_in_temp_dir(cookies) as result:

        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None
