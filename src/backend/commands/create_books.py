import click

from backend.factories import BookFactory


@click.command
@click.option("-c", "--count", default=10,   help="Number of generated instances.", type=int)
def create_books(count: int):
    BookFactory.create_batch(count)
    click.secho(f"{count} books instances has been created", fg="green")
