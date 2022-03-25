'''
Backup command application.
'''

from typing import Optional, cast

import typer
from pydantic import ValidationError

from nfsops import (
    BackupConfiguration,
    BackupOperator,
    RestoreConfiguration,
    utils
)

#: Backup command application.
app = typer.Typer(
    name='backup',
    help='Manage backup versions.',
    add_completion=False
)


@app.callback(help='Manage backup versions.')
def main(
    ctx: typer.Context,
    name: Optional[str] = typer.Option(
        None,
        '--name', '-n',
        help='Backup name for root context.'
    )
):
    '''
    Create operator context.

    Parameters:
        ctx (typer.Context): Application context.
        root_template (Optional[str]): Path template for backup name reference in the root context.
    Raises:
        typer.Exit: Expected parameters contain validation errors.
    '''

    try:
        ctx.obj = BackupOperator(
            ctx.obj,
            BackupConfiguration(name=name)
        )
    except ValidationError as exception:
        typer.echo(exception)
        raise typer.Exit(code=1)


@app.command(name='list', help='List backup versions.')
def list_versions(ctx: typer.Context):
    '''
    List backup versions.

    Parameters:
        ctx (typer.Context): Application context.
    Raises:
        typer.Exit: Expected list operation failed.
    '''

    try:
        operator = cast(BackupOperator, ctx.obj)

        for backup_version in operator.list_versions():
            typer.echo(utils.format_configuration_string(backup_version))
    except Exception as exception:
        typer.echo(exception)
        raise typer.Exit(code=1)


@app.command(help='Restore backup versions.')
def restore(
    ctx: typer.Context,
    version: str = typer.Argument(
        ...,
        help='Single/initial backup version.'
    ),
    final_version: Optional[str] = typer.Argument(
        None,
        help='Final backup version.'
    )
):
    '''
    Restore backup versions.

    Parameters:
        ctx (typer.Context): Application context.
        version (str): Single/initial backup version.
        final_version (Optional[str]): Final backup version.
    Raises:
        typer.Exit: Expected parameters contain validation errors or restore operation failed.
    '''

    try:
        options = RestoreConfiguration(
            version=version,
            final_version=final_version
        )
        operator = cast(BackupOperator, ctx.obj)
        report = operator.restore(options)

        typer.echo(utils.format_configuration_string(report))
    except Exception as exception:
        typer.echo(exception)
        raise typer.Exit(code=1)


__all__ = [
    'app',
    'main',
    'list_versions',
    'restore'
]
