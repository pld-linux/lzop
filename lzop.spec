Summary:	lzop - a file compressor which uses LZO data compression library
Summary(pl.UTF-8):	lzop - kompresor plików używający biblioteki kompresji danych LZO
Name:		lzop
Version:	1.04
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.lzop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	271eb10fde77a0a96b9cbf745e719ddf
URL:		http://www.lzop.org/
BuildRequires:	automake
BuildRequires:	lzo-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lzop is a file compressor which is very similar to gzip. lzop uses the
LZO data compression library for compression services, and its main
advantages over gzip are much higher compression and decompression
speed (at the cost of some compression ratio).

%description -l pl.UTF-8
lzop to kompresor plików bardzo podobny do gzipa, ale używający
biblioteki kompresji danych LZO. Główną przewagą nad gzipem jest dużo
wyższa szybkość kompresji i dekompresji (częściowo kosztem
współczynnika kompresji).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/lzop
%{_mandir}/man1/lzop.1*
