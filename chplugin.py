"""plugin for clickhook

define a new top-level command for clickhook and a hook command
"""
import logging
import click


@click.command()
def show():
    """Show command from plugin"""
    logging.info('calling show from plugin')
    click.echo('showing off')


'''hooked does not need to be called in the context of click, and whatever
is returned can be used.
'''


def hooked():
    """Function to call during the run hook"""
    logging.info('calling plugin.hooked')
    click.echo("I'm hooked")
