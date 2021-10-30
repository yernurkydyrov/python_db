# Assignment 3


## Installation

Import in the project
```bash
pip install -r requirements.txt
```
Set up the database with PostgreSQL
```sql
CREATE TABLE public.users (
	"id" integer primary key NOT NULL,
    login text not NULL,
	"password" text not NULL,
	"token" text NULL
);
```
Add some users
```sql
INSERT INTO public.users ("id",login,"password") 
values 
    (1,'admin','password'), 
    (2,'user1','password'), 
    (3,'user2','password')
```
Change Database connection strings in main.py
```python
dbName = "yourDataBaseName"
user = "yourDataBaseUserName"
```
## Usage

Run the server through termnial

```python
python src/main.py
```

Endpoints
```python
/login
/protected?token=<token>
```

## Examples

### Login examples
Succesful log in example
![Login](/Assignment3/assets/1.png)

Wrong password/login example
![WrongPass](/Assignment3/assets/WrongPass.png)
Response
![PassResponse](/Assignment3/assets/wrongPassResponse.png)

### Protected examples
Correct Token
![Correct](/Assignment3/assets/correct.png)
Wrong Token
![WrongToken](/Assignment3/assets/wrongtoken.png)


## License
[MIT](LICENSE.md)
