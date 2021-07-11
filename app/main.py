# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import uvicorn

from app.application import create_app

app = create_app()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("app.main:app", reload=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
