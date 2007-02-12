Summary:	WMApp graphics library
Summary(pl.UTF-8):	WMApp - biblioteka graficzna
Name:		wmapp
Version:	0.0.4.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/fetchmailmon/stable.pkg/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	4bf473fdcacce60a3e1d5fbe945e9e9d
URL:		http://www.princeton.edu/~kmccarty/wmapp.html
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is WMApp, a C++ graphics library written exclusively for
developing WindowMaker dockapps. If you like dockapps, but you also
like C++ and you are tired of trying to work with the code in
wmgeneral.c, this library is for you!

%description -l pl.UTF-8
WMApp jest graficzną biblioteką napisaną wyłącznie dla celów
rozwijania dokowalnych aplikacji Window Makera. Jeśli lubisz takie
aplikacje a także C++ i jesteś zmęczony pracą z kodem wmgeneral.c, ta
biblioteka jest właśnie dla Ciebie!

%package devel
Summary:	Header files for WMApp
Summary(pl.UTF-8):	Pliki nagłówkowe dla WMApp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	XFree86-devel
Requires:	libstdc++-devel

%description devel
The header files are only needed for development of programs using the
WMApp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe, które są potrzebne tylko dla programistów używająch
biblioteki WMApp.

%package static
Summary:	Static version of WMApp library
Summary(pl.UTF-8):	Statyczna wersja biblioteki WMApp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of WMApp library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki WMApp.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -fPIC -Wall -pedantic"

%{__cxx} %{rpmldflags} -shared *.o -o libwmapp.so.1.0 \
	-Wl,-soname=libwmapp.so.1 -L/usr/X11R6/lib -lXpm -lXext -lX11

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/%{name},%{_libdir},%{_examplesdir}/%{name}-%{version}/example{1,2}}

install libwmapp* $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install xpm/*.xpm $RPM_BUILD_ROOT%{_includedir}/%{name}
ln -s libwmapp.so.1 $RPM_BUILD_ROOT%{_libdir}/libwmapp.so

install example1/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/example1
install example2/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/example2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog Changelog.Jason README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
