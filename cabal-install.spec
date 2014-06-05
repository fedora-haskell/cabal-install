# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1

Name:           cabal-install
Version:        1.20.0.2
Release:        1%{?dist}
Summary:        The command-line interface for Cabal and Hackage

License:        BSD
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel > 1.20.0
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-HTTP-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-zlib-devel
# End cabal-rpm deps

%description
The 'cabal' command-line program simplifies the process of managing Haskell
software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.


%prep
%setup -q


%build
%ghc_bin_build


%install
%ghc_bin_install


%files
%doc LICENSE
%doc README
%{_bindir}/cabal


%changelog
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
