# cumulus-site

## Project install

Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install dependencies

```bash
poetry install
cd assets
npm install
```

## Running the dev server with Tailwind

```bash
cd assets
npm run dev
cd ..
poetry run python manage.py runserver
```
