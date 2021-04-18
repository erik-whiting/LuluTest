import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='LuluTest',
    version='1.2.0',
    author='Erik Whiting',
    author_email='erik@erikwhiting.com',
    description='A web browser automation framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erik-whiting/LuluTest',
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
        'urllib3',
        'pyyaml'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.5'
)
