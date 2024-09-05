```
uvx ruff check
uvx mypy src
uv run pytest -sv
uvx hatch build -t wheel
uvx twine upload dist/*
```
