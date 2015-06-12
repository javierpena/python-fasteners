%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

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


%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        A python package that provides useful locks

BuildRequires:  python3-six
BuildRequires:  python3-devel

Requires:  python3-six

%description -n python3-%{pypi_name}
A python package that provides useful locks.
%endif


%description
A python package that provides useful locks.

%prep
%setup -qc
mv %{pypi_name}-%{version} python2
pushd python2

# copy LICENSE etc. to top level dir
cp -a README.rst ..

popd

%if 0%{?with_python3}
cp -a python2 python3
%endif


%build
pushd python2
%{__python2} setup.py build
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py build
popd
%endif # with_python3

%install
pushd python2
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%files
%doc README.rst

%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python_version}.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%endif

%changelog
