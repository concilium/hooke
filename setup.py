from setuptools import setup, find_packages
from src.Hooke import __version__

setup(

    name                 = 'Hooke',
    version              = __version__,
    packages             = find_packages( 'src' ),
    package_dir          = { '': 'src' },
    entry_points = {
    },

    install_requires     = [ 'Flask', 'SQLAlchemy', 'sqlalchemy-enum34', 'slackclient', 'pydispatcher' ],

    author               = 'Mike Simpson',
    author_email         = 'stendhal9@white-knight.org',
    description          = 'Play Lame Mage\'s Microscope RPG online.',
    license              = 'BSD 2-Clause',
    url                  = 'https://github.com/concilium/hooke',
    
    classifiers = [
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
)
