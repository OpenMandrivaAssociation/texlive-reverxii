# revision 24976
# category Package
# catalog-ctan /macros/plain/contrib/reverxii
# catalog-date 2011-12-30 00:42:15 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-reverxii
Version:	20170414
Release:	1
Summary:	Playing Reversi in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/reverxii
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reverxii.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/reverxii.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Following the lead of xii.tex, this little (938 characters)
program that plays Reversi. (The program incorporates some
primitive AI.).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/reverxii/README
%doc %{_texmfdistdir}/doc/plain/reverxii/reverxii.pdf
%doc %{_texmfdistdir}/doc/plain/reverxii/reverxii.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111230-1
+ Revision: 759052
- texlive-reverxii
- texlive-reverxii

