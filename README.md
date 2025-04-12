# cumulus-site

## Project creation

The project was created using the following steps

Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Create the project directory

```bash
mkdir cumulus_site
cd cumulus_site
poetry init
```

Add initial packages

```bash
poetry add django python-decouple gunicorn whitenois
```

If you are using VS Code and come across issues where installed packages are not recognised you will need to run

```bash
poetry env info --path
```

Open pyproject.toml and add [tool section](https://python-poetry.org/docs/pyproject/#the-toolpoetry-section)

```toml
[tool.poetry]
name = "cumulus-site"
```

Ensure we are not use root installs for Poetry

```bash
poetry env remove python3.13  # or whatever version you’re using
poetry config virtualenvs.in-project true
poetry install --no-root
```

- Press Cmd+Shift+P (or Ctrl+Shift+P) to open the command palette
- Type Python: Select Interpreter
- Select entry like: `.venv/bin/python`

### Building the home page + base template

- A core app for general site pages
- A working homepage (/)
- A base layout with SEO-ready head tags (no inline HTML)
- Static + template support

```bash
poetry run python manage.py startapp core
```

## Running the dev server with Tailwind

```bash
cd assets
npm run dev
cd ..
poetry run python manage.py runserver
```
