#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.service
Version  : 1.4.0
Release  : 12
URL      : http://tarballs.openstack.org/oslo.service/oslo.service-1.4.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.service/oslo.service-1.4.0.tar.gz
Summary  : oslo.service library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.service-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : MarkupSafe-python
BuildRequires : Paste-python
BuildRequires : PasteDeploy-python
BuildRequires : Pygments
BuildRequires : Routes-python
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : linecache2-python
BuildRequires : mccabe-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.concurrency-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : procps-ng
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : repoze.lru-python
BuildRequires : requests-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
========================================================
oslo.service -- Library for running OpenStack services
========================================================

%package python
Summary: python components for the oslo.service package.
Group: Default
Requires: Babel-python
Requires: Paste-python
Requires: PasteDeploy-python
Requires: Routes-python
Requires: WebOb-python
Requires: eventlet-python
Requires: greenlet-python
Requires: monotonic-python
Requires: oslo.concurrency-python
Requires: oslo.config
Requires: oslo.i18n-python
Requires: oslo.log-python
Requires: oslo.utils-python
Requires: six-python

%description python
python components for the oslo.service package.


%prep
%setup -q -n oslo.service-1.4.0

%build
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
