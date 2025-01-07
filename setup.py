from setuptools import setup, find_packages

setup(
    name='xssMan',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['selenium', 'setuptools'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'xssman=injection.main:main',
        ],
    },
    description='''
    xssMan: XSS Injection Exploiter (XSS-Exploit)

    Description:
    The XSS Injection Exploiter is a Python-based tool designed for security researchers,
    ethical hackers, and penetration testers to identify and demonstrate vulnerabilities in web applications.
    This tool specifically targets web application security vulnerability:

    Cross-Site Scripting (XSS):
    XSS vulnerabilities allow attackers to inject malicious scripts into trusted websites. This tool helps detect and demonstrate stored, 
    reflected (time-based, error-based) injection.

    Features:
    Multiple Payload Support:
    Includes a variety of pre-built XSS such as:

    XSS payloads to execute malicious scripts in the victim’s browser.

    ''',
    author='Ali Yousif Nayyef',
    author_email='ali.nayyef.contact@gmail.com',
    url='www.linkedin.com/in/ali-nayyef',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)