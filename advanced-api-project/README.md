## Book API Endpoints

### Read-Only Endpoints (Public)
- **GET** `/api/books/` → List all books
- **GET** `/api/books/<id>/` → Retrieve a single book by ID

### Authenticated CRUD Endpoints
- **POST** `/api/books/create/` → Create a new book
- **PUT** `/api/books/<id>/update/` → Update an existing book
- **DELETE** `/api/books/<id>/delete/` → Delete a book

### Permissions
- List & Detail: Accessible by everyone
- Create, Update, Delete: Only authenticated users

### Notes
- `BookSerializer` handles validation, e.g., `publication_year` cannot be in the future.
- All endpoints are connected under `/api/`.
- You can test using the DRF **Browsable API**, `curl`, or Django shell.
