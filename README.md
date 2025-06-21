# CarPartsSitee

## How to Run the Project

Follow these steps to install and run the CarPartsSitee project in your local environment:

### 1. Prerequisites

- Python 3.10 or higher
- pip
- Git
- [Optional] Recommended virtual environment (venv, virtualenv, etc.)

### 2. Clone the repository

```bash
git clone https://github.com/hidravneno/CarPartsSitee.git
cd CarPartsSitee
```

### 3. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Set up environment variables

Copy the `.env.example` file to `.env` and fill in the required values (e.g., email configuration).  
If `.env.example` does not exist, create a `.env` file with the necessary variables.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser to access the admin panel

```bash
python manage.py createsuperuser
```

Follow the prompts to enter username, email, and password.

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser and go to:  
http://127.0.0.1:8000/

### 9. (Optional) Load sample data or set up inventory from the admin panel

Go to http://127.0.0.1:8000/admin with the superuser you created.

---

## Additional Notes

- Media files (product images) are stored in the `/media/` folder.
- To customize the design, edit the files in `/static` and `/templates`.
- If you have questions or issues, check the code documentation or contact the developer.

---

You’re all set! You can now use CarPartsSitee on your local environment.