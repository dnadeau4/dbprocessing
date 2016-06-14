# -*- coding: utf-8 -*-
#
# dbprocessing documentation build configuration file, created by
# sphinx-quickstart on Fri Feb 12 15:59:00 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import sysconfig
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(
    0, os.path.abspath(
        os.path.join('..', '..', 'build', 'lib.{0}-{1}.{2}'.format(
            sysconfig.get_platform(), *sys.version_info[:2]))))
# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.pngmath',
    'sphinx.ext.viewcode',
    #'numpydoc',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
]

autosummary_generate = True
#numpydoc_show_class_members = False

# # make it so TODOs will work
# todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'dbprocessing'
copyright = u'2016, Brian Larsen, Jonathan Niehof'
author = u'Brian Larsen, Jonathan Niehof'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
from dbprocessing import __version__
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_templates']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'dbprocessingdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'dbprocessing.tex', u'dbprocessing Documentation',
     u'Brian Larsen, Jonathan Niehof', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'dbprocessing', u'dbprocessing Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'dbprocessing', u'dbprocessing Documentation',
     author, 'dbprocessing', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

#Fix for https://github.com/sphinx-doc/sphinx/issues/1585
#Have to monkey-patch in the entire method for a one-line fix.
#This is essentially verbatim from 1.2.3, plus the fix, and some namespacing
#to keep from bringing in all of sphinx.ext.autosummary
import sphinx
if sphinx.__version__ == '1.2.3':
    import sphinx.ext.autosummary
    import re
    from types import ModuleType
    from docutils.statemachine import ViewList
    from sphinx.pycode import ModuleAnalyzer, PycodeError
    class FixedAutosummary(sphinx.ext.autosummary.Autosummary):
        def get_items(self, names):
            """Try to import the given names, and return a list of
            ``[(name, signature, summary_string, real_name), ...]``.
            """
            env = self.state.document.settings.env

            prefixes = sphinx.ext.autosummary.get_import_prefixes_from_env(env)

            items = []

            max_item_chars = 50

            for name in names:
                display_name = name
                if name.startswith('~'):
                    name = name[1:]
                    display_name = name.split('.')[-1]

                try:
                    real_name, obj, parent, modname = sphinx.ext.autosummary.import_by_name(name, prefixes=prefixes)
                except ImportError:
                    self.warn('failed to import %s' % name)
                    items.append((name, '', '', name))
                    continue

                self.result = ViewList()  # initialize for each documenter
                full_name = real_name
                if not isinstance(obj, ModuleType):
                    # give explicitly separated module name, so that members
                    # of inner classes can be documented
                    full_name = modname + '::' + full_name[len(modname)+1:]
                # NB. using full_name here is important, since Documenters
                #     handle module prefixes slightly differently
                documenter = sphinx.ext.autosummary.get_documenter(obj, parent)(self, full_name)
                if not documenter.parse_name():
                    self.warn('failed to parse name %s' % real_name)
                    items.append((display_name, '', '', real_name))
                    continue
                if not documenter.import_object():
                    self.warn('failed to import object %s' % real_name)
                    items.append((display_name, '', '', real_name))
                    continue

                # try to also get a source code analyzer for attribute docs
                try:
                    documenter.analyzer = ModuleAnalyzer.for_module(
                        documenter.get_real_modname())
                    # parse right now, to get PycodeErrors on parsing (results will
                    # be cached anyway)
                    documenter.analyzer.find_attr_docs()
                except PycodeError, err:
                    documenter.env.app.debug(
                        '[autodoc] module analyzer failed: %s', err)
                    # no source file -- e.g. for builtin and C modules
                    documenter.analyzer = None

                # -- Grab the signature

                sig = documenter.format_signature()
                if not sig:
                    sig = ''
                else:
                    max_chars = max(10, max_item_chars - len(display_name))
                    sig = sphinx.ext.autosummary.mangle_signature(sig, max_chars=max_chars)
                    sig = sig.replace('*', r'\*')

                # -- Grab the summary

                documenter.add_content(None)
                doc = list(documenter.process_doc([self.result.data]))

                while doc and not doc[0].strip():
                    doc.pop(0)

                # If there's a blank line, then we can assume the first sentence /
                # paragraph has ended, so anything after shouldn't be part of the
                # summary
                for i, piece in enumerate(doc):
                    if not piece.strip():
                        doc = doc[:i]
                        break

                # Try to find the "first sentence", which may span multiple lines
                m = re.search(r"^([A-Z].*?\.)(?:\s|$)", " ".join(doc).strip())
                if m:
                    summary = m.group(1).strip()
                elif doc:
                    summary = doc[0].strip()
                else:
                    summary = ''

                items.append((display_name, sig, summary, real_name))

            return items
    sphinx.ext.autosummary.Autosummary = FixedAutosummary

#Monkey-patch to put data items in automodule
#This is essentially verbatim from 1.2.3, new code is commented with ##
from jinja2 import FileSystemLoader, TemplateNotFound
from jinja2.sandbox import SandboxedEnvironment

from sphinx import package_dir
from sphinx.ext.autosummary import import_by_name, get_documenter
from sphinx.jinja2glue import BuiltinTemplateLoader
from sphinx.pycode import ModuleAnalyzer
from sphinx.util.osutil import ensuredir
from sphinx.util.inspect import safe_getattr

import sphinx.ext.autosummary.generate
from sphinx.ext.autosummary.generate import _simple_warn, _simple_info, \
    find_autosummary_in_files
