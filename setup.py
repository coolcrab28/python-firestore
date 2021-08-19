from distutils.core import setup
setup(
    # How you named your package folder (MyLib)
    name='python-firestore',
    packages=['python-firestore'],   # Chose the same as "name"
    version='0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Use Firestore without the need of firebase Admin SDK',
    author='Lakshya Mahajan',                   # Type in your name
    author_email='lakshyamah.jan@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/coolcrab28/python-firestore',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['without admin sdk', 'Firestore', 'Firebase',
              'python-firebase'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
