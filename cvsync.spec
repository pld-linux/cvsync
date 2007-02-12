Summary:	Tailor, the VCS sync tool
Summary(pl.UTF-8):	Tailor - narzędzie do synchronizacji systemów kontroli wersji
Name:		cvsync
Version:	0
%define codate 20050612
Release:	0.%{codate}.1
License:	Free
Group:		Development/Version Control
Source0:	cvsync-%{codate}.tar.gz
# Source0-md5:	b3d7d184ecbf95278dc8112d67f48cfe
URL:		http://darcs.net/DarcsWiki/Tailor
BuildRequires:	python
BuildRequires:	python-devel >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python tool able to keep in sync various kinds of repository: it
works for various revision control systems, digesting patches coming
from three different VC, CVS, Subversion, Darcs and (still partially)
Monotone and Codeville, preserving history.

%description -l pl.UTF-8
Narzędzie w Pythonie potrafiące synchronizować różne rodzaje
repozytoriów - działa z różnymi systemami kontroli wersji, zbierając
łaty nadchodzące z trzech różnych VC: CVS, Subversion, Darcs oraz
(jeszcze częściowo) Monotone i Codeville, zachowując historię.

%prep
%setup -q -n %{name}

%build
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
