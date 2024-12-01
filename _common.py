import pathlib
import requests



def get_input(day:int):
    """
    Gets input. Cookie is stored in cookie.py in the form {'session':'your_session_id'}

    Params:
    -------
    day: int
        The day of the advent calendar.
    """
    cookie_path=pathlib.Path("cookie.py")
    resp=requests.get(f"https://adventofcode.com/2024/day/{day}/input",cookies=eval(cookie_path.read_text()))
    print(resp.text)