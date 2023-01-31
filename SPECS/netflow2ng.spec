Name:           netflow2ng
Version:        0.0.3
Release:        1%{?dist}
Summary:        Netflow2ng rpm packaging task

License:        MIT
URL:            https://github.com/synfinatic/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  make
BuildRequires:	epel-release
BuildRequires:	zeromq-devel
Requires:    bash

%description
The long-tail description for netflow2ng

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
make
mkdir -p %{buildroot}/usr/local/bin
cp dist/netflow2ng-0.0.3 %{buildroot}/usr/local/bin

%files
/usr/local/bin/netflow2ng-0.0.3
