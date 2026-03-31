# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           python-meh
Version:        0.52
Release:        %autorelease
Summary:        A python library for handling exceptions
License:        GPL-2.0-or-later
URL:            https://github.com/rhinstaller/python-meh
#!RemoteAsset
Source0:        https://github.com/rhinstaller/python-meh/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-dbus

Provides:       python3-meh
%python_provide python3-meh

Requires:       python3dist(dbus)
Requires:       python3dist(rpm)
Requires:       python3-gobject

%description
The python-meh package is a python library for handling, saving,
and reporting exceptions.

# No configure
%conf

%check
make test

%files
%doc COPYING
%{python3_sitelib}/*
%{_datadir}/python-meh

%changelog
%{?autochangelog}
