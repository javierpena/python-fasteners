%global pypi_name fasteners

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        A python package that provides useful locks

License:        ASL 2.0
URL:            https://github.com/harlowja/fasteners
Source0:        https://pypi.python.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel

BuildRequires:  python-six
Requires:       python-six

%description
A python package that provides useful locks.

%prep
%setup -qc

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst

# license is included in latest github checkout
# %LICENSE LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info

%changelog

