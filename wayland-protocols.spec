Summary:	Wayland protocol files
Summary(pl.UTF-8):	Pliki protokołu Wayland
Name:		wayland-protocols
Version:	1.30
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://wayland.freedesktop.org/releases.html
Source0:	https://gitlab.freedesktop.org/wayland/wayland-protocols/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	000b0113e7fe73eb2da6dbaf54f8eca3
URL:		https://wayland.freedesktop.org/
BuildRequires:	meson >= 0.55.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.20.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING GOVERNANCE.md MEMBERS.md README.md
%{_datadir}/wayland-protocols
%{_npkgconfigdir}/wayland-protocols.pc
