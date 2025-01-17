# Copyright 2019-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from __future__ import absolute_import

from glob import glob
import os
import sys

import setuptools


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


def read_version():
    return read("VERSION").strip()


packages = setuptools.find_packages(where="src", exclude=("test",))

required_packages = ["boto3", "numpy", "six", "psutil", "retrying>=1.3.3,<1.4", "scipy"]

# enum is introduced in Python 3.4. Installing enum back port
if sys.version_info < (3, 4):
    required_packages.append("enum34 >= 1.1.6")

PKG_NAME = "sagemaker_inference_gpu"

setuptools.setup(
    name=PKG_NAME,
    version=read_version(),
    description="(Altered to work with multi-model-server-gpu) Open source toolkit for helping create serving containers to run on Amazon SageMaker.",
    packages=packages,
    package_dir={PKG_NAME: "src/sagemaker_inference_gpu"},
    package_data={PKG_NAME: ["etc/*"]},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob("src/*.py")],
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Amazon Web Services + Blake Donahoo",
    url="https://github.com/deathstarenterprise/sagemaker-inference-gpu/",
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=required_packages,
    extras_require={
        "test": ["tox", "flake8", "pytest", "pytest-xdist", "pytest-cov", "mock", "requests"]
    },
)
