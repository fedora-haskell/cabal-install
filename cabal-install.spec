# https://fedoraproject.org/wiki/Packaging:Haskell

# nothing to see here
%global debug_package %{nil}

Name:           cabal-install
Version:        2.0.0.1
Release:        1%{?dist}
Summary:        The command-line interface for Cabal and Hackage

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        cabal-install.sh

BuildRequires:  ghc-Cabal-devel > 2.0
#BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
#BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-array-devel
#BuildRequires:  ghc-async-devel
#BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
#BuildRequires:  ghc-cryptohash-sha256-devel
#BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
#BuildRequires:  ghc-echo-devel
#BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-hackage-security-devel
#BuildRequires:  ghc-hashable-devel
#BuildRequires:  ghc-mtl-devel
#BuildRequires:  ghc-network-devel
#BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
#BuildRequires:  ghc-random-devel
#BuildRequires:  ghc-stm-devel
#BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
#BuildRequires:  ghc-zlib-devel
# End cabal-rpm deps
BuildRequires:  zlib-devel
# for /etc/bash_completion.d/
Requires:       filesystem
# for /etc/profile.d/
Requires:       setup
# added for F26
Obsoletes:      %{name}-common < %{version}-%{release}
Obsoletes:      %{name}-static < %{version}-%{release}

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs from Hackage.


%prep
%setup -q


%build
# allow building with bootstrap ghc
export EXTRA_CONFIGURE_OPTS=""
export NO_DOCUMENTATION=1
./bootstrap.sh


%install
install -D dist/build/cabal/cabal %{buildroot}%{_bindir}/cabal

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
cp -p bash-completion/cabal $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d


%files
%doc LICENSE
%doc README.md
%doc changelog
%{_bindir}/cabal
%config(noreplace) %{_sysconfdir}/bash_completion.d/cabal
%config(noreplace) %{_sysconfdir}/profile.d/cabal-install.sh


%changelog
* Fri Dec  8 2017 Jens Petersen <petersen@redhat.com> - 2.0.0.1-1
- update to 2.0.0.1

* Fri Feb 10 2017 Jens Petersen <petersen@fedoraproject.org> - 1.24.0.2-2
- obsolete common and static subpackages

* Fri Dec  9 2016 Jens Petersen <petersen@redhat.com> - 1.24.0.2-1
- 1.24.0.2 release

* Fri Nov 11 2016 Jens Petersen <petersen@redhat.com> - 1.24.0.1-1
- update to 1.24.0.1

* Wed Jul 20 2016 Jens Petersen <petersen@redhat.com> - 1.24.0.0-1
- update to 1.24.0.0

* Mon Feb 29 2016 Jens Petersen <petersen@redhat.com> - 1.23.0.0-1
- update to candidate 1.23.0.0 for ghc8

* Wed Feb 17 2016 Jens Petersen <petersen@redhat.com> - 1.22.8.0-1
- update to 1.22.8.0

* Tue Jan 19 2016 Jens Petersen <petersen@redhat.com> - 1.22.7.0-3
- no cabal-install-common for epel

* Tue Jan 12 2016 Jens Petersen <petersen@redhat.com> - 1.22.7.0-2
- require Fedora cabal-install-common rather than conflicting with it

* Fri Jan  8 2016 Jens Petersen <petersen@redhat.com> - 1.22.7.0-1
- update to 1.22.7.0

* Mon Jul 13 2015 Jens Petersen <petersen@redhat.com> - 1.22.6.0-1
- 1.22.6.0

* Wed May 13 2015 Jens Petersen <petersen@redhat.com> - 1.22.4.0-1
- 1.22.4.0

* Mon Feb 23 2015 Jens Petersen <petersen@fedoraproject.org> - 1.22.0.1-1
- update to 1.22.0.1

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 1.22.0.0-3
- add bash_completion.d and profile.d files

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 1.22.0.0-2
- build with ghc-7.10 and without old-time dep

* Fri Jan 16 2015 Jens Petersen <petersen@redhat.com> - 1.22.0.0-1
- update to 1.22.0.0
- build with bootstrap.sh

* Thu Dec 25 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.4-1
- update to 1.20.0.4

* Thu Jun  5 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.2-1
- update to 1.20.0.2

* Wed May  7 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.1-2
- copr rebuild

* Wed May  7 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.1-1
- update to 1.20.0.1

* Mon Apr 21 2014 Jens Petersen <petersen@redhat.com> - 1.20.0.0-1
- update to 1.20.0.0

* Thu Mar  6 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.18.0.3
- spec file generated by cabal-rpm-0.8.10
