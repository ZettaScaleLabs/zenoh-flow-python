#
# Copyright (c) 2022 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#

from setuptools import find_packages, setup
try:
    from setuptools_rust import Binding, RustExtension
except ImportError:
    import sys
    import subprocess

    subprocess.call([sys.executable, '-m', 'pip', 'install',
                     'setuptools-rust'])
    from setuptools_rust import Binding, RustExtension


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name="eclipse-zenoh-flow",
    version="0.2.0",
    description="The python API for Eclipse zenoh flow",
    long_description=readme(),
    long_description_content_type='text/markdown',
    author="ADLINK zenoh team",
    author_email="zenoh@adlink-labs.tech",
    license="EPL-2.0 OR Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Rust",
        "Intended Audience :: Developers",
        "Development Status :: 1 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="Networks network",
    url="https://github.com/atolab/zenoh-flow-python",
    project_urls={
        "Bug Tracker": "https://github.com/eclipse-zenoh/zenoh-flow/issues",
        "Source Code": "https://github.com/eclipse-zenoh/zenoh-flow",
    },
    rust_extensions=[RustExtension("zenoh_flow", "Cargo.toml",
                                   binding=Binding.PyO3, py_limited_api=True)],
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.6",
)
