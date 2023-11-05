import click

from backend.factories import UserFactory


@click.command
@click.option("-c", "--count", default=10,   help="Number of generated instances.", type=int)
def create_users(count: int):
    UserFactory.create_batch(count)
    click.secho(f"{count} users instances has been created", fg="green")
