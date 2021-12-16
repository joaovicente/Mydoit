from setuptools import find_packages, setup
setup(
    name='Mydoit',
    packages=find_packages(include=['Mydoit']),
    version='0.1.0',
    description='Mydoit library',
    author='Joao Vicente',
    author_email='joao.diogo.vicente@gmail.com',
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    install_requires=["requests", "pygments", "termcolor", "pyyaml", "tabulate"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)