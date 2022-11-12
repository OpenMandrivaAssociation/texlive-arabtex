Name:		texlive-arabtex
Version:	64260
Release:	1
Summary:	Macros and fonts for typesetting Arabic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/arabic/arabtex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabtex.r64260.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabtex.doc.r64260.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ArabTeX is a package extending the capabilities of TeX/LaTeX to
generate Arabic and Hebrew text. Input may be in ASCII
transliteration or other encodings (including UTF-8); output
may be Arabic, Hebrew, or any of several languages that use the
Arabic script. ArabTeX consists of a TeX macro package and
Arabic and Hebrew fonts (provided both in Metafont format and
Adobe Type 1). The Arabic font is presently only available in
the Naskhi style. ArabTeX will run with Plain TeX and also with
LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/arabtex
%{_texmfdistdir}/fonts/source/public/arabtex
%{_texmfdistdir}/fonts/tfm/public/arabtex
%{_texmfdistdir}/fonts/type1/public/arabtex
%{_texmfdistdir}/tex/latex/arabtex
%doc %{_texmfdistdir}/doc/latex/arabtex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
