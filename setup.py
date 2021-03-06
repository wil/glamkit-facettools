from setuptools import setup, find_packages

setup(
    name='glamkit-facettools',
    version='0.1.0',
    author='Julien Phalip',
    author_email='julien@interaction.net.au',
    description='A Django app to help you filter lists of things and show number of results.',
    url='http://github.com/ixc/glamkit-facettools',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)