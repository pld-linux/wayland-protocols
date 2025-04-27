Summary:	Wayland protocol files
Summary(pl.UTF-8):	Pliki protokołu Wayland
Name:		wayland-protocols
Version:	1.44
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://wayland.freedesktop.org/releases.html
Source0:	https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	bbf053c2d62cf11e253cf2cc151c2df0
URL:		https://wayland.freedesktop.org/
BuildRequires:	libstdc++-devel
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.23.0
BuildRequires:	xz
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING GOVERNANCE.md MEMBERS.md README.md
%{_datadir}/wayland-protocols
%{_npkgconfigdir}/wayland-protocols.pc
%{_includedir}/wayland-protocols
