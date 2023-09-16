from traitlets.config import Config
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import ExtractOutputPreprocessor
from datetime import datetime
import re

"""
Next steps:
- Add table of contents.
- Add <br> before standard headings, e.g. Objective, Methods, etc.
"""

def make_codeblocks_collapsible(body, remove_style=True):
    """
    Convert codeblocks to collapsible codeblocks. 
    Combine adjacent codeblocks into one.
    Remove <style> blocks.
    """
    pattern = re.compile(r'```python\n(.*?)```\n', re.DOTALL)
    result =  re.sub(
        pattern, r'<details>\n<summary>Code</summary>\n\n```Python\n\1```\n</details>', body)
    result = re.sub(r'</details>\s*<details>\n<summary>Code</summary>', '', result)
    if remove_style:
        pattern = re.compile(r'<style.*?>.+?</style>', re.DOTALL)
        result = re.sub(pattern, r'', result)
    return result

def export_notebook_to_md(filename, output_filename=None, figure_path='', 
    append_version=True, remove_style=True
    ):
    """
    Export a Jupyter notebook to a markdown file.
    Parameters:
    - filename (str): The filename of the Jupyter notebook.
    - output_filename (str): The filename of the output markdown file without the `.md` extension.
    - figure_path (str): The path in which to save the extracted figures.
    - append_version (bool): Whether to append the date and time to the output filename.
    """
    c = Config()
    c.ExtractOutputPreprocessor.enabled = True
    
    # Create the ExtractOutputPreprocessor with the given configuration
    preprocessor = ExtractOutputPreprocessor(config=c)
    
    exporter = MarkdownExporter(config=c)
    (body, resources) = exporter.from_filename(filename, resources={"metadata": {"path": ""}}, preprocessors=[preprocessor])
    print(output_filename)
    if append_version:
        output_filename = output_filename + '_' + datetime.now().strftime("%Y-%m-%d_%H%M") + '.md'

    body = make_codeblocks_collapsible(body, remove_style=remove_style)
    figure_path_from_root = figure_path.split('../')[-1]
    body = re.sub(r'!\[(.*?)\]\((.*?)\)', r'![\1]('+figure_path_from_root+r'\2)', body)
    result = {
        'body': body,
        'response': resources
    }
    if output_filename:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(body)
        print(f'Markdown file saved to {output_filename}')

        # Save extracted figures
        for output_entry in resources['outputs']: 
            filename = figure_path+output_entry    
            with open(filename , 'wb') as f:
                f.write(resources['outputs'][output_entry])
            print(f'Saving {filename}')

    return result

def create_readme(filename, output_filename='README.md', figure_path='../outputs/figures/', 
    append_version=False, remove_style=True
    ):
    """
    Create a README.md file from a Jupyter notebook.

    Parameters:
    - filename (str): The filename of the Jupyter notebook.
    - output_filename (str): The filename of the output markdown file.
    - append_version (bool): Whether to append the date and time to the output filename.
    """
    output_filename=f'../{output_filename}'

    result = export_notebook_to_md(
        filename, output_filename, figure_path=figure_path,
        append_version=append_version, remove_style=remove_style
        )
    return result