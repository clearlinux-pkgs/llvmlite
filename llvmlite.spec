#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : llvmlite
Version  : 0.20.0
Release  : 3
URL      : http://pypi.debian.net/llvmlite/llvmlite-0.20.0.tar.gz
Source0  : http://pypi.debian.net/llvmlite/llvmlite-0.20.0.tar.gz
Summary  : lightweight wrapper around basic LLVM functionality
Group    : Development/Tools
License  : BSD-3-Clause
Requires: llvmlite-legacypython
Requires: llvmlite-python3
Requires: llvmlite-python
BuildRequires : cmake
BuildRequires : enum34
BuildRequires : llvm-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: llvm5.patch

%description
========
llvmlite
========
.. image:: https://travis-ci.org/numba/llvmlite.svg?branch=master
:target: https://travis-ci.org/numba/llvmlite
:alt: Travis CI
.. image:: https://codeclimate.com/github/numba/llvmlite/badges/gpa.svg
:target: https://codeclimate.com/github/numba/llvmlite
:alt: Code Climate
.. image:: https://coveralls.io/repos/github/numba/llvmlite/badge.svg
:target: https://coveralls.io/github/numba/llvmlite
:alt: Coveralls.io
.. image:: https://readthedocs.org/projects/llvmlite/badge/
:target: https://llvmlite.readthedocs.io
:alt: Readthedocs.io

%package legacypython
Summary: legacypython components for the llvmlite package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the llvmlite package.


%package python
Summary: python components for the llvmlite package.
Group: Default
Requires: llvmlite-legacypython
Requires: llvmlite-python3

%description python
python components for the llvmlite package.


%package python3
Summary: python3 components for the llvmlite package.
Group: Default
Requires: python3-core

%description python3
python3 components for the llvmlite package.


%prep
%setup -q -n llvmlite-0.20.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508684827
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1508684827
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
