# Pagination

This project covers different pagination techniques using Python.

## Learning Objectives

By the end of this project, you should be able to explain:

- How to paginate a dataset using `page` and `page_size`
- How to paginate a dataset using hypermedia metadata
- How to implement deletion-resilient pagination

## Files

### 0-simple_helper_function.py

Contains the `index_range` helper function that calculates
the start and end indexes for pagination.

### 1-simple_pagination.py

Implements simple pagination using a CSV dataset.

### 2-hypermedia_pagination.py

Implements hypermedia pagination and returns metadata such as:

- Current page
- Page size
- Previous page
- Next page
- Total pages

### 3-hypermedia_del_pagination.py

Implements deletion-resilient hypermedia pagination.

This allows pagination to continue correctly even when rows
are removed from the dataset.

## Dataset

The project uses:

`Popular_Baby_Names.csv`

## Requirements

- Ubuntu 20.04 LTS
- Python 3.9
- pycodestyle 2.5.x
- All files must end with a new line
- All modules, classes, and functions must be documented
- All functions must use type annotations
