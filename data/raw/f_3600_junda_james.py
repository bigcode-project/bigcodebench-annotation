import os
from docxtpl import DocxTemplate

def f_3599(template_path, output_file_path, context):
    """
    Generate a Word document from a template with the given context.

    Parameters:
    - template_path (str): The path to the Word template file (.docx).
    - output_file_path (str): The path where the output file will be saved.
    - context (dict): A dictionary containing the context to render the document with.

    Returns:
    - None

    Raises:
    - FileNotFoundError: If the template file does not exist.
    - ValueError: If the context is not a dictionary.

    Required Libraries:
    - docxtpl: For generating Word documents from templates. Ensures dynamic content can be inserted into the document based on the provided context.
    - os: For file path operations, including checking the existence of the template file.

    Example:
    Consider you have a template Word document ('template.docx') that contains placeholders for a title and a body, formatted as follows:
        {{ title }}
        {{ body }}

    You want to generate a new Word document ('output.docx') with the title "Document Title" and the body "This is the body of the document."

    Prepare your context dictionary:
    >>> context = {'title': 'Document Title', 'body': 'This is the body of the document.'}

    Call the function:
    >>> f_3599('template.docx', 'output.docx', context)

    This will replace the placeholders in the template with the values from the context dictionary and save the resulting document to 'output.docx'.
    """
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file '{template_path}' not found.")

    if not isinstance(context, dict):
        raise ValueError("The 'context' argument must be a dictionary.")

    doc = DocxTemplate(template_path)
    doc.render(context)
    doc.save(output_file_path)

import unittest
from unittest.mock import patch, mock_open
from docxtpl import DocxTemplate
import os

class TestF3599(unittest.TestCase):
    def setUp(self):
        self.template_path = 'template.docx'
        self.output_file_path = 'output.docx'
        self.context = {'title': 'Test Title', 'body': 'Test body content.'}

    @patch('os.path.exists', return_value=True)
    @patch('docxtpl.DocxTemplate.save')
    def test_document_generation_with_valid_data(self, mock_doc_save, mock_exists):
        f_3599(self.template_path, self.output_file_path, self.context)
        mock_doc_save.assert_called_once()

    @patch('os.path.exists', return_value=False)
    def test_nonexistent_template_file(self, mock_exists):
        with self.assertRaises(FileNotFoundError):
            f_3599('nonexistent_template.docx', self.output_file_path, self.context)

    @patch('os.path.exists', return_value=True)
    def test_invalid_context_type(self, mock_exists):
        with self.assertRaises(ValueError):
            f_3599(self.template_path, self.output_file_path, "not a dictionary")

    @patch('os.path.exists', return_value=True)
    @patch('docxtpl.DocxTemplate.save', autospec=True)
    def test_output_file_creation(self, mock_doc_save, mock_exists):
        f_3599(self.template_path, self.output_file_path, self.context)
        mock_doc_save.assert_called_once()

if __name__ == '__main__':
    unittest.main()
