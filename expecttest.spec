#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : expecttest
Version  : 0.1.3
Release  : 2
URL      : https://files.pythonhosted.org/packages/8e/e6/584ea2be6cf46a7f86991353c8c7de8321327a50c9a3e6cd120abc904c3f/expecttest-0.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/e6/584ea2be6cf46a7f86991353c8c7de8321327a50c9a3e6cd120abc904c3f/expecttest-0.1.3.tar.gz
Summary  : No summary provided
Group    : Development/Tools
License  : MIT
Requires: expecttest-python = %{version}-%{release}
Requires: expecttest-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# expecttest [![PyPI version](https://badge.fury.io/py/expecttest.svg)](https://badge.fury.io/py/expecttest)

%package python
Summary: python components for the expecttest package.
Group: Default
Requires: expecttest-python3 = %{version}-%{release}

%description python
python components for the expecttest package.


%package python3
Summary: python3 components for the expecttest package.
Group: Default
Requires: python3-core
Provides: pypi(expecttest)

%description python3
python3 components for the expecttest package.


%prep
%setup -q -n expecttest-0.1.3
cd %{_builddir}/expecttest-0.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637359004
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
