import os
import click
from app import create_app, db
from app.models import Admin

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

print('the root path from ihufied.py is {}'.format(app.root_path))

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Admin=Admin)

@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names: 
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run( threaded=True, debug=True)