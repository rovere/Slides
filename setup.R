#!/usr/bin/env Rscript

install.packages("devtools", repo="http://stat.ethz.ch/CRAN/")
install.packages("knitr", repo="http://stat.ethz.ch/CRAN/")
require("devtools")
install_github("slidify", "ramnathv")
install_github("slidifyLibraries", "ramnathv")
