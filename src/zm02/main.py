import datetime

import typer

from zm02 import mathtools

app = typer.Typer()


@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))

@app.command()
def lcm(m: int, n:int):
    """最小公倍数"""
    typer.echo(mathtools.lcm(m,n))

@app.command()
def fizzbuzz(x:int):
    typer.echo(mathtools.fizzbuzz(x))

    
    