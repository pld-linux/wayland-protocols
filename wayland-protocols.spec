Summary:	Wayland protocol files
Summary(pl.UTF-8):	Pliki protokołu Wayland
Name:		wayland-protocols
Version:	1.14
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://wayland.freedesktop.org/releases.html
Source0:	https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
# Source0-md5:	5d32eaf0f5d6b7da7f5ad0959e2551e6
URL:		https://wayland.freedesktop.org/
BuildRequires:	pkgconfig
BuildRequires:	wayland-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wayland-protocols contains Wayland protocols that adds functionality
not available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some
other protocol either in Wayland core, or some other protocol in
wayland-protocols.

%description -l pl.UTF-8
Pakiet wayland-protocols zawiera protokoły Wayland dodające
funkcjonalność niedostępną w podstawowym protokole Wayland. Protokoły
te dodają zupełnie funkcje, albo rozszerzają funkcjonalność innego
protokołu spośród postawiowych protokołów Wayland lub innego protokołu
z wayland-protocols.

%prep
%setup -q

%build
%configure \
%if "%{_gnu}" != "-gnux32"
	--host=%{_host} \
	--build=%{_host} \
%endif
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_datadir}/wayland-protocols
%{_npkgconfigdir}/wayland-protocols.pc
