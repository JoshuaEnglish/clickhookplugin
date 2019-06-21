"""plugin for clickhook

define a new top-level command for clickhook and a hook command
"""
import logging
import click

logger = logging.getLogger(__name__)


@click.command()
@click.pass_context
def show(ctx):
    """Show command from plugin"""
    logger.info('calling show from plugin')
    click.echo('showing off')


'''hooked does not need to be called in the context of click, and whatever
is returned can be used.
'''


def hooked(ctx):
    """Function to call during the run hook"""
    logger.info('calling plugin.hooked')
    click.echo(f"I'm hooked to ctx {ctx}")
    click.echo(f"ctx.parent: {ctx.parent}")
    click.echo(f"current library: {ctx.obj['lib']}")