def generate_autosummary_docs(sources, output_dir=None, suffix='.rst',
                              warn=_simple_warn, info=_simple_info,
                              base_path=None, builder=None, template_dir=None):
    showed_sources = list(sorted(sources))
    if len(showed_sources) > 20:
        showed_sources = showed_sources[:10] + ['...'] + showed_sources[-10:]
    info('[autosummary] generating autosummary for: %s' %
         ', '.join(showed_sources))

    if output_dir:
        info('[autosummary] writing to %s' % output_dir)

    if base_path is not None:
        sources = [os.path.join(base_path, filename) for filename in sources]

    # create our own templating environment
    template_dirs = [os.path.join(package_dir, 'ext',
                                  'autosummary', 'templates')]
    if builder is not None:
        # allow the user to override the templates
        template_loader = BuiltinTemplateLoader()
        template_loader.init(builder, dirs=template_dirs)
    else:
        if template_dir:
            template_dirs.insert(0, template_dir)
        template_loader = FileSystemLoader(template_dirs)
    template_env = SandboxedEnvironment(loader=template_loader)

    # read
    items = find_autosummary_in_files(sources)

    # remove possible duplicates
    items = dict([(item, True) for item in items]).keys()

    # keep track of new files
    new_files = []

    # write
    for name, path, template_name in sorted(items, key=str):
        if path is None:
            # The corresponding autosummary:: directive did not have
            # a :toctree: option
            continue

        path = output_dir or os.path.abspath(path)
        ensuredir(path)

        try:
            res = import_by_name(name)
            if len(res) == 3:
                name, obj, parent = res
            else:
                name, obj, parent, mod_name = res
        except ImportError, e:
            warn('[autosummary] failed to import %r: %s' % (name, e))
            continue

        fn = os.path.join(path, name + suffix)

        # skip it if it exists
        if os.path.isfile(fn):
            continue

        new_files.append(fn)

        f = open(fn, 'w')

        try:
            doc = get_documenter(obj, parent)

            if template_name is not None:
                template = template_env.get_template(template_name)
            else:
                try:
                    template = template_env.get_template('autosummary/%s.rst'
                                                         % doc.objtype)
                except TemplateNotFound:
                    template = template_env.get_template('autosummary/base.rst')

            def get_members(obj, typ, include_public=[]):
                items = []
                for name in dir(obj):
                    try:
                        documenter = get_documenter(safe_getattr(obj, name),
                                                    obj)
                    except AttributeError:
                        continue
                    if documenter.objtype == typ:
                        items.append(name)
                public = [x for x in items
                          if x in include_public or not x.startswith('_')]
                return public, items

            ns = {}

            if doc.objtype == 'module':
                ns['members'] = dir(obj)
                ns['functions'], ns['all_functions'] = \
                                   get_members(obj, 'function')
                ns['classes'], ns['all_classes'] = \
                                 get_members(obj, 'class')
                ns['exceptions'], ns['all_exceptions'] = \
                                   get_members(obj, 'exception')
                ##Added, following four lines
                ns['data'], ns['all_data'] = \
                                   get_members(obj, 'data')
                ns['attributes'], ns['all_attributes'] = \
                                 get_members(obj, 'attribute')
            elif doc.objtype == 'class':
                ns['members'] = dir(obj)
                ns['methods'], ns['all_methods'] = \
                                 get_members(obj, 'method', ['__init__'])
                ns['attributes'], ns['all_attributes'] = \
                                 get_members(obj, 'attribute')
                ##NEW
                #Try to get stuff that's only in attributes
                if hasattr(obj, '__module__'):
                    realmodule = obj.__module__
                elif hasattr(parent, '__module__'):
                    realmodule = parent.__module__
                else:
                    realmodule = None
                if realmodule:
                    #Keyed by a tuple of (class name, attribute name)
                    #Result is a list of docstrings
                    docattrs = ModuleAnalyzer.for_module(
                        realmodule).find_attr_docs()
                    moreattrs = [k[1] for k in docattrs.keys()
                                 if k[1] not in ns['all_attributes']
                                 and k[0] == obj.__name__]
                    ns['all_attributes'].extend(moreattrs)
                    ns['attributes'].extend(
                        [a for a in moreattrs if not a.startswith('_')])
                ##END NEW

            parts = name.split('.')
            if doc.objtype in ('method', 'attribute'):
                mod_name = '.'.join(parts[:-2])
                cls_name = parts[-2]
                obj_name = '.'.join(parts[-2:])
                ns['class'] = cls_name
            else:
                mod_name, obj_name = '.'.join(parts[:-1]), parts[-1]

            ns['fullname'] = name
            ns['module'] = mod_name
            ns['objname'] = obj_name
            ns['name'] = parts[-1]

            ns['objtype'] = doc.objtype
            ns['underline'] = len(name) * '='

            rendered = template.render(**ns)
            f.write(rendered)
        finally:
            f.close()

    # descend recursively to new files
    if new_files:
        generate_autosummary_docs(new_files, output_dir=output_dir,
                                  suffix=suffix, warn=warn, info=info,
                                  base_path=base_path, builder=builder,
                                  template_dir=template_dir)

sphinx.ext.autosummary.generate.generate_autosummary_docs = \
    generate_autosummary_docs

#If the autosummary on data has docstring of object constructor instead
#of the docstring attached to the object, look at this:
#https://bitbucket.org/birkenfeld/sphinx/pull-requests/142/make-autosummary-work-with-module-class/diff
