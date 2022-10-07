%global git0 https://github.com/containers/%{name}

%global built_tag v1.9
%global built_tag_strip %(b=%{built_tag}; echo ${b:1})
%global gen_version %(b=%{built_tag_strip}; echo ${b/-/"~"})

%{!?_modulesloaddir:%global _modulesloaddir %{_usr}/lib/modules-load.d}

Name: fuse-overlayfs
Version: %{gen_version}
Release: %autorelease
License: GPLv3+
Summary: FUSE overlay+shiftfs implementation for rootless containers
URL: https://github.com/containers/%{name}
# Tarball fetched from upstream
Source0: %{url}/archive/%{built_tag}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
Requires: fuse3
Requires: kmod
BuildRequires: fuse3-devel
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: make
BuildRequires: systemd-rpm-macros
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
%autosetup -Sgit %{name}-%{built_tag_strip}

%build
./autogen.sh
./configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__make}

%install
%make_install
install -d %{buildroot}%{_modulesloaddir}
echo fuse > %{buildroot}%{_modulesloaddir}/fuse-overlayfs.conf

%post
modprobe fuse > /dev/null 2>&1 || :

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_modulesloaddir}/fuse-overlayfs.conf

%changelog
%autochangelog
