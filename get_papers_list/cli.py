# get_papers_list/cli.py

import typer
from typing import Optional
from get_papers_list.pubmed import fetch_papers
from get_papers_list.utils import write_to_csv
from rich import print

app = typer.Typer()

@app.command()
def run(
    query: str = typer.Argument(..., help="Search query for PubMed"),
    file: Optional[str] = typer.Option(None, "-f", "--file", help="Output CSV filename"),
    debug: bool = typer.Option(False, "-d", "--debug", help="Enable debug output")
):
    """
    Fetch PubMed papers and filter for non-academic affiliations.
    """
    if debug:
        print(f"[bold blue]Query:[/bold blue] {query}")
    
    papers = fetch_papers(query, debug=debug)

    if file:
        write_to_csv(papers, file)
        print(f"[green]Saved results to {file}[/green]")
    else:
        for p in papers:
            print(p)

def main():
    app()
