import os
from pathlib import Path
import random
from textwrap import dedent

import yaml

from sphinx.application import Sphinx
from sphinx.util import logging

from pyzotero import zotero
import bibtexparser

from dotenv import dotenv_values
config=dotenv_values(".env")

LOGGER = logging.getLogger("conf")

def generate_zotero_library(app: Sphinx):
    zot = zotero.Zotero(config["NFETRA_GROUP"], "group", config["ZOTERO_KEY"])
    items = zot.collection_items(config["ZOTERO_PUBLICATIONS_KEY"], limit=5, format="bibtex", sort="date")

    with open("latest-publications.bib", "w") as f:
        bibtexparser.dump(items, f)