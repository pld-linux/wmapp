Summary:	WMApp graphics library
Summary(pl):	WMApp biblioteka graficzna
Name:		wmapp
Version:	0.0.4.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/fetchmailmon/stable.pkg/0.3/%{name}-%{version}.tar.gz
# Source0-md5:	4bf473fdcacce60a3e1d5fbe945e9e9d
URL:		http://www.princeton.edu/~kmccarty/wmapp.html
BuildRequires:	libstdc++-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is WMApp, a C++ graphics library written exclusively for developing
WindowMaker dockapps.  If you like dockapps, but you also like C++ and you
are tired of trying to work with the code in wmgeneral.c, this library is
for you!

%description -l pl
WMApp, jest graficzn± bibliotek± napisan± wy³±cznie dla celów rozwijania
dokowalnych aplikacji Window Makera. Je¶li lubisz takie aplikacje a tak¿e
C++ i jeste¶ zmêczony prac± z kodem wmgeneral.c, ta biblioteka jest
w³a¶nie dla Ciebie!

%package devel
Summary:	Header files for WMApp
Summary(pl):	Pliki nag³ówkowe dla WMApp
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The header files are only needed for development of programs using the
WMApp library.

%description devel -l pl
Pliki nag³ówkowe, które s± potrzebne tylko dla programistów uzywaj±ch
biblioteki WMApp.

%package static
Summary:	Static version of WMApp library
Summary(pl):	Wersja statyczna WMApp
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}

%description static
Static version of WMApp library.

%description static -l pl
Wersja statyczna WMApp.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"
gcc -shared *.o -o libwmapp.so.1

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
%doc Changelog Changelog.Jason README COPYING
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%dir %{_examplesdir}/%{name}-%{version}/example1
%dir %{_examplesdir}/%{name}-%{version}/example2
%{_examplesdir}/%{name}-%{version}/example1/*
%{_examplesdir}/%{name}-%{version}/example2/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
