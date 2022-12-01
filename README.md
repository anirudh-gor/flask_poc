flask app poc for GSB BFF

feature change log:
- added before/after request decorators
- added CORS, CSRF middlewares
- added capability to parse and validate requests
- refactor using flask_restful
- added '/solutions' and '/solution/<sol_name>' endpoints
- added '/recommend' endpoint
  - ability to aggregate responses across multiple APIs
  - use public APIs to recommend a random song
  - API return as JSON format
- use psql as db
  - integrate flask_sqlalchemy ORM
  - connect with postgres
  - ability to to db operations using ORM
- vanilla CRUD app 'todo list'
  - ability to add/delete/update tasks
