import click
from pathlib import Path
import pymupdf4llm
import sys

@click.command()
@click.argument('input_pdf', type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument('output_md', type=click.Path(dir_okay=False, path_type=Path))
@click.option('--verbose', '-v', is_flag=True, help="Print verbose output during conversion")
def convert(input_pdf: Path, output_md: Path, verbose: bool):
    """Convert PDF document to Markdown format.

    INPUT_PDF: Path to the input PDF file
    OUTPUT_MD: Path where the output Markdown file should be saved
    """
    try:
        if verbose:
            click.echo(f"Converting {input_pdf} to {output_md}")

        # Convert PDF to markdown
        md_text = pymupdf4llm.to_markdown(str(input_pdf))

        # Write to output file
        output_md.write_text(md_text, encoding='utf-8')

        if verbose:
            click.echo("Conversion completed successfully")

    except Exception as e:
        click.echo(f"Error during conversion: {str(e)}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    convert()
