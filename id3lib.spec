%define name    id3lib
%define version 3.8.3
%define release %mkrel 11

%define major 3.8_3
%define libname %mklibname id3_ %{major}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Summary:	A software library for manipulating ID3v1 and ID3v2 tags
Source:         http://download.sourceforge.net/id3lib/%{name}-%version.tar.bz2
Patch:		id3lib-3.8.2-doxygen.patch
Patch1:		patch_id3lib_3.8.3_UTF16_writing_bug.diff
Patch2:		id3lib-3.8.3-CVE-2007-4460.patch
URL:		http://id3lib.sourceforge.net
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	LGPL
Obsoletes:      id3lib-examples
Provides:	id3lib-examples
BuildRequires:  doxygen
BuildRequires:	zlib-devel

%description
This package provides a software library for manipulating ID3v1 and ID3v2 tags.
It provides a convenient interface for software developers to include 
standards-compliant ID3v1/2 tagging capabilities in their applications.  
Features include identification of valid tags, automatic size conversions, 
(re)synchronisation of tag frames, seamless tag (de)compression, and optional
padding facilities.
Included are some simple command line example applications.

%package -n %{libname}
Summary: Id3lib libraries
Group: System/Libraries

%description -n %{libname}
This package provides a software library for manipulating ID3v1 and ID3v2 tags.

%package -n %{libname}-static-devel
Summary: Id3lib static libraries
Requires:       %{libname} = %{epoch}:%{version}-%release
Group: Development/C++

%description -n %{libname}-static-devel
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It contains the static library of id3lib.

%package	-n %{libname}-devel
Summary:	Headers for developing programs that will use id3lib
Group:		Development/C++
Requires:       %{libname} = %{epoch}:%{version}-%release
Requires:	zlib-devel
Obsoletes:      id3lib-doc
Provides:	libid3-devel = %{epoch}:%version-%release
Provides:	libid3lib-devel = %{epoch}:%version-%release , id3lib-doc
Provides:	id3lib-devel = %{epoch}:%version-%release
#for rpmlint
Provides:	libid3lib3.8-devel = %{epoch}:%version-%release
Provides:	libid3_3.8-devel = %{epoch}:%version-%release

%description	-n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use id3lib, the software library for ID3v1 and ID3v2
tag manipulation.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch
%patch1 -p1
%patch2 -p1
(mkdir -p doc/examples
cd examples
cp *.cpp *.c *.h *.tag *.jpg *.mp3 ../doc/examples
)

%build
%configure2_5x
%make
%make docs

%install
rm -rf $RPM_BUILD_ROOT


%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS HISTORY NEWS README THANKS TODO
%{_bindir}/*

%files -n %{libname}
%defattr(-, root, root)
%doc README COPYING
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc ChangeLog doc/*.html doc/*gif doc/*.txt doc/*.jpg doc/*.ico doc/*.css
%doc doc/api doc/examples
%{_includedir}/id3*.h
%{_includedir}/id3
%{_libdir}/*.la
%{_libdir}/*.so

%files -n %{libname}-static-devel
%defattr(-, root, root)
%{_libdir}/*.a


