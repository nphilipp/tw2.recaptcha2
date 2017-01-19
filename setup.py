from setuptools import setup, find_packages

_extras_genshi = ["Genshi >= 0.7"]
_extras_mako = ["Mako"]
_extras_kajiki = ["kajiki"]
_extras_jinja = ["jinja2"]


setup(
    name="tw2.recaptcha2",
    version="0.0",
    description="ToscaWidgets2 widget for Google reCAPTCHA API v2.0",
    author="Nils Philippsen",
    author_email="nils@tiptoe.de",
    url="https://github.com/nphilipp/tw2.recaptcha2",
    #download_url="",
    install_requires=[
        "tw2.core",
        ],
    extras_require={
        'genshi': _extras_genshi,
        'mako': _extras_mako,
        'kajiki': _extras_kajiki,
        'jinja': _extras_jinja,
    },
    tests_require=['nose'] + _extras_genshi + _extras_mako + _extras_kajiki + _extras_jinja,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
		[tw2.widgets]
		widgets = tw2.recaptcha2
    """,
    keywords = ["tw2.widgets"],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
