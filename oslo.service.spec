#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.service
Version  : 1.16.0
Release  : 24
URL      : http://tarballs.openstack.org/oslo.service/oslo.service-1.16.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.service/oslo.service-1.16.0.tar.gz
Summary  : oslo.service library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.service-python
BuildRequires : GitPython-python
BuildRequires : Jinja2
BuildRequires : Paste-python
BuildRequires : PasteDeploy-python
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : bandit-python
BuildRequires : coverage-python
BuildRequires : doc8-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : msgpack-python-python
BuildRequires : oslo.concurrency-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyinotify-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : restructuredtext_lint-python
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
========================================================
oslo.service -- Library for running OpenStack services
========================================================

%package python
Summary: python components for the oslo.service package.
Group: Default
Requires: Paste-python
Requires: PasteDeploy-python
Requires: WebOb-python
Requires: eventlet-python
Requires: greenlet-python
Requires: oslo.concurrency-python
Requires: oslo.i18n-python
Requires: oslo.log-python

%description python
python components for the oslo.service package.


%prep
%setup -q -n oslo.service-1.16.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
