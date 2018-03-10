from distutils.core import setup

setup(
    name='aiopause',
    version='0.1.2',
    license='LICENSE.txt',
    author='Patrick Thomas',
    author_email='none@none.com',
    packages=['pause', 'pause.tests'],
    url='https://github.com/Tinkerwolf/python-pause',
    description='A timestamp-based sleep function for AsyncIO based on Jeremy\'s pause.',
    long_description=open('README.rst').read(),
    platforms='osx, posix, linux, windows',
    keywords='sleep timestamp datetime',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Environment :: Console'
    ]
)
