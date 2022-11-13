Name:		texlive-reverxii
Version:	63753
Release:	1
Summary:	Playing Reversi in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/reverxii
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reverxii.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reverxii.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Following the lead of xii.tex, this little (938 characters)
program that plays Reversi. (The program incorporates some
primitive AI.).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/reverxii

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
