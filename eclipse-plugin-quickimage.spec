Summary:	QuickImage - plugin for Eclipse
Summary(pl.UTF-8):   QuickImage - wtyczka do środowiska Eclipse
Name:		eclipse-plugin-quickimage
Version:	0.2.0
Release:	1
License:	CPL
Group:		Development/Languages
Source0:	http://psnet.nu/eclipse/quickimage/files/nu.psnet.quickimage_%{version}.zip
# Source0-md5:	d6c5d7c7baf450d907123888f876a4eb
URL:		http://psnet.nu/eclipse/quickimage/
BuildRequires:	unzip
Requires:	eclipse >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86/x86/;s/athlon/x86/;s/pentium./x86/')
%define		_eclipsedir	%{_libdir}/eclipse

%description
The QuickImage plugin provides an eclipse-editor for viewing images.
You can browse images one by one in fullsize or all as thumbnails. Use
the toolbar to navigate or by single/double clicking the images. By
default QuickImage associates its editor with .gif .jpg .jpeg .png
.bmp .ico .

%description -l pl.UTF-8
Wtyczka QuickImage dodaje edytor dla eclipse do podglądu obrazków.
Umożliwia przeglądanie obrazków jeden po drugim w pełnym rozmiarze,
lub wszystkich jako miniaturkek. Domyślnie QuickImage kojarzy swój
edytor z .gif .jpg .jpeg .png .bmp .ico .

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/plugins

cp -r * $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_eclipsedir}
%dir %{_eclipsedir}/plugins
%{_eclipsedir}/plugins/*
