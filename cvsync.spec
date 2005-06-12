
Summary:	Tailor, the VCS sync tool
Name:		cvsync
Version:	0
%define codate 20050612
Release:	0.%{codate}.1
License:	Free
Source0:	cvsync-%{codate}.tar.gz
# Source0-md5:	b3d7d184ecbf95278dc8112d67f48cfe
URL:		http://darcs.net/DarcsWiki/Tailor
Group:		Development/Version Control
BuildRequires:	python
BuildRequires:	python-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python tool able to keep in sync various kinds of repository: it works for various revision control systems, digesting patches coming from three different VC, CVS, Subversion, Darcs and (still partially) Monotone and Codeville, preserving history.

%prep
%setup -q -n %{name}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tailor.py
%dir %{py_sitescriptdir}/vcpx
%{py_sitescriptdir}/vcpx/*.py[co]
