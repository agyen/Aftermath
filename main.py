import requests
import json
import time

from collections import defaultdict
from rich.console import Console
from rich.table import Column, Table
from collections import namedtuple
from rich import box
from contextlib import contextmanager
from rich.measure import Measurement
from rich.text import Text
from contextlib import contextmanager

url = requests.get('https://petstore.swagger.io/v2/swagger.json')
urlLink = url.json()

description = urlLink['info']['description']

tagsList = []
for tags in urlLink['tags']:
    tagsList.append(tags['name'])

finalList = []
def getPaths():
    url = requests.get('https://petstore.swagger.io/v2/swagger.json')
    urlLink = url.json()
    for key, value in urlLink['paths'].items():
        getChildPath(key,value)

    return 

def getChildPath(parentkey, data):
    ran = False
    for key, value in data.items():
        jsonData = {}
        jsonData['path'] = parentkey
        jsonData['request_methods'] = key
        jsonData['description'] = value['summary']
        jsonData['tag'] = value['tags'][0]
        if "parameters" in value and not ran:
            rowObject = [] if not value['parameters'] else value['parameters'][0]
            if "type" in rowObject:
                jsonData['data_type'] = rowObject['type']
            else:
                jsonData['data_type'] = '---'
            ran 
        else:
           jsonData['data_type'] = '---'
        final(jsonData)
    
    return 

def final(jsonData):
    finalList.append(jsonData)
    
getPaths()

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

    table.add_column("Data Type")
    with beat(10):
        console.print(table, justify="center")

    table.title = description
    with beat(10):
        console.print(table, justify="center")

    table.caption = "Aftermath: turntabl swagger cli"
    with beat(10):
        console.print(table, justify="center")

    table.caption = "Aftermath: [b]turntabl swagger cli[/b]"
    with beat(10):
        console.print(table, justify="center")

    table.caption = "Aftermath: [b magenta not dim]turntabl swagger cli[/]"
    with beat(10):
        console.print(table, justify="center")
    
    for row in finalList:
        table.add_row(
        row['request_methods'],
        "[cyan]" + row['path'] + "[/cyan]",
        "[blue]" + row['description'] + "[/blue]",
        "[green]" + row['tag'] + "[/green]",
        "[yellow]" + row['data_type'] + "[/yellow]"
        )
        with beat(10):
            console.print(table, justify="center")

finally:
    console.show_cursor(True)
