'''
Version command application.
'''

import typer

import nfsops

#: Version command application.
app = typer.Typer(
    name='version',
    help='Show version and exit.',
    add_completion=False
)


@app.callback(help='Show version and exit.', invoke_without_command=True)
def main():
    '''
    Show version and exit.

    Raises:
        typer.Exit: Expected completion of the application.
    '''

    typer.echo(f'Version: {nfsops.__version__}')

    raise typer.Exit()


__all__ = [
    'app',
    'main'
]
