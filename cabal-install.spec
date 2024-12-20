# generated by cabal-rpm-2.2.2 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

%global pkg_name cabal-install
%global pkgver %{pkg_name}-%{version}

%if 0%{?fedora} < 40
%global ghc_major 9.6
%global ghc_name ghc%{ghc_major}
%endif
%bcond_with compiler_default

%bcond_with revision

Name:           %{pkg_name}
Version:        3.12.1.0
Release:        1%{?dist}
Summary:        The command-line interface for Cabal and Hackage

License:        BSD-3-Clause
Url:            https://hackage.haskell.org/package/cabal-install
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with revision}
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{name}.cabal#/%{pkgver}.cabal
%endif
# End cabal-rpm sources
Source2:        cabal-install.sh

# Begin cabal-rpm deps:
%if %{with revision}
BuildRequires:  dos2unix
%endif
BuildRequires:  ghc-rpm-macros
%if %{defined ghc_name}
BuildRequires:  %{ghc_name}-devel
%if %{with compiler_default}
BuildRequires:  %{ghc_name}-compiler-default
%endif
BuildRequires:  zlib-devel
%else
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Cabal-syntax-devel
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cabal-install-solver-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-echo-devel
BuildRequires:  ghc-edit-distance-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hackage-security-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-lukko-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-regex-base-devel
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-resolv-devel
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tar-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-zlib-devel
%endif
BuildRequires:  cabal-install
# End cabal-rpm deps

# for /etc/bash_completion.d/
Requires:       filesystem
# nslookup used for mirror dns
Requires:       bind-utils
# for /etc/profile.d/
Requires:       setup
Recommends:     (ghc or ghc8.10 or ghc9.0 or ghc9.2 or ghc9.4 or ghc9.6 or ghc9.8 or ghc9.10)
Recommends:     zlib-devel

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.


%prep
# Begin cabal-rpm setup:
%setup -q
%if %{with revision}
dos2unix -k -n %{SOURCE1} %{name}.cabal
%endif
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
cabal update %{?ghc_major:%{!?with_compiler_default:-w ghc-%{ghc_major}}}
# End cabal-rpm build


%install
# Begin cabal-rpm install
mkdir -p %{buildroot}%{_bindir}
%if %{defined fedora} || 0%{?rhel} >= 9
%ghc_set_gcc_flags
cabal install %{?ghc_major:%{!?with_compiler_default:-w ghc-%{ghc_major}}} --install-method=copy --enable-executable-stripping --installdir=%{buildroot}%{_bindir}
%else
for i in .cabal-sandbox/bin/*; do
strip -s -o %{buildroot}%{_bindir}/$(basename $i) $i
done
%endif
# End cabal-rpm install

install -pm 644 -D -t %{buildroot}%{_datadir}/bash-completion/completions/ bash-completion/cabal

install -pm 644 -D -t %{buildroot}%{_sysconfdir}/profile.d/ %{SOURCE2}


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md changelog
%{_bindir}/cabal
# End cabal-rpm files
%config(noreplace) %{_sysconfdir}/profile.d/cabal-install.sh
%{_datadir}/bash-completion/completions/cabal


%changelog
* Fri Dec 20 2024 Jens Petersen <petersen@redhat.com> - 3.12.1.0-1
- https://github.com/haskell/cabal/blob/master/release-notes/cabal-install-3.12.1.0.md

* Fri Dec 20 2024 Jens Petersen <petersen@redhat.com> - 3.10.3.0-2
- build with cabal-install-solver-3.10.3.0

* Fri Dec 20 2024 Jens Petersen <petersen@redhat.com> - 3.10.3.0-1
- https://github.com/haskell/cabal/blob/master/release-notes/cabal-install-3.10.3.0.md

* Mon Nov  6 2023 Jens Petersen <petersen@redhat.com> - 3.10.2.0-1
- https://github.com/haskell/cabal/blob/master/release-notes/cabal-install-3.10.2.0.md

* Fri Nov  3 2023 Jens Petersen <petersen@redhat.com> - 3.10.1.0-2
- workaround pkgconf-1.9 --modversion regression breaking pkgconfig-depends

* Tue May 30 2023 Jens Petersen <petersen@redhat.com> - 3.10.1.0-1
- https://github.com/haskell/cabal/blob/master/release-notes/cabal-install-3.10.1.0.md

* Fri Aug 12 2022 Jens Petersen <petersen@redhat.com> - 3.8.1.0-1
- https://github.com/haskell/cabal/blob/master/release-notes/cabal-install-3.8.1.0.md

* Sun May  1 2022 Jens Petersen <petersen@redhat.com> - 3.6.2.0-1
- https://github.com/haskell/cabal/tree/master/release-notes
- build with ghc9.2

* Sun May  1 2022 Jens Petersen <petersen@redhat.com> - 3.4.1.0-2
- replace ghc-compiler requires with recommends ghc or ghcX.Y
- build with ghc9.0

* Wed Dec  1 2021 Jens Petersen <petersen@redhat.com> - 3.4.1.0-1
- 3.4.1.0 bugfix release

* Wed Dec  1 2021 Jens Petersen <petersen@redhat.com> - 3.4.0.0-1
- https://github.com/haskell/cabal/blob/master/release-notes/cabal-install-3.4.0.0.md

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
