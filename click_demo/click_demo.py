import click


@click.group()
def psp():
    pass


@psp.command()
@click.option('--name', '-n', default='there', prompt='Please ent Name', help='Name of the person to greet',
              show_default=True)
def hi(name):
    click.echo('Hi {}!'.format(name))    # used instead of print since print syntax differ by version, just a
    # safer side they say


@psp.command()
@click.option('--name', '-n', default='there', prompt='Please ent Name', help='Name of the person to greet',
              show_default=True)
def bye(name):
    click.echo('Bye {}!'.format(name))


# psp.add_command(hi)
# psp.add_command(bye)

if __name__ == '__main__':
    pass
