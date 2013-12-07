%define api	3.8
%define major	3
%define libname %mklibname id3_ %{api} %{major}
%define devname %mklibname id3 -d

Summary:	A software library for manipulating ID3v1 and ID3v2 tags
Name:		id3lib
Epoch:		1
Version:	3.8.3
Release:	27
Group:		Sound
License:	LGPLv2
Url:		http://id3lib.sourceforge.net
Source0:	http://download.sourceforge.net/id3lib/%{name}-%version.tar.gz
Patch0:		id3lib-3.8.2-doxygen.patch
Patch1:		patch_id3lib_3.8.3_UTF16_writing_bug.diff
Patch2:		id3lib-3.8.3-CVE-2007-4460.patch
Patch3:		id3lib-3.8.3-includes.patch
#Patch4:		id3lib-3.8.3-link.patch
Patch5:		id3lib-3.8.3-libtool-autofoo.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(zlib)
Provides:	id3lib-examples

%description
This package provides a software library for manipulating ID3v1 and ID3v2 tags.
It provides a convenient interface for software developers to include 
standards-compliant ID3v1/2 tagging capabilities in their applications.  
Features include identification of valid tags, automatic size conversions, 
(re)synchronisation of tag frames, seamless tag (de)compression, and optional
padding facilities.
Included are some simple command line example applications.

%package -n %{libname}
Summary:	Id3lib libraries
Group:		System/Libraries

%description -n %{libname}
This package provides a software library for manipulating ID3v1 and ID3v2 tags.

%package	-n %{devname}
Summary:	Headers for developing programs that will use id3lib
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}id3-static-devel < 1:3.8.3-24

%description	-n %{devname}
This package contains the headers that programmers will need to develop
applications which will use id3lib, the software library for ID3v1 and ID3v2
tag manipulation.

%prep
%setup -q
%apply_patches
#%%patch4 -p0
(mkdir -p doc/examples
cd examples
cp *.cpp *.c *.h *.tag *.jpg *.mp3 ../doc/examples
)

%build
%configure2_5x \
	--disable-static
%make
%make docs

%install
%makeinstall_std

%files
%doc AUTHORS HISTORY NEWS README THANKS TODO
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libid3-%{api}.so.%{major}*

%files -n %{devname}
%doc README COPYING
%doc ChangeLog doc/*.html doc/*gif doc/*.txt doc/*.jpg doc/*.ico doc/*.css
%doc doc/api doc/examples
%{_includedir}/id3*.h
%{_includedir}/id3
%{_libdir}/*.so

