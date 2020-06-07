import unittest

from glossary import Glossary as Glo


class TestPythonGlossary(unittest.TestCase):
    """Tests for 'glossary.py'."""
    

    def setUp(self):
        """Glossary instance to use in all test methods."""
        self.glossary = Glo()
