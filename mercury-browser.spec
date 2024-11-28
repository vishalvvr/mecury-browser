Name:           mercury-browser
Version:        129.0.2
Release:        2%{?dist}
Summary:        Mercury Portable Browser
License:        MPL-2.0 
URL:            https://thorium.rocks/mercury
Source0:        https://github.com/Alex313031/Mercury/releases/download/v.%{VERSION}/mercury_%{VERSION}_linux_AVX2.zip#/%{NAME}.zip
Source1:        mercury_browser.desktop
Source2:        mercury_browser_logo.png
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Mercury is a lightweight and fast portable web browser designed for optimal performance.

# Disable debug package generation if not needed
%define debug_package %{nil}

%prep
# Unzip the source ZIP file
%autosetup -p1 -n mercury_%{VERSION}_linux_AVX2
rm -rf mercury/mercury

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/mercury-browser
mkdir -p %{buildroot}/usr/share/applications

# Install the binary and other necessary files
cp -r * %{buildroot}/opt/mercury-browser
cp %{SOURCE1} %{buildroot}/usr/share/applications/
cp %{SOURCE2} %{buildroot}/opt/mercury-browser/mercury

%clean
rm -rf %{buildroot}

%files
/opt/mercury-browser
/usr/share/applications/mercury_browser.desktop

%changelog
* Thu Nov 28 2024 vishalvvr <vishalvvr@fedoraproject.org> - 129.0.2-2
- update desktop file

* Thu Nov 28 2024 vishalvvr <vishalvvr@fedoraproject.org> - 129.0.2-1
- Initial RPM release of Mercury Portable Browser.