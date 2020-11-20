from setuptools import setup, find_packages

# Setup module
setup(
    # Module name
    name="terminalcolor",
    # Module version
    version="1.0.2",
    # Description
    description="Change the Python terminal text color.",
    # Long Description
    long_description=open('README.rst').read(),
    # License
    license="MIT",
    # Author - Github username
    author="cheongwoli",
    # Author email
    author_email="cheong7wol@gmail.com",
    # Project url
    url="https://github.com/cheongwoli/TerminalColor",
    # Project packages
    packages=find_packages(),
    # Python requires
    python_requires=">=3.6",
    # Keywords
    keywords=["Python Terminal Text Color", "terminal text color", "terminalcolor"],
    # Classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
