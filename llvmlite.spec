#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : llvmlite
Version  : 0.30.0
Release  : 35
URL      : https://github.com/numba/llvmlite/archive/v0.30.0/llvmlite-0.30.0.tar.gz
Source0  : https://github.com/numba/llvmlite/archive/v0.30.0/llvmlite-0.30.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: llvmlite-license = %{version}-%{release}
Requires: llvmlite-python = %{version}-%{release}
Requires: llvmlite-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : llvm
BuildRequires : llvm-dev
Patch1: 0001-Use-fPIC-as-recommended-by-ld.patch
Patch2: 0002-Support-building-against-LLVM-9.patch

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

%package license
Summary: license components for the llvmlite package.
Group: Default

%description license
license components for the llvmlite package.


%package python
Summary: python components for the llvmlite package.
Group: Default
Requires: llvmlite-python3 = %{version}-%{release}

%description python
python components for the llvmlite package.


%package python3
Summary: python3 components for the llvmlite package.
Group: Default
Requires: python3-core

%description python3
python3 components for the llvmlite package.


%prep
%setup -q -n llvmlite-0.30.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571084562
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
unset LDFLAGS
export AR=llvm-ar
export RANLIB=llvm-ranlib
export NM=llvm-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/llvmlite
cp %{_builddir}/llvmlite-0.30.0/LICENSE %{buildroot}/usr/share/package-licenses/llvmlite/55c607b2a9efc5324451d2fc8a1ff473a2aae643
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/llvmlite/55c607b2a9efc5324451d2fc8a1ff473a2aae643

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
