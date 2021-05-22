#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Perl4-CoreLibs
Version  : 0.004
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Perl4-CoreLibs-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Perl4-CoreLibs-0.004.tar.gz
Summary  : 'libraries historically supplied with Perl 4'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Perl4-CoreLibs-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Perl4::CoreLibs - libraries historically supplied with Perl 4
DESCRIPTION
This is a collection of ".pl" files that were bundled with the Perl
core until core version 5.15.1.  Relying on their presence in the core
distribution is deprecated; they should be acquired from this CPAN
distribution instead.  From core version 5.13.3 until their removal, the
core versions of these libraries emit a deprecation warning when loaded.
The CPAN version does not emit such a warning.

%package dev
Summary: dev components for the perl-Perl4-CoreLibs package.
Group: Development
Provides: perl-Perl4-CoreLibs-devel = %{version}-%{release}
Requires: perl-Perl4-CoreLibs = %{version}-%{release}

%description dev
dev components for the perl-Perl4-CoreLibs package.


%package perl
Summary: perl components for the perl-Perl4-CoreLibs package.
Group: Default
Requires: perl-Perl4-CoreLibs = %{version}-%{release}

%description perl
perl components for the perl-Perl4-CoreLibs package.


%prep
%setup -q -n Perl4-CoreLibs-0.004
cd %{_builddir}/Perl4-CoreLibs-0.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Perl4::CoreLibs.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Perl4/CoreLibs.pm
/usr/lib/perl5/vendor_perl/5.34.0/abbrev.pl
/usr/lib/perl5/vendor_perl/5.34.0/assert.pl
/usr/lib/perl5/vendor_perl/5.34.0/bigfloat.pl
/usr/lib/perl5/vendor_perl/5.34.0/bigint.pl
/usr/lib/perl5/vendor_perl/5.34.0/bigrat.pl
/usr/lib/perl5/vendor_perl/5.34.0/cacheout.pl
/usr/lib/perl5/vendor_perl/5.34.0/chat2.pl
/usr/lib/perl5/vendor_perl/5.34.0/complete.pl
/usr/lib/perl5/vendor_perl/5.34.0/ctime.pl
/usr/lib/perl5/vendor_perl/5.34.0/dotsh.pl
/usr/lib/perl5/vendor_perl/5.34.0/exceptions.pl
/usr/lib/perl5/vendor_perl/5.34.0/fastcwd.pl
/usr/lib/perl5/vendor_perl/5.34.0/find.pl
/usr/lib/perl5/vendor_perl/5.34.0/finddepth.pl
/usr/lib/perl5/vendor_perl/5.34.0/flush.pl
/usr/lib/perl5/vendor_perl/5.34.0/ftp.pl
/usr/lib/perl5/vendor_perl/5.34.0/getcwd.pl
/usr/lib/perl5/vendor_perl/5.34.0/getopt.pl
/usr/lib/perl5/vendor_perl/5.34.0/getopts.pl
/usr/lib/perl5/vendor_perl/5.34.0/hostname.pl
/usr/lib/perl5/vendor_perl/5.34.0/importenv.pl
/usr/lib/perl5/vendor_perl/5.34.0/look.pl
/usr/lib/perl5/vendor_perl/5.34.0/newgetopt.pl
/usr/lib/perl5/vendor_perl/5.34.0/open2.pl
/usr/lib/perl5/vendor_perl/5.34.0/open3.pl
/usr/lib/perl5/vendor_perl/5.34.0/pwd.pl
/usr/lib/perl5/vendor_perl/5.34.0/shellwords.pl
/usr/lib/perl5/vendor_perl/5.34.0/stat.pl
/usr/lib/perl5/vendor_perl/5.34.0/syslog.pl
/usr/lib/perl5/vendor_perl/5.34.0/tainted.pl
/usr/lib/perl5/vendor_perl/5.34.0/termcap.pl
/usr/lib/perl5/vendor_perl/5.34.0/timelocal.pl
/usr/lib/perl5/vendor_perl/5.34.0/validate.pl
