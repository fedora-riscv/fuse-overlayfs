%global git0 https://github.com/containers/%{name}
%global commit0 ff65edefc7fa70890a035449d720ae71d09ffe70
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: fuse-overlayfs
Version: 0.3
Release: 3.dev.git%{shortcommit0}%{?dist}
Summary: FUSE overlay+shiftfs implementation for rootless containers
License: GPLv3+
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: fuse3-devel
BuildRequires: gcc
BuildRequires: git
BuildRequires: make
Provides: bundled(gnulib) = cb634d40c7b9bbf33fa5198d2e27fdab4c0bf143

%description
%{summary}.

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%autosetup -Sgit -n %{name}-%{commit0}

%build
./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make}

%install
make DESTDIR=%{buildroot} install

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Wed Feb 13 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.3-3.dev.gitff65ede
- built commit ff65ede

* Tue Jan 15 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.3-1.dev.git6d269aa
- built commit 6d269aa

* Tue Jan 08 2019 Giuseppe Scrivano <gscrivan@redhat.com> - 0.1-9.dev.git5c9742d
- built commit 5c9742d

* Thu Dec 20 2018 Giuseppe Scrivano <gscrivan@redhat.com> - 0.1-8.dev.git91bb401
- built commit 91bb401

* Tue Dec 18 2018 Giuseppe Scrivano <gscrivan@redhat.com> - 0.1-7.dev.gitf48e1ef
- built commit f48e1ef

* Fri Nov 23 2018 Giuseppe Scrivano <gscrivan@redhat.com> - 0.1-6.dev.git3d48bf9
- built commit 3d48bf9

* Fri Aug 10 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-5.dev.gitd40ac75
- built commit d40ac75

* Mon Jul 30 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-4.dev.git79c70fd
- Resolves: #1609598 - initial upload to Fedora
- bundled gnulib

* Mon Jul 30 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-3.dev.git79c70fd
- correct license field

* Mon Jul 30 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-2.dev.git79c70fd
- fix license

* Sun Jul 29 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-1.dev.git13575b6
- First package for Fedora
