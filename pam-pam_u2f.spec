Summary:	A Pluggable Authentication Module for Universal 2nd Factor (U2C)
Summary(pl.UTF-8):	Moduł PAM dla urządzeń Universal 2nd Factor (U2C)
Name:		pam-pam_u2f
Version:	1.0.7
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/pam-u2f/Releases/pam_u2f-%{version}.tar.gz
# Source0-md5:	b34e91a03e7e454abd3b5374e76d6221
URL:		https://developers.yubico.com/pam-u2f
BuildRequires:	asciidoc
BuildRequires:	libu2f-host-devel
BuildRequires:	libu2f-server-devel
BuildRequires:	libxslt-progs
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
Requires:	pam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements PAM over U2F, providing an easy way to
integrate the YubiKey (or other U2F compliant authenticators) into
your existing infrastructure.

%description -l pl.UTF-8
Ten moduł implementuje PAM po U2F, zapewniając łatwy sposób
integrowania urządzeń YubiKey (lub innych urządzeń uwierzytelniających
zgodnych z U2F) z istniejącą infrastrukturą.

%prep
%setup -q -n pam_u2f-%{version}

%build
%configure \
	--disable-silent-rules \
	--with-pam-dir=/%{_lib}/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_lib}/security/pam_u2f.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) /%{_lib}/security/pam_u2f.so
%attr(755,root,root) %{_bindir}/pamu2fcfg
%{_mandir}/man1/pamu2fcfg.1*
%{_mandir}/man8/pam_u2f.8*
