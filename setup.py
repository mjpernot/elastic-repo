# Classification (U)

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

# Libraries and Global Variables

# Standard
import os
import setuptools

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f_hdlr:
    LONG_DESCRIPTION = f_hdlr.read()

setuptools.setup(
    name="Elastic_Repo",
    description="Administration tasks for an Elasticsearch repository.",
    author="Mark Pernot",
    author_email="Mark.J.Pernot@coe.ic.gov",
    url="https://sc.appdev.proj.coe.ic.gov/JAC-DSXD/elastic-repo",
    version=version.__version__,
    platforms=["Linux"],
    long_description=LONG_DESCRIPTION,

    classifiers=[
        # Common Values:
        #  1 - Pre-Alpha
        #  2 - Alpha
        #  3 - Beta
        #  4 - Field
        #  5 - Production/Stable
        "Development Status :: 4 - Field",
        "Operating System :: Linux",
        "Operating System :: Linux :: Centos",
        "Operating System :: Linux :: Ubuntu",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Database",
        "Topic :: Database :: Elasticsearch",
        "Topic :: Database :: Elasticsearch :: 6.4",
        "Topic :: Database :: Elasticsearch :: 7.4",
        "Topic :: Database :: Elasticsearch :: 7.12",
        "Topic :: Database :: Elasticsearch :: 7.17",
        "Topic :: Database :: Elasticsearch :: 8.5"])
