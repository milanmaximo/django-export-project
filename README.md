
What's this repository about?

I have found that many people have problem with Export models to CSV of Excel files.
When you do export problem is when  ForeignKey it comes as number into Excel but not as a string.

Here is solution how to get a string in your CSV or Excel.

How do I run this project locally?

1. Clone the repository:

git clone https://github.com/milanmaximo/django-export-project.git

2. Install -r requirements.txt 

3. Run migrations:

```bash
python manage.py migrate
```
4. Create a user:

```bash
python manage.py createsuperuser
```

5. Run the server:

```bash
python manage.py runserver
```
6. And open 127.0.0.1:8000 in your web browser.


