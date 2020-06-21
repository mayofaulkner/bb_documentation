from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
import os
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

nb_path = Path('C:/Users/Mayo/iblenv/bb_documentation/docs/tutorials/jupyer_test.ipynb')
file_path = Path('C:/Users/Mayo/iblenv/bb_documentation/executed_notebook.ipynb')

with open(nb_path) as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

nb, r = ep.preprocess(nb, {'path': 'C:/Users/Mayo/iblenv/bb_documentation/src'})

with open('executed_notebook.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)


from nbconvert import RSTExporter
# Instantiate it
rst_exporter = RSTExporter()

with open(file_path) as f:
    nb = nbformat.read(f, as_version=4)

(body, resources) = rst_exporter.from_notebook_node(nb)

from nbconvert.writers import FilesWriter
writer = FilesWriter()

output_file_path = writer.write(body, resources,
                                notebook_name='test')

from traitlets.config import Config
from nbconvert import HTMLExporter

c = Config()
c.HTMLExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']
 # create the new exporter using the custom config
html_exporter_with_figs = HTMLExporter(config=c)
html_exporter_with_figs.preprocessors

(output, resources_with_fig) = html_exporter_with_figs.from_notebook_node(nb)
output_file_path = writer.write(output, resources_with_fig,
                                notebook_name = 'html')
