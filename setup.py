from setuptools import setup

setup(
    name='pauto',
    version='2.0.0',
    description='A tool for scripting software demonstrations.',
    author='Ellen Marie Dash',
    author_email='me@duckie.co',
    url='https://github.com/duckinator/pauto',
    license='MIT',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3.8',
    ],
    install_requires=['opencv-python'],
    entry_points={
        'console_scripts': [
            'pauto=pauto:main',
        ],
    },
    packages=['pauto'],
    python_requires='>=2.7, <3.0',
)
