import streamlit as st
from src import functions

todos = functions.get_todos()


def main():
    todo = input("Paste todo: ")
    add_todo(todo)


def add_todo(todo):
    todos.append(todo + "\n")
    functions.write_todos(todos)


if __name__ == '__main__':
    main()
