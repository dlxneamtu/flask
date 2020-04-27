import sqlite3
from sqlite3 import Error

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('test_db.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_to_do_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Description TEXT,
          _is_done boolean,
          _is_deleted boolean,
          CreatedOn Date DEFAULT CURRENT_DATE,
          DueDate Date,
          CreatedBy INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
         id INTEGER PRIMARY KEY,
         Email TEXT,
         Name TEXT
        );
        """

        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('test_db.db')

    def create(self, text, description):
        print(f'{self.TABLENAME}',f'{text}',f'{description}')
        query = f'INSERT INTO {self.TABLENAME} (Title, Description) VALUES ' f'("{text}", "{description}")'
        cursor = self.conn.cursor()
        result = cursor.execute(query)
        self.conn.commit()


        return result

class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        self.model.create(params["Title"], params["Description"])


if __name__ == "__main__":
    Schema()
    ToDoService().create({"Title": "my first todo", "Description": "my first todo"})

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

@app.route("/<name>")
def hello_name(name):
    return "Hello you " + name + "!"

@app.route("/todo", methods=["POST"])
def create_todo():
    return ToDoService().create({"Title": "my first todo", "Description": "my first todo"})
  #  return ToDoService().create(request.get_json())


if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)