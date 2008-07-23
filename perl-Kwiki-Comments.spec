%define module	Kwiki-Comments
%define name	perl-%{module}
%define version 0.06
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Post comments to a page
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Kwiki)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Kwiki::Comments is a Kwiki plugin that allow anyone to leave comments to a
Page, just like Slash comments or MT comments.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*

