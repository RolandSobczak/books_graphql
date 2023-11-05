import click

from backend.factories import AuthorFactory


@click.command
@click.option("-c", "--count", default=10,   help="Number of generated instances.", type=int)
def create_authors(count: int):
    AuthorFactory.create_batch(count)
    click.secho(f"{count} authors instances has been created", fg="green")
