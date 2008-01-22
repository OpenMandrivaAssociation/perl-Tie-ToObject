%define module   Tie-ToObject
%define version  0.03
%define release  %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Tie to an existing object
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Tie/%{module}-%{version}.tar.gz
BuildRequires:  perl(Test::use::ok)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
While "tie" in perldoc allows tying to an arbitrary object, the class in
question must support this in it's implementation of TIEHASH, TIEARRAY or
whatever.

This class provides a very tie constructor that simply returns the object it was given as it's first argument.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/man3/*
%{perl_vendorlib}/Tie

