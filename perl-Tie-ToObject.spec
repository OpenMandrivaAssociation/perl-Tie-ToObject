%define upstream_name    Tie-ToObject
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Tie to an existing object
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch

%description
While "tie" in perldoc allows tying to an arbitrary object, the class in
question must support this in it's implementation of TIEHASH, TIEARRAY or
whatever.

This class provides a very tie constructor that simply returns the object it
was given as it's first argument.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_mandir}/man3/*
%{perl_vendorlib}/Tie


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 405758
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-4mdv2009.0
+ Revision: 258656
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-3mdv2009.0
+ Revision: 246650
- rebuild
- fix description-line-too-long

* Tue Jan 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.1
+ Revision: 156875
- import perl-Tie-ToObject


* Tue Jan 22 2008 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.03-1mdv2008.1
- first mdv release
