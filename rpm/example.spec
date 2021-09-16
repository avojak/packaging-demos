# Use the version defined in the VERSION file plus a qualifier (if provided by the CI system)
%global _version %(sh -c "cat VERSION")%{?_ci_version_qualifier}
# Use the build number if provided by the CI system, otherwise default to 1
%global _release %{?_ci_build}%{?!_ci_build:1}%{?dist}

Name:       example
Version:    %{_version}
Release:    %{_release}
Summary:    Example of RPM packaging
License:    GPLv3

Source0:    hello

%description
This is an example of RPM packaging and versioning.

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}/hello

%files
%{_bindir}/hello