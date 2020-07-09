import requests
from collections import defaultdict
import json

from rich.console import Console
from rich.table import Column, Table
from collections import namedtuple
from rich import box
from contextlib import contextmanager
import time
from rich.measure import Measurement
from rich.text import Text
from contextlib import contextmanager
import time


url = requests.get('https://projectservice02.herokuapp.com/v2/api-docs')
urlLink = url.json()

description = urlLink['info']['description']

tagsList = []
for tags in urlLink['tags']:
    tagsList.append(tags['name'])

finalList = []
def getPaths():
    url = requests.get('https://projectservice02.herokuapp.com/v2/api-docs')
    urlLink = url.json()
    for key, value in urlLink['paths'].items():
        getChildPath(key,value)

    return None

def getChildPath(parentkey, data):

    for key, value in data.items():
        shape = {}
        shape['path']= parentkey
        shape['request_methods']= key
        shape['description']= value['summary']
        shape['tag'] = value['tags'][0]
        # shape['data_type'] = [] if not value['parameters'] else value['parameters'][0]
        final(shape)
    
    return 

def final(shape):
    finalList.append(shape)
    

getPaths()
# print(json.dumps(finalList, indent=4, sort_keys=True))


console = Console()

BEAT_TIME = 0.04

@contextmanager
def beat(length: int = 1) -> None:
    with console:
        console.clear()
        yield
    time.sleep(length * BEAT_TIME)


table = Table(show_header=True, header_style="bold magenta", title_style="green", box=box.HEAVY, border_style="bright_green")

console.clear()
console.show_cursor(False)

try:
    table.add_column("Request Method")
    with beat(10):
        console.print(table, justify="center")

    table.add_column("Path")
    with beat(10):
        console.print(table, justify="center")

    table.add_column("Description")
    with beat(10):
        console.print(table, justify="center")

    table.add_column("Controller")
    with beat(10):
        console.print(table, justify="center")

    #  table.add_column("Data Type")
    #   with beat(10):
    #     console.print(table, justify="center")

    table.title = description
    with beat(10):
        console.print(table, justify="center")
    
    table_width = Measurement.get(console, table, console.width).maximum

    # print(finalList)
    for row in finalList:
    
        table.add_row(
        "[red]" + row['request_methods'] +"[/red]",
        "[cyan]" + row['path'] + "[/cyan]",
        "[blue]" + row['description'] + "[/blue]",
        "[green]" + row['tag'] + "[/green]"
        # row['data_type']
        )
        with beat(10):
            console.print(table, justify="center")

    console.print(":smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up::smiley: :thumbs_up: :smiley: :thumbs_up::smiley: :thumbs_up: ",table,":thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley: :thumbs_up: :smiley:")

finally:
    console.show_cursor(True)
