Summary:	lzop - a file compressor which uses LZO data compression library
Summary(pl):	lzop - kompresor plików u¿ywaj±cy biblioteki kompresji danych LZO
Name:		lzop
Version:	1.02
%define	bver	rc1
Release:	0.%{bver}.1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.lzop.org/download/%{name}-%{version}%{bver}.tar.gz
# Source0-md5:	4b999030716b1353c3dac049b269df7a
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
%setup -q -n %{name}-%{version}%{bver}

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
