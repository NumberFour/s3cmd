# norootforbuild

Name:           s3cmd
#%define realver 1.0.0-rc2
%define realver	1.0.0
#Version:        1.0.0_rc2
Version:		%{realver}
Release:        4001.1
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{realver}-build
Group:          Networking
Source:         http://prdownloads.sourceforge.net/s3tools/s3cmd-%{realver}.tar.gz
BuildRequires:  python-devel
Summary:        Command line tool for managing Amazon S3 and CloudFront services

%if 0%{?suse_version}
%if 0%{?suse_version} < 1020 
%define use_elementtree 1
%define use_python_xml 1
Requires:  python-devel
%else
%define use_python_xml 1
%endif

%else
# not SuSE
%if (0%{?rhel_version} > 0 && 0%{?rhel_version} < 600) || (0%{?centos_version} > 0 && 0%{?centos_version} < 600)
%define use_elementtree 1
%endif
%endif

%if %{defined use_elementtree}
BuildRequires:  python-elementtree
Requires:       python-elementtree
%endif

%if %{defined use_python_xml}
BuildRequires:  python-xml
Requires:       python-xml
%endif

%if %{defined suse_version}
%{py_requires}
%endif

%description
S3cmd lets you copy files from/to Amazon S3
(Simple Storage Service) using a simple to use
command line client. Supports rsync-like backup,
GPG encryption, and more. Also supports management
of Amazon's CloudFront content delivery network.

%prep
%setup -n s3cmd-%{realver}

%build
export S3CMD_PACKAGING=1
%{__python} setup.py build

%install
export S3CMD_PACKAGING=1
%if %{defined suse_version}
RECORD_ARG=--record-rpm
%else
RECORD_ARG=--record
%endif
%{__python} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix} $RECORD_ARG=INSTALLED_FILES

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f INSTALLED_FILES
%defattr(-,root,root,-)
%doc README PKG-INFO NEWS

%changelog
* Sun Jan  9 2011 mludvig@logix.net.nz
- Updated to s3cmd 1.0.0
* Wed Dec  8 2010 mludvig@logix.net.nz
- Updated to s3cmd 1.0.0-rc2
* Tue Oct 13 2009 mludvig@logix.net.nz
- Updated to s3cmd 0.9.9.91
