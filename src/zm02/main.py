import datetime

import typer

from zm02 import mathtools

from . import demo

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

@ app.command()
def hello(name: str = "Kouki"):
    typer.echo(demo.hello(name))
    





@app.command()
def movie():
    """ランダムな洋画を表示します"""
    result = demo.get_random_movie()
    print(f"おすすめの洋画：{result}")

if __name__ == "__main__":
    app()






@app.command()
def encode():
    """謎のカエサル暗号に変換します（import禁止ver）"""
    text = input("🔐 入力してください：")
    encoded = demo.caesar_code(text)
    print("🧩 変換結果：", encoded)


@app.command()
def decode():
    """🔓 カエサル暗号を元に戻します（importなし）"""
    text = input("🔐 暗号文を入力してください：")
    decoded = demo.decode_caesar(text)
    print("🧩 元の文章：", decoded)
