#!/usr/bin/env python3
"""
Ggaggalang 설치 스크립트
"""
from setuptools import setup, find_packages

setup(
    name="ggaggalang",
    version="0.2.0",
    description="Brainfuck 기반의 한국형 프로그래밍 언어",
    author="GG4GG4",
    author_email="noreply@github.com",
    url="https://github.com/GG4GG4/ggaggalang",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ggaggalang=ggaggalang.cli:main",
        ],
    },
)