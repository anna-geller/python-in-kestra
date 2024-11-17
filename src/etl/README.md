## Shared Utilities

This package is meant to store utility code that can be shared across Python tasks.

The code itself shown here is just an example that you should replace with your:
- common functions
- common classes
- business logic code
- shared utilities.

To install the package locally in editable mode, run the following command:

```bash
pip install -e .
```

To build the package, run the following command:

```bash
pip install build
python -m build
```

This should create a `dist` directory with a `.tar.gz` file that you can install using `pip install <file>.tar.gz`, as well as a `.whl` file that you can install using `pip install <file>.whl`:

```
Successfully built etl-0.1.0.tar.gz and etl-0.1.0-py3-none-any.whl
```