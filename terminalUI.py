from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table

from getpass import getuser


console = Console()




def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    layout["main"].split_row(
        Layout(name="body", ratio=8),
        Layout(name="footer", ratio=4),
    )
    return layout


class Header:
    """Display header with clock."""
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="left", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[i]Welcome to[/i] [b]nTask Manager[/b] Cli Tool 💻",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
            
        )
        return Panel(grid, style="cyan on black")


def greet_user():
    """Some example content."""
    body_headline = Table.grid(padding=0)
    body_headline.add_column(style="yellow", justify="left")
    body_headline.add_row(
        f"Hi, {getuser()} ",
    )
    return body_headline


def make_footer_panel() -> Panel:
    message = Table.grid()
    message.add_column()
    message.add_column(no_wrap=True)
    footer_table = make_footer_table()
    message.add_row(footer_table)

    message_panel = Panel(
        Align.left(
            Group(Align.left(footer_table),"\n"),
        ),
        box=box.ROUNDED,
        title="[bold red]Author Info",
        border_style="bright_red",
    )
    return message_panel

def make_footer_table() -> Table:
    """Some example content."""
    sponsor_message = Table.grid()
    sponsor_message.add_column(style="green", justify="left")
    sponsor_message.add_column(no_wrap=False,justify="left")
    sponsor_message.add_row(
        "Name",
        ": Praful Patekar",
    )
    sponsor_message.add_row(
        "Gmail",
        ": prafulpatekar23@gmail.com",
    )
    sponsor_message.add_row(
        "Mobile",
        ": 8625921207",
    )
    sponsor_message.add_row(
        "Profile",
        ": SDE-1 @ pvt ltd Company",
    )
    sponsor_message.add_row(
        "Message",
        ": You can reach me for any projects \t\nI can build anything!",
    )
    return sponsor_message

def make_todo_table(tasks) -> Table:
    """Some example content."""
    table = Table(show_header=True,header_style="bold white",width=None,border_style="white",box=box.DOUBLE_EDGE)
    table.add_column("#",min_width=2,justify="center")
    table.add_column("Tasks",width=40,justify="left",no_wrap=False)
    table.add_column("Category",width=10,justify="left")
    table.add_column("Status",width=6,justify="center")

    def get_category_color(category):
        COLORS = {
            'Learn':'cyan',
            'YouTube':'red',
            'Sports':'yellow',
            'Study':'green',
        }
        if category in COLORS:
            return COLORS[category]
        return 'white'


    for idx,task in enumerate(tasks,start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == True else '❌'
        table.add_row(str(idx),task.task,f'[{c}]{task.category}[/{c}]', is_done_str)
    return table

def make_body_panel(tasks) -> Panel:
    message = Table.grid(padding=0)
    message.add_column(no_wrap=True)
    sponsor_message = greet_user()
    message_panel = Panel(
        Align.left(
            Group(Align.left(sponsor_message),Align.left(make_todo_table(tasks))),
        ),
        box=box.ROUNDED,
        title="[bold cyan]nTask Status Table",
        border_style="cyan",
    )
    return message_panel


layout = make_layout()
def get_layout(tasks):
    layout["header"].update(Header())
    layout["body"].update(make_body_panel(tasks))
    layout["footer"].update(make_footer_panel())
    console.print(layout)
        
        


