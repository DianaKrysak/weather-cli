import typer
import httpx
from http import HTTPStatus

APPID = '' # Your API KEY here

def main(city: str, count: int = 3):
    if APPID == '':
        typer.secho(f'Please set APPID from https://home.openweathermap.org/api_keys', fg=typer.colors.RED, err=True)

    url = (f'http://api.openweathermap.org/data/2.5/forecast'
           f'?q={city}&appid={APPID}&cnt={count}&units=metric')
    r = httpx.get(url)
    if r.status_code == HTTPStatus.OK:
        forecast_list = r.json()['list']
        for item in forecast_list:
            typer.echo(f'''{item['dt_txt']}: {item['main']['temp']}°C''')


if __name__ == '__main__':
    typer.run(main)