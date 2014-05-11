%define		_state		stable
%define		orgname		konquest
%define		qtver		4.8.0

Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl.UTF-8):	Podbój galaktyki - wersja KDE gry Gnu-Lactic Konquest
Summary(pt_BR.UTF-8):	Jogo espacial de estratégia
Name:		kde4-%{orgname}
Version:	4.13.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	002b1ccf66408235ab2d73eaaca1b123
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This the KDE version of Gnu-Lactic Konquest, a multi-player strategy
game. The goal of the game is to expand your interstellar empire
across the galaxy and of course, crush your rivals in the process.

%description -l pl.UTF-8
To jest wersja KDE gry Gnu-Lactic Konquest - gry strategicznej dla
wielu graczy. Celem gry jest rozszerzenie imperium międzygwiezdnego
poprzez galaktyki, i oczywiście niszczenie w tym czasie przeciwników.

%description -l pt_BR.UTF-8
Jogo espacial de estratégia.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_desktopdir}/kde4/konquest.desktop
%{_datadir}/apps/konquest
%{_iconsdir}/*/*/apps/konquest.png
