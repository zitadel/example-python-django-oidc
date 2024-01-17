# Example Python Django with external OIDC Provider

This repository provides a Django example for ZITADEL using OpenID connect (OIDC) authentication instead of the internal authentication mechanism.
This example is provided as companion to our [guide](https://zitadel.com/docs/examples/login/django),
which should produce this application when followed.

## Base

The used base is the "Writing your first Django app"-app from the Django documentation under [https://docs.djangoproject.com/en/5.0/intro/](https://docs.djangoproject.com/en/5.0/intro/), which has documented additional parts in to use [mozilla-django-oidc](https://github.com/mozilla/mozilla-django-oidc) to integrate ZITADEL as AuthenticationBackend.

## Features

- OIDC Code flow with User Info call after authentication.
- Fully integrated with Django authentication
- User Role mapping to standard user types in Django (superuser/staff/user)
- Persistent user data using local sqlite file. See `DATABASE_URL` in [.env](.env).
- Public page at `/polls`
- Authenticated `/polls/<id>/` page for all users.
- Authenticated `/polls/<id>/results/` page for staff role users.
- Authenticated `/admin/` pages for admin role users.

## Getting started

If you want to run this example directly you can fork and clone it to your system.
Be sure to [configure ZITADEL](https://docs-git-docs-example-symfony-zitadel.vercel.app/docs/examples/login/symfony#zitadel-setup) to accept requests from this app.

### Prerequisites

You need all prerequisites also listed in the [Quick install quide](https://docs.djangoproject.com/en/5.0/intro/install/).

Alternatively if you have a system with Docker and an IDE capable of running [Development Container](https://containers.dev/),
definitions are provided with a complete Python environment, configuration and tools required for Django development.
Use your IDE to build and launch the development environment or use GitHub code spaces from your browser.

### Django

After setting up your system and repository, create the sqlite-database.

```bash
python manage.py migrate
```

Create a local superuser with username, email and password:

```bash
python manage.py createsuperuser
```

And run the server:

```bash
python manage.py runserve
```

Visit [http://localhost:8000/admin/], login as the superuser and click around.
You can create Questions and the availabe Choices, where users can vote on.
After you can go to [http://localhost:8000/polls/] and vote on different Questions.