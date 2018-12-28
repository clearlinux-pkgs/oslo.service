#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.service
Version  : 1.33.0
Release  : 42
URL      : http://tarballs.openstack.org/oslo.service/oslo.service-1.33.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.service/oslo.service-1.33.0.tar.gz
Source99 : http://tarballs.openstack.org/oslo.service/oslo.service-1.33.0.tar.gz.asc
Summary  : oslo.service library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.service-license = %{version}-%{release}
Requires: oslo.service-python = %{version}-%{release}
Requires: oslo.service-python3 = %{version}-%{release}
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: WebOb
Requires: eventlet
Requires: fixtures
Requires: greenlet
Requires: monotonic
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Team and repository tags
        ========================

%package license
Summary: license components for the oslo.service package.
Group: Default

%description license
license components for the oslo.service package.


%package python
Summary: python components for the oslo.service package.
Group: Default
Requires: oslo.service-python3 = %{version}-%{release}

%description python
python components for the oslo.service package.


%package python3
Summary: python3 components for the oslo.service package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.service package.


%prep
%setup -q -n oslo.service-1.33.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541635965
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.service
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.service/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.service/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
