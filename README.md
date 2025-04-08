Sure! Here's a complete `README.md` file for your **`get-papers-list`** project, ready to drop into your repo:

---

```markdown
# 🧪 get-papers-list

`get-papers-list` is a Python CLI tool that allows users to fetch research papers from PubMed based on a search query and filter them to identify papers with authors affiliated with pharmaceutical or biotech companies. The filtered results are saved to a CSV file or printed to the console.

---

## 📁 Project Structure

```
get-papers-list/
├── get_papers_list/
│   ├── __init__.py               # Package initializer
│   ├── cli.py                    # CLI entry point using Typer
│   ├── pubmed.py                 # Logic to query and fetch data from PubMed
│   ├── filters.py                # Heuristics to filter non-academic authors
│   └── utils.py                  # Utility functions (CSV writer, etc.)
├── pyproject.toml                # Poetry config for dependency management and CLI command setup
├── README.md                     # Project documentation
└── tests/                        # Unit tests (optional)
```

---

## 🚀 Features

✅ Fetch papers using PubMed's eSearch and eFetch APIs  
✅ Supports full PubMed query syntax  
✅ Filter out academic authors using simple heuristics  
✅ Extract fields:
- **PubmedID**
- **Title**
- **Publication Date**
- **Non-academic Author(s)**
- **Company Affiliation(s)**
- **Corresponding Author Email**  
✅ Output results to CSV or display on console  
✅ Debug mode for verbose logging  
✅ Command-line interface using Typer  

---

## ⚙️ Installation & Usage

### 🧱 Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/docs/#installation)

### 🔧 Install the project

```bash
git clone https://github.com/your-username/get-papers-list.git
cd get-papers-list
poetry install
```

### ▶️ Run the program

```bash
poetry run get-papers-list "COVID-19 vaccine" --file covid_papers.csv --debug
```

### 🛠️ CLI Options

```bash
Usage: get-papers-list [OPTIONS] QUERY

Arguments:
  QUERY                      PubMed search query [required]

Options:
  -f, --file TEXT            Output CSV filename
  -d, --debug                Enable debug logging
  -h, --help                 Show this message and exit
```

---

## 🔍 How It Works

1. Sends a search request to **PubMed's eSearch API** to get a list of paper IDs based on the query.
2. Uses **eFetch API** to retrieve detailed metadata for each paper.
3. Applies simple heuristics to identify **non-academic authors** (based on keywords like "Inc", "Ltd", "Pharma", absence of university/lab terms).
4. Extracts and writes relevant information to a CSV or console.

---

## 🧰 Tools and Libraries Used

| Tool/Library                                   | Purpose                                      |
|------------------------------------------------|----------------------------------------------|
| [Typer](https://typer.tiangolo.com/)           | CLI creation using type hints                |
| [Requests](https://docs.python-requests.org/)  | HTTP requests to PubMed APIs                 |
| [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/) | XML parsing for PubMed responses  |
| [lxml](https://lxml.de/)                       | XML parser backend for BeautifulSoup         |
| [Poetry](https://python-poetry.org/)           | Dependency management and CLI packaging      |

> 💡 This project was designed and implemented with the help of **ChatGPT (OpenAI)** for planning, code generation, and debugging.

---

## 🧪 Testing (Optional)

If you add tests in the `tests/` directory, you can run them like this:

```bash
poetry run pytest
```

---

## 🐍 Running as a CLI tool

You can also make this CLI tool globally accessible:

1. Add the CLI command to `pyproject.toml`:

```toml
[tool.poetry.scripts]
get-papers-list = "get_papers_list.cli:main"
```

2. Run:

```bash
poetry install
poetry run get-papers-list "your search term here"
```

---

## 🎯 Publishing (Bonus)

To publish this module to TestPyPI:

```bash
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry build
poetry publish -r test-pypi
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests and issues are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## ✉️ Contact

**Author**: Hari Sai Kumar Thatholu  
**Email**: harisaikumar06@gmail.com
**GitHub**: [https://github.com/hari-r31]

```

---

Let me know if you'd like this saved as an actual file or help with publishing to Test PyPI!