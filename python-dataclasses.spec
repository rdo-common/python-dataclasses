%global pypi_name dataclasses

Name:           python-%{pypi_name}
Version:        0.7
Release:        1%{?dist}
Summary:        A backport of the dataclasses module for Python 3.6

License:        Apache
URL:            https://github.com/ericvsmith/dataclasses
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 This is an implementation of PEP 557, Data Classes. It is a backport for
Python 3.6. Because dataclasses will be included in Python 3.7, any discussion
of dataclass features should occur on the python-dev mailing list at At this
point this repo should only be used for historical purposes (it's where the
original dataclasses discussions took place) and for discussion of the actual
backport to...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 This is an implementation of PEP 557, Data Classes. It is a backport for
Python 3.6. Because dataclasses will be included in Python 3.7, any discussion
of dataclass features should occur on the python-dev mailing list at At this
point this repo should only be used for historical purposes (it's where the
original dataclasses discussions took place) and for discussion of the actual
backport to...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 13 2020 ykarel <ykarel@redhat.com> - 0.7-1
- Initial package.
