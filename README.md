# NetFix - Service Provider Platform

NetFix is a Django-based web application that connects customers with service providers for various services and maintenance tasks.

## Features

- User Registration and Authentication
  - Two user types: Customer and Company
  - Unique email and username for each user
  - Profile pages for both user types

- Service Management
  - Companies can create services in their field of work
  - Customers can request services
  - Services categorized by field.
  - The following are the currently allowed fields:
    - Air Conditioner
    - All in One (Not a service field option, but a company field option to offer all kinds of services)
    - Carpentry
    - Electricity
    - Gardening
    - Home Machines
    - Housekeeping
    - Interior Design
    - Locks
    - Painting
    - Plumbing
    - Water Heaters

## Technical Details

- Built with Django v3.1.14
- Python 3.x required
- A virtual environment is required

## Setup and Installation

1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```
2. Set Up Virtual Environment:
```bash
python3 -m virtualenv venv
source venv/bin/activate
```
3. Install Requirements:
```bash
pip install -r requirements.txt
```
4. Run Migrations:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Create Superuser (optional for admin access):
```bash
python3 manage.py createsuperuser
```
6. Start Development Server:
```bash
python3 manage.py runserver
```

## Contributing

Feel free to submit a pull request and contribute to the missing functionalities, both front-end and back-end.

## License

[MIT License](LICENSE)