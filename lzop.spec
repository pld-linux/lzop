Summary:	lzop - a file compressor which uses LZO data compression library
Summary(pl):	lzop - kompresor plików u¿ywaj±cy biblioteki kompresji danych LZO
Name:		lzop
Version:	1.01
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.lzop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	de1f90bc21a0e56a27f39322f56a275d
URL:		http://www.lzop.org/
BuildRequires:	automake
BuildRequires:	lzo-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lzop is a file compressor which is very similar to gzip. lzop uses the
LZO data compression library for compression services, and its main
advantages over gzip are much higher compression and decompression
speed (at the cost of some compression ratio).

%description -l pl
lzop to kompresor plików bardzo podobny do gzipa, ale u¿ywaj±cy
biblioteki kompresji danych LZO. G³ówn± przewag± nad gzipem jest du¿o
wy¿sza szybko¶æ kompresji i dekompresji (czê¶ciowo kosztem
wspó³czynnika kompresji).

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* acconfig
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
