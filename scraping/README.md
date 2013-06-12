# Scraping tools

## PDFs

## `pdftotext` from [xpdf](http://www.foolabs.com/xpdf/)

On OS X:

    brew install xpdf

Let's glance at a PDF description of some dataset:

    wget ftp://ftp.cdc.gov/pub/Health_statistics/NCHs/Dataset_Documentation/DVS/natality/UserGuide2010.pdf
    pdftotext -layout UserGuide2010.pdf UserGuide2010.txt

Because this PDF has tabular / structured data inside, we use the `-layout` flag.

Here's a snippet from the output file, `UserGuide2010.txt`:

```
Position          Len     Field             Description                   Reporting           Rev*    Values Definition
                                                                          Flag Position
1-6               6       FILLER            Filler                                                    Blank

7                 1       REVISION          Revision                                          U,R     A       Data based on the 2003 revision of the US Standard Birth
                                                                                                              Certificate (Revised)
                                                                                                      S       Data based on the 1989 revision of the US Standard Birth
                                                                                                              Certificate (Unrevised)

8-14              7       FILLER            Filler                                                    Blank

15-18             4       DOB_YY            Birth Year                                        U,R     2009    Year of birth

19-20             2       DOB_MM            Birth Month                                       U,R     01      January
                                                                                                      02      February
                                                                                                      03      March
                                                                                                      04      April
                                                                                                      05      May
                                                                                                      06      June
                                                                                                      07      July
                                                                                                      08      August
                                                                                                      09      September
                                                                                                      10      October
                                                                                                      11      November
                                                                                                      12      December

21-28             8       FILLER            Filler                                                    Blank

29                1       DOB_WK            Weekday                                           U,R     1       Sunday
                                                                                                      2       Monday
                                                                                                      3       Tuesday
                                                                                                      4       Wednesday
                                                                                                      5       Thursday
                                                                                                      6       Friday
                                                                                                      7       Saturday
```

Still messy, but more usable than the PDF.

Let's try without the layout:

    pdftotext '../Causality/Heckman (2005) - Scientific Model of Causality.pdf' heckman.txt

From the resulting `heckman.txt`:

> THE SCIENTIFIC MODEL OF CAUSALITY
>
> 65
>
> is correct so far as data description goes. Matching imposes just-identifying restrictions and in this sense--at a purely empirical level--is as good as any other just-identifying assumption in describing the data. However, the implied behavioral restrictions are not ``for free.'' Imposing that--conditional on X and Z or conditional on P(W) the marginal person entering a program is the same as the average person-- is a strong and restrictive implication of the conditional independence assumptions and is not a ``for free'' assumption in terms of its behavioral content.72 In the context of estimating the economic returns to schooling, it implies that, conditional on W, the economic return to schooling for persons who are just at the margin of going to school are the same as the return for persons with strong preferences for schooling. Introducing a distinction between X and Z allows the analyst to overcome the problem arising from perfect prediction of treatment assignment for some values of (X, Z) if there are some variables Z not in X. If P is a nontrivial function of Z (so P(X, Z) varies with Z for all X) and Z can be varied independently of X for all points of support of X,73 and if outcomes are d

## Webpages

* [phantomjs](http://phantomjs.org/)
* [python mechanize](http://wwwsearch.sourceforge.net/mechanize/)
