# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1

Name:           cabal-install
Version:        1.22.0.0
Release:        2%{?dist}
Summary:        The command-line interface for Cabal and Hackage

License:        BSD
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
#BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
#BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-mtl-devel
#BuildRequires:  ghc-network-devel
#BuildRequires:  ghc-old-time-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
#BuildRequires:  ghc-random-devel
#BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
#BuildRequires:  ghc-zlib-devel
# End cabal-rpm deps
BuildRequires:  zlib-devel

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.


%prep
%setup -q


%build
# allow building with bootstrap ghc
export EXTRA_CONFIGURE_OPTS=""
export NO_DOCUMENTATION=1
./bootstrap.sh


%install
install -D dist/build/cabal/cabal %{buildroot}%{_bindir}/cabal


%files
%doc LICENSE
%doc README.md
%doc changelog
%{_bindir}/cabal


%changelog
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
