# revision 25711
# category Package
# catalog-ctan /language/arabic/arabtex
# catalog-date 2012-03-20 14:44:41 +0100
# catalog-license lppl
# catalog-version 3.17 
Name:		texlive-arabtex
Version:	3.17
Release:	9
Summary:	Macros and fonts for typesetting Arabic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/arabic/arabtex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arabtex.doc.tar.xz
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
%{_texmfdistdir}/fonts/map/dvips/arabtex/arabtex.map
%{_texmfdistdir}/fonts/source/public/arabtex/arabsymb.mf
%{_texmfdistdir}/fonts/source/public/arabtex/hcaption.mf
%{_texmfdistdir}/fonts/source/public/arabtex/hcbase.mf
%{_texmfdistdir}/fonts/source/public/arabtex/hclassic.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nash.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nash14.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nash14bf.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nashbase.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nashchar.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nashdia.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nashdig.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nashlig.mf
%{_texmfdistdir}/fonts/source/public/arabtex/nashspec.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xarbsymb.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnsh.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnsh14.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnsh14bf.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnshbase.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnshchar.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnshdia.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnshdig.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnshlig.mf
%{_texmfdistdir}/fonts/source/public/arabtex/xnshspec.mf
%{_texmfdistdir}/fonts/tfm/public/arabtex/hcaption.tfm
%{_texmfdistdir}/fonts/tfm/public/arabtex/hclassic.tfm
%{_texmfdistdir}/fonts/tfm/public/arabtex/nash14.tfm
%{_texmfdistdir}/fonts/tfm/public/arabtex/nash14bf.tfm
%{_texmfdistdir}/fonts/tfm/public/arabtex/xnsh14.tfm
%{_texmfdistdir}/fonts/tfm/public/arabtex/xnsh14bf.tfm
%{_texmfdistdir}/fonts/tfm/public/arabtex/yarborn.tfm
%{_texmfdistdir}/fonts/type1/public/arabtex/hcaption-4.pfb
%{_texmfdistdir}/fonts/type1/public/arabtex/hclassic-4.pfb
%{_texmfdistdir}/fonts/type1/public/arabtex/xnsh14.pfb
%{_texmfdistdir}/fonts/type1/public/arabtex/xnsh14bf.pfb
%{_texmfdistdir}/tex/latex/arabtex/Uxnsh.fd
%{_texmfdistdir}/tex/latex/arabtex/abidir.sty
%{_texmfdistdir}/tex/latex/arabtex/abjad.sty
%{_texmfdistdir}/tex/latex/arabtex/aboxes.sty
%{_texmfdistdir}/tex/latex/arabtex/acjk.sty
%{_texmfdistdir}/tex/latex/arabtex/acmd.sty
%{_texmfdistdir}/tex/latex/arabtex/aconfig.sty
%{_texmfdistdir}/tex/latex/arabtex/aedpatch.sty
%{_texmfdistdir}/tex/latex/arabtex/afonts.sty
%{_texmfdistdir}/tex/latex/arabtex/afonts0.sty
%{_texmfdistdir}/tex/latex/arabtex/afonts1.sty
%{_texmfdistdir}/tex/latex/arabtex/afonts2.sty
%{_texmfdistdir}/tex/latex/arabtex/afoot.sty
%{_texmfdistdir}/tex/latex/arabtex/alatex.sty
%{_texmfdistdir}/tex/latex/arabtex/aligs.sty
%{_texmfdistdir}/tex/latex/arabtex/alists.sty
%{_texmfdistdir}/tex/latex/arabtex/alocal.sty
%{_texmfdistdir}/tex/latex/arabtex/altxext.sty
%{_texmfdistdir}/tex/latex/arabtex/amac.sty
%{_texmfdistdir}/tex/latex/arabtex/aoutput.sty
%{_texmfdistdir}/tex/latex/arabtex/aparse.sty
%{_texmfdistdir}/tex/latex/arabtex/apatch.sty
%{_texmfdistdir}/tex/latex/arabtex/arababel.sty
%{_texmfdistdir}/tex/latex/arabtex/arabart.cls
%{_texmfdistdir}/tex/latex/arabtex/arabaux.sty
%{_texmfdistdir}/tex/latex/arabtex/arabbook.cls
%{_texmfdistdir}/tex/latex/arabtex/arabchrs.sty
%{_texmfdistdir}/tex/latex/arabtex/arabext.sty
%{_texmfdistdir}/tex/latex/arabtex/arabrep.cls
%{_texmfdistdir}/tex/latex/arabtex/arabrep1.cls
%{_texmfdistdir}/tex/latex/arabtex/arabskel.sty
%{_texmfdistdir}/tex/latex/arabtex/arabsymb.sty
%{_texmfdistdir}/tex/latex/arabtex/arabtex-doc.tex
%{_texmfdistdir}/tex/latex/arabtex/arabtex.sty
%{_texmfdistdir}/tex/latex/arabtex/arabtex.tex
%{_texmfdistdir}/tex/latex/arabtex/arabtoks.sty
%{_texmfdistdir}/tex/latex/arabtex/arwindoc.tex
%{_texmfdistdir}/tex/latex/arabtex/ascan.sty
%{_texmfdistdir}/tex/latex/arabtex/asect.sty
%{_texmfdistdir}/tex/latex/arabtex/asize10.clo
%{_texmfdistdir}/tex/latex/arabtex/asize11.clo
%{_texmfdistdir}/tex/latex/arabtex/asize12.clo
%{_texmfdistdir}/tex/latex/arabtex/asmo449.sty
%{_texmfdistdir}/tex/latex/arabtex/asmo449a.sty
%{_texmfdistdir}/tex/latex/arabtex/atabg.sty
%{_texmfdistdir}/tex/latex/arabtex/atrans.sty
%{_texmfdistdir}/tex/latex/arabtex/awrite.sty
%{_texmfdistdir}/tex/latex/arabtex/bhs.sty
%{_texmfdistdir}/tex/latex/arabtex/bhslabel.sty
%{_texmfdistdir}/tex/latex/arabtex/buck.sty
%{_texmfdistdir}/tex/latex/arabtex/captions.def
%{_texmfdistdir}/tex/latex/arabtex/cp1256.sty
%{_texmfdistdir}/tex/latex/arabtex/etrans.sty
%{_texmfdistdir}/tex/latex/arabtex/gedalin.sty
%{_texmfdistdir}/tex/latex/arabtex/guha.tex
%{_texmfdistdir}/tex/latex/arabtex/hebchrs.sty
%{_texmfdistdir}/tex/latex/arabtex/hebsymb.sty
%{_texmfdistdir}/tex/latex/arabtex/hebtex.sty
%{_texmfdistdir}/tex/latex/arabtex/hebtex.tex
%{_texmfdistdir}/tex/latex/arabtex/hecmd.sty
%{_texmfdistdir}/tex/latex/arabtex/hefonts.sty
%{_texmfdistdir}/tex/latex/arabtex/hefonts0.sty
%{_texmfdistdir}/tex/latex/arabtex/hefonts1.sty
%{_texmfdistdir}/tex/latex/arabtex/hefonts2.sty
%{_texmfdistdir}/tex/latex/arabtex/heparse.sty
%{_texmfdistdir}/tex/latex/arabtex/hepatch.sty
%{_texmfdistdir}/tex/latex/arabtex/hescan.sty
%{_texmfdistdir}/tex/latex/arabtex/hetrans.sty
%{_texmfdistdir}/tex/latex/arabtex/hewrite.sty
%{_texmfdistdir}/tex/latex/arabtex/hmac.sty
%{_texmfdistdir}/tex/latex/arabtex/isiri.sty
%{_texmfdistdir}/tex/latex/arabtex/iso88596.sty
%{_texmfdistdir}/tex/latex/arabtex/kashmiri.tex
%{_texmfdistdir}/tex/latex/arabtex/ligtable.tex
%{_texmfdistdir}/tex/latex/arabtex/malay.tex
%{_texmfdistdir}/tex/latex/arabtex/nashbf.sty
%{_texmfdistdir}/tex/latex/arabtex/omar.tex
%{_texmfdistdir}/tex/latex/arabtex/raw.sty
%{_texmfdistdir}/tex/latex/arabtex/saw.sty
%{_texmfdistdir}/tex/latex/arabtex/sindhi.tex
%{_texmfdistdir}/tex/latex/arabtex/sotoku.sty
%{_texmfdistdir}/tex/latex/arabtex/twoblks.sty
%{_texmfdistdir}/tex/latex/arabtex/uheb.fd
%{_texmfdistdir}/tex/latex/arabtex/uighur.tex
%{_texmfdistdir}/tex/latex/arabtex/unash.fd
%{_texmfdistdir}/tex/latex/arabtex/utf8.sty
%{_texmfdistdir}/tex/latex/arabtex/utfcode.sty
%{_texmfdistdir}/tex/latex/arabtex/verses.sty
%{_texmfdistdir}/tex/latex/arabtex/witbhs.sty
%{_texmfdistdir}/tex/latex/arabtex/xarbskel.sty
%{_texmfdistdir}/tex/latex/arabtex/xarbsymb.sty
%{_texmfdistdir}/tex/latex/arabtex/yiddish.sty
%doc %{_texmfdistdir}/doc/latex/arabtex/announce.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/arabtex-doc.pdf
%doc %{_texmfdistdir}/doc/latex/arabtex/arabtex.doc
%doc %{_texmfdistdir}/doc/latex/arabtex/arabtex.faq
%doc %{_texmfdistdir}/doc/latex/arabtex/arabtex.gif
%doc %{_texmfdistdir}/doc/latex/arabtex/arabtex.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/arabtex1.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/arabtex2.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/changes.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/changes.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/changes2.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/chg311.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/chg311a.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/chg311b.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/chg311c.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/chg311d.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/guha.ps
%doc %{_texmfdistdir}/doc/latex/arabtex/hebrew.305
%doc %{_texmfdistdir}/doc/latex/arabtex/install.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/lppl.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/malay.ps
%doc %{_texmfdistdir}/doc/latex/arabtex/manifest.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/miktex.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/miktex.mai
%doc %{_texmfdistdir}/doc/latex/arabtex/new1.gif
%doc %{_texmfdistdir}/doc/latex/arabtex/new2.gif
%doc %{_texmfdistdir}/doc/latex/arabtex/readme.305
%doc %{_texmfdistdir}/doc/latex/arabtex/readme.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/refer.htm
%doc %{_texmfdistdir}/doc/latex/arabtex/sindhi.ps
%doc %{_texmfdistdir}/doc/latex/arabtex/tetex.txt
%doc %{_texmfdistdir}/doc/latex/arabtex/uighur.ps
%doc %{_texmfdistdir}/doc/latex/arabtex/xarbsymb.dat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.17-1
+ Revision: 787564
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.11s-2
+ Revision: 749320
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.11s-1
+ Revision: 717848
- texlive-arabtex
- texlive-arabtex
- texlive-arabtex
- texlive-arabtex
- texlive-arabtex

