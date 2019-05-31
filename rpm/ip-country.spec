Name:           ip-country
Version:        2.28
Release:        3%{?dist}
Summary:        Fast Lookup of Country Codes From Ip Addresses
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IP-Country/

Source0:        %{name}_%{version}.orig.tar.gz

BuildArch:      noarch

BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)

Requires:       perl(Geography::Countries)

%description
Finding the home country of a client using only the IP address can be
difficult. Looking up the domain name associated with that address can
provide some help, but many IP address are not reverse mapped to any useful
domain, and the most common domain (.com) offers no help when looking for
country.

This module comes bundled with a database of countries where various IP
addresses have been assigned. Although the country of assignment will
probably be the country associated with a large ISP rather than the client
herself, this is probably good enough for most log analysis applications,
and under test has proved to be as accurate as reverse-DNS and WHOIS
lookup.


%prep
%setup -q -n %{name}_%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}


%check
%{__make} test


%install
%{__make} pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc CHANGES README
%{_bindir}/ip2cc
%{perl_vendorlib}/IP/Authority.pm
%{perl_vendorlib}/IP/Authority/
%{perl_vendorlib}/IP/Country.pm
%{perl_vendorlib}/IP/Country/
%{_mandir}/man1/ip2cc.1*
%{_mandir}/man3/IP::Country::Slow.3*
%{_mandir}/man3/IP::Country::Medium.3*
%{_mandir}/man3/IP::Country::MaxMind.3*
%{_mandir}/man3/IP::Country::Fast.3*
%{_mandir}/man3/IP::Country.3*
%{_mandir}/man3/IP::Authority.3*


%changelog
* Fri May 31 2019 Jerry Lundström <lundstrom.jerry@gmail.com> 2.28-3
- Add RPM files.
