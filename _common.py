import pathlib
import requests



def get_input(day:int, test:bool=False):
    """
    Gets input. Cookie is stored in cookie.py in the form {'session':'your_session_id'}

    Params:
    -------
    day: int
        The day of the advent calendar.
    """
    if not test:
        cookie_path=pathlib.Path("cookie.py")
        resp=requests.get(f"https://adventofcode.com/2024/day/{day}/input",cookies=eval(cookie_path.read_text()))
        return resp.text
    else:
        cookie_path=pathlib.Path(f"test_data/day_{day}.txt")
        return cookie_path.read_text()
