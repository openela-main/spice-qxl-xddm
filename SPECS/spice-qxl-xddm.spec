%global spice_data_dir  %{_datadir}/spice

Name: spice-qxl-xddm
Version: 0.1
Release: 24%{?dist}.2
License: GPLv2
Summary: A QXL driver for Windows 7 virtual machines
Group: Virtualization/Management
URL: http://www.spice-space.org

Source0: qxl_w7_x86.zip
Source1: qxl_xp_x86.zip
Source2: qxl_w7_x64.zip
Source3: spice-qxl-xddm-0.1-24.2-sources.zip
Source4: qxl_msi.zip
Source5: spice-qxl-xddm-0.1-24.2-spec.zip
Source6: qxl_8k2R2_x64.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
A QXL driver for Windows 7 virtual machines.
QXL is a paravirtualized display driver and a part of SPICE project.

%prep

%build

%install
rm -rf %{buildroot}
/usr/bin/install -d %{buildroot}%{spice_data_dir}

/usr/bin/unzip %{SOURCE4}
/bin/cp *.msi %{buildroot}%{spice_data_dir}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{spice_data_dir}/*.msi


%changelog
* Wed Mar 11 2020 Uri Lublin <uril@redhat.com> - 0.1-24.2
- Build for 8.2
- Resolves: rhbz#1757771

