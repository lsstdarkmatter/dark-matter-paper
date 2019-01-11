%Copyright (C) 1992-93 TCI Software Research, Inc.
%put into LaTeX2e format by ltg

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tcibook}

%%added by ltg to try to get 12pt to take
%\PassOptionsToPackage{12pt}{book}
%%end ltg


\typeout{TC Software Research, Inc. `tcibook' <13 Apr 93>.}
%
%% Uses tcilcomm.tex and book.cls
%
\input tcilcomm.tex
%

%%more ltg changes
\@ptoptinput{book.cls}%
%\RequirePackage[12pt]{book}
%end ltg


\typeout{TCI Document Style `tcibook' <5 Mar 92>.}
%
\def\adjustpagemargin{% adjust \oddsidemargin by \marginpartotal
 \marginpartotal\marginparwidth\advance\marginpartotal\marginparsep
 \if@reversemargin\advance\oddsidemargin\marginpartotal\fi
 \if@mparswitch
  \if@reversemargin\else\advance\evensidemargin\marginpartotal\fi
  \else\if@reversemargin\advance\evensidemargin\marginpartotal\fi
  \fi
 }%
% chapter opener page hooks
\def\chapter{%
 \clearchapterpage\thispagestyle{chapter}\global\@topnum\z@\@afterindentfalse 
 \secdef\@chapter\@schapter
 }%
\def\clearchapterpage{\cleardoublepage}%
\def\ps@chapter{\ps@plain}%
%
% figure captions
\long\def\@makecaption#1#2{%
 \addtolength{\hsize}{-36pt}
 \vskip 2pt 
 \edef\@tempa{#1}
 \ifx\@tempa\@empty\let\captsep\@empty\else\let\captsep\quad\fi
 \setbox\@tempboxa\hbox{\small{\bf #1.}\captsep{\sl #2}}%
 \ifdim \wd\@tempboxa >\hsize   % IF longer than one line:
  {\hspace*{18pt}\parbox{\hsize}{\small{\bf #1.}\captsep{\sl #2}\par}}%   THEN set as ordinary paragraph.
  \else                        %   ELSE  center.
  {\hspace*{18pt}\hbox to\hsize{\hfil\box\@tempboxa\hfil}}%
  \fi
 \addtolength{\hsize}{36pt}
 }%
%
\def\artbox#1{%
 \par\vbox{\hrule\vskip-.4pt
  \hbox to\hsize{\vrule\hfil\vrule height#1}\vskip-.4pt\hrule}%
 }%
%
\def\tlap#1{\vbox to\z@{\vss#1}}%
%
\def\dropletter#1{\par
 \setbox\z@\hbox spread3\p@{\Huge\bf#1\hfil}\dimen@\wd\z@\hangindent
 \dimen@\hangafter-\tw@
 \leavevmode{\setbox\z@\lastbox}\llap{\tlap{\box\z@
 \vskip-\normalbaselineskip}}%
 }%
%
\newdimen\sectionruledimen
\sectionruledimen.4pt
\def\makeparrule{%
 \def\par{%
  \endgraf\nobreak\vskip\lineskip\nointerlineskip
  \hbox to\hsize{\hskip\sectionbackskip\leaders\hrule height\sectionruledimen
  \hfil}%
  %\nointerlineskip
  }%
 }%
\def\prerule{\par
 \hbox to\hsize{\hskip-\marginpartotal\leaders\hrule height\sectionruledimen
 \hfil}%
 \nobreak
 }%
\newdimen\sectionbackskip
\sectionbackskip\z@
%
\def\ps@headings{%
 \let\@mkboth\markboth
 \def\@oddfoot{}%
 \def\@evenfoot{}%       No foot.
 \def\@oddhead{\rulefoot{\headfont\rectomark\hfil\null\foliofont\thepage}}
 \def\@evenhead{\rulefoot{\foliofont\thepage\hfil\headfont\versomark}}
 \let\chaptermark\markrectoverso
 \let\sectionmark\markrecto
 }%
\def\ps@footings{%
 \let\@mkboth\markboth
 \def\@oddhead{}%
 \def\@evenhead{}%       No head.
 \def\@oddfoot{\rulefoot{\headfont\rectomark\hfil\null\foliofont\thepage}}
 \def\@evenfoot{\rulefoot{\foliofont\thepage\hfil\headfont\versomark}}
 \let\chaptermark\markrectoverso
 \let\sectionmark\markrecto
 }%
\def\rectomark{\rightmark}%
\def\versomark{\leftmark}%
\def\markrectoverso#1{\markboth{\headcase{#1}}{\headcase{#1}}}%
\def\markrecto#1{\markright{\headcase{#1}}}%
%
\def\ps@plain{% used for chapter openers
 \def\@oddhead{}%
 \def\@evenhead{}%       No head.
 \def\@oddfoot{\hfil\null\foliofont\thepage}% Right footing.
 \def\@evenfoot{\foliofont\thepage\hfil}% Left footing.
 }%
\def\headfont{\sf}%
\def\foliofont{\rm}%
\let\headcase\@empty
%
\def\rulefoot#1{\rulefooting
 \@tempcnta\m@ne\if@mparswitch\ifodd\c@leaf\else\@tempcnta\@ne\fi\else\fi
 \if@reversemargin\@tempcnta-\@tempcnta\fi
 \ifnum\@tempcnta>\z@\hskip-\marginpartotal\fi
 \vtop{\hsize\textwidth\advance\hsize\marginpartotal\parfillskip
  \z@\parindent\z@\small\sl
  \ifruleabovefooting\hrule\prevdepth\z@\vskip18pt\vskip-\baselineskip\fi
  \leavevmode#1\par
  \ifrulebelowfooting\hrule\nointerlineskip\fi
  }%
 \ifnum\@tempcnta>\z@\else\hskip-\marginpartotal\fi
 }%
\newif\ifruleabovefooting
\newif\ifrulebelowfooting
\def\ruleabovefooting{\ruleabovefootingtrue\rulebelowfootingfalse}%
\def\rulebelowfooting{\ruleabovefootingfalse\rulebelowfootingtrue}%
\def\norulefooting{\ruleabovefootingfalse\rulebelowfootingfalse}%
\let\rulefooting\norulefooting
%
% Refer to corner of page as TeX's origin
\hoffset-1in
\voffset-1in
%
\@options

