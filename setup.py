from setuptools import setup, find_packages

# Setup module
setup(
    # Module name
    name="colortext",
    # Module version
    version="1.0.0",
    # Description
    description="Change the Python terminal text color.",
    # License
    license="MIT",
    # Author - Github username
    author="cheongwoli",
    # Author email
    author_email="cheong7wol@gmail.com",
    # Project url
    url="https://github.com/cheongwoli/PythonTerminalTextColor",
    # Project packages
    packages=find_packages(),
    # Python requires
    python_requires=">=3.6",
    # Keywords
    keywords=["Python Terminal Text Color", "terminal text color", "colortext"],
    # Classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
