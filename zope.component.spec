#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.component
Version  : 4.4.1
Release  : 7
URL      : https://pypi.debian.net/zope.component/zope.component-4.4.1.tar.gz
Source0  : https://pypi.debian.net/zope.component/zope.component-4.4.1.tar.gz
Summary  : Zope Component Architecture
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.component-python3
Requires: zope.component-python
Requires: Sphinx
Requires: persistent
Requires: setuptools
Requires: zope.configuration
Requires: zope.event
Requires: zope.hookable
Requires: zope.i18nmessageid
Requires: zope.interface
Requires: zope.location
Requires: zope.proxy
Requires: zope.security
Requires: zope.testing
Requires: zope.testrunner
BuildRequires : component-python
BuildRequires : pbr
BuildRequires : persistent-python
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zope.configuration-python
BuildRequires : zope.event
BuildRequires : zope.exceptions-python
BuildRequires : zope.hookable
BuildRequires : zope.i18nmessageid-python
BuildRequires : zope.interface
BuildRequires : zope.location-python
BuildRequires : zope.proxy-python
BuildRequires : zope.schema-python
BuildRequires : zope.security-python
BuildRequires : zope.testing-python

%description
==================

%package python
Summary: python components for the zope.component package.
Group: Default
Requires: zope.component-python3

%description python
python components for the zope.component package.


%package python3
Summary: python3 components for the zope.component package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.component package.


%prep
%setup -q -n zope.component-4.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512997232
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
