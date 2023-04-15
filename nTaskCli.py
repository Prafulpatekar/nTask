import typer
from database import insert_todo,update_todo,complete_todo,change_position,get_all_todos,delete_todo
from model import Todo
from terminalUI  import get_layout
import os

app = typer.Typer()

@app.command(name="create",help="To create task")
def create(task:str,category:str):
    typer.echo(f"adding {task} , {category}")
    todo = Todo(task,category)
    print(todo)
    insert_todo(todo)
    show()

@app.command(name="delete",help="To delete task")
def delete(position:int):
    typer.echo(f"task at {position} position")
    delete_todo(position-1)
    show()

@app.command(name="update",help="To update task")
def update(position:int,task:str,category:str):
    typer.echo(f"task at {position} position {task} , {category}")
    update_todo(position-1,task,category)
    show()

@app.command(name="complete",help="To complete task")
def complete(position:int):
    typer.echo(f"task at {position} position")
    complete_todo(position-1)
    show()

@app.command(name="show",help="To show task")
def show():
    
    tasks = get_all_todos()
    get_layout(tasks)
    

if __name__=="__main__":
    os.system("cls")
    app()

