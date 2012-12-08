%define major 3.8_3
%define libname %mklibname id3_ %{major}
%define devname %mklibname id3 -d
%define staticname %mklibname id3 -s -d

Name:		id3lib
Version:	3.8.3
Release:	23
Epoch:		1
Summary:	A software library for manipulating ID3v1 and ID3v2 tags
Group:		Sound
License:	LGPL
URL:		http://id3lib.sourceforge.net
Source:		http://download.sourceforge.net/id3lib/%{name}-%version.tar.bz2
Patch:		id3lib-3.8.2-doxygen.patch
Patch1:		patch_id3lib_3.8.3_UTF16_writing_bug.diff
Patch2:		id3lib-3.8.3-CVE-2007-4460.patch
Patch3:		id3lib-3.8.3-includes.patch
Patch4:		id3lib-3.8.3-link.patch
Patch5:		id3lib-3.8.3-libtool-autofoo.patch
Provides:	id3lib-examples
BuildRequires:	doxygen
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
Summary:	Id3lib libraries
Group:		System/Libraries

%description -n %{libname}
This package provides a software library for manipulating ID3v1 and ID3v2 tags.

%package	-n %{devname}
Summary:	Headers for developing programs that will use id3lib
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	zlib-devel
Provides:	libid3-devel = %{EVRD}
Provides:	libid3lib-devel = %{EVRD}
Provides:	id3lib-devel = %{EVRD}
Provides:	id3lib-doc

%description	-n %{devname}
This package contains the headers that programmers will need to develop
applications which will use id3lib, the software library for ID3v1 and ID3v2
tag manipulation.

%package -n %{staticname}
Summary:	Id3lib static libraries
Group:		Development/C++
Requires:	%{devname} = %{EVRD}

%description -n %{staticname}
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It contains the static library of id3lib.


%prep
%setup -q
%patch -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%%patch4 -p0
%patch5 -p1
(mkdir -p doc/examples
cd examples
cp *.cpp *.c *.h *.tag *.jpg *.mp3 ../doc/examples
)

%build
%configure2_5x
%make
%make docs

%install
%makeinstall_std

%files
%doc AUTHORS HISTORY NEWS README THANKS TODO
%{_bindir}/*

%files -n %{libname}
%doc README COPYING
%{_libdir}/*.so.*

%files -n %{devname}
%doc ChangeLog doc/*.html doc/*gif doc/*.txt doc/*.jpg doc/*.ico doc/*.css
%doc doc/api doc/examples
%{_includedir}/id3*.h
%{_includedir}/id3
%{_libdir}/*.so

%files -n %{staticname}
%{_libdir}/*.a

%changelog
* Tue Jun 28 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:3.8.3-20mdv2011.0
+ Revision: 687776
- removed major from devel and static pkgs
- properly commented out p4

* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 1:3.8.3-19
+ Revision: 672979
- add hug fedora patch to have it build
- fix linkage
- fix patch apply

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:3.8.3-18mdv2011.0
+ Revision: 605972
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1:3.8.3-17mdv2010.1
+ Revision: 521146
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:3.8.3-16mdv2010.0
+ Revision: 425329
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1:3.8.3-15mdv2009.0
+ Revision: 264681
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1:3.8.3-14mdv2009.0
+ Revision: 210031
- fixes for gcc 4.3

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1:3.8.3-13mdv2008.1
+ Revision: 150283
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1:3.8.3-12mdv2008.1
+ Revision: 148489
- rebuild
- do not package big ChangeLog
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 13 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1:3.8.3-11mdv2008.0
+ Revision: 85257
- Add patch2 to fix CVE-2007-4460 (Bug #33524)


* Fri Jan 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 3.8.3-10mdv2007.0
+ Revision: 108133
- Import id3lib

* Fri Jan 12 2007 Götz Waschk <waschk@mandriva.org> 3.8.3-10mdv2007.1
- unpack patches

* Sun Feb 19 2006 Götz Waschk <waschk@mandriva.org> 3.8.3-10mdk
- patch to fix UTF-16 writing

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 3.8.3-9mdk
- Rebuild

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.8.3-8mdk
- Rebuild
- Make rpmlint Happier

* Fri Jun 04 2004 Laurent Montel <lmontel@mandrakesoft.com> 3.8.3-7mdk
- Rebuild

* Mon Feb 02 2004 Götz Waschk <waschk@linux-mandrake.com> 3.8.3-6mdk
- provide id3lib-devel as well

* Mon Jan 19 2004 Olivier Blin <blino@mandrake.org> 3.8.3-5mdk
- add Epoch to Requires/Provides

