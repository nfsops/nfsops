'''
Main command application.
'''

from pathlib import Path
from typing import Optional

import typer
from pydantic import ValidationError

from nfsops import ContextConfiguration, ContextType
from nfsops.cli import backup, version

#: Main command application.
app = typer.Typer(add_completion=False)

app.add_typer(version.app)
app.add_typer(backup.app)


@app.callback(help='Storage management for workspaces.')
def main(
    ctx: typer.Context,
    context: ContextType = typer.Option(
        ContextType.SUBPATH,
        '--context', '-c',
        envvar='NFSOPS_CONTEXT',
        case_sensitive=False,
        help='Context type.'
    ),
    root_template: Optional[str] = typer.Option(
        None,
        '--root-template', '-t',
        envvar='NFSOPS_ROOT_TEMPLATE',
        help='Path template for backup name reference in the root context.'
    ),
    path: Optional[Path] = typer.Option(
        None,
        '--path', '-p',
        envvar='NFSOPS_PATH',
        exists=True,
        dir_okay=True,
        help=(
            'Context path. Defaults to `$PWD` (current working directory) for subpath context, '
            '`/var/nfs-shared` otherwise.'
        )
    )
):
    '''
    Create main context.

    Parameters:
        ctx (typer.Context): Application context.
        context (ContextType): Context type.
        root_template (Optional[str]): Path template for backup name reference in the root context.
        path (Optional[Path]):
            Context path. Defaults to `$PWD` (current working directory) for subpath context,
            `/var/nfs-shared` otherwise.
    Raises:
        typer.Exit: Expected parameters contain validation errors.
    '''

    try:
        ctx.obj = ContextConfiguration(
            context=context,
            root_template=root_template,
            path=path
        )
    except ValidationError as exception:
        typer.echo(exception)
        raise typer.Exit(code=1)


__all__ = [
    'app',
    'main'
]
