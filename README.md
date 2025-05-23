# puregym-attendance

puregym-attendance is a Python client to query the PureGym Mobile API for live gym attendance statistics.

## Dependencies

[Poetry](https://python-poetry.org/docs/basic-usage/) - `pip install poetry`

  - `poetry install` will install the necessary packages into a venv from there.

  - `poetry shell` will enter into that venv for development.
  
  - `poetry add [package]` will add a package to the venv and associated lockfile.

  - `poetry run python puregym.py [email] [pin]` (per the Usage section) will run the script inside the venv without leaving your local environment.

## Usage

```python
puregym.py [email] [pin]

Optional Arguments
--gym [gym name OR gym ID] (defaults to puregym home gym)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
