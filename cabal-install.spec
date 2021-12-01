# generated by cabal-rpm-2.1.0 --standalone --stream hackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

Name:           cabal-install
Version:        3.2.0.0
Release:        2%{?dist}
Summary:        The command-line interface for Cabal and Hackage

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources
Source1:        cabal-install.sh
# backport fix from https://github.com/haskell/cabal/issues/5813
Patch0:         https://github.com/haskell/cabal/commit/442869918260a7bb3f0cb0698eaeaeb6dae2c4f6.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
%if 0%{?fedora} || 0%{?rhel} == 7
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
%if 0%{?fedora}
BuildRequires:  ghc-base16-bytestring-devel
%endif
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
%if 0%{?fedora}
BuildRequires:  ghc-cryptohash-sha256-devel
%endif
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
%if 0%{?fedora}
BuildRequires:  ghc-echo-devel
%endif
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-filepath-devel
%if 0%{?fedora}
BuildRequires:  ghc-hackage-security-devel
%endif
BuildRequires:  ghc-hashable-devel
%if 0%{?fedora}
BuildRequires:  ghc-lukko-devel
%endif
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
%if 0%{?fedora}
BuildRequires:  ghc-network-uri-devel
%endif
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
%if 0%{?fedora}
BuildRequires:  ghc-resolv-devel
%endif
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-zlib-devel
%else
BuildRequires:  ghc-devel
BuildRequires:  zlib-devel
%endif
BuildRequires:  cabal-install > 1.18
# End cabal-rpm deps
## for hackage-security
#BuildRequires:  ghc-template-haskell-devel
#BuildRequires:  zlib-devel

# cabal-install 2.0 does not require Cabal
Requires:       ghc-compiler
# for /etc/bash_completion.d/
Requires:       filesystem
# nslookup used for mirror dns
Requires:       bind-utils
# for /etc/profile.d/
Requires:       setup
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     ghc-devel
Recommends:     zlib-devel
%endif

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup
%patch0 -p2 -b .sdist


%build
# Begin cabal-rpm build:
%global cabal cabal
cabal v2-update
cabal v2-build
# End cabal-rpm build


%install
# Begin cabal-rpm install
# End cabal-rpm install
install -D dist-newstyle/build/*/ghc-%{ghc_version}/cabal-install-%{version}/build/cabal/cabal %{buildroot}%{_bindir}/cabal

install -pm 644 -D -t %{buildroot}%{_datadir}/bash-completion/completions/ bash-completion/cabal

install -pm 644 -D -t %{buildroot}%{_sysconfdir}/profile.d/ %{SOURCE1}


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md changelog
%{_bindir}/cabal
# End cabal-rpm files
%config(noreplace) %{_sysconfdir}/profile.d/cabal-install.sh
%{_datadir}/bash-completion/completions/cabal


%changelog
* Thu Sep 23 2021 Jens Petersen <petersen@redhat.com> - 3.2.0.0-2
- sync with Fedora package

* Tue Apr 14 2020 Jens Petersen <petersen@redhat.com> - 3.2.0.0-1
- update to 3.2.0.0

* Tue Mar  3 2020 Jens Petersen <petersen@redhat.com> - 3.0.0.0-1
- update to 3.0.0.0

* Fri Jul 26 2019 Jens Petersen <petersen@redhat.com> - 2.4.1.0-1
- update to 2.4.1.0

* Sun Sep 23 2018 Jens Petersen <petersen@redhat.com> - 2.4.0.0-1
- update to 2.4.0.0

* Fri Mar 30 2018 Jens Petersen <petersen@redhat.com> - 2.2.0.0-1
- update to 2.2.0.0

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
