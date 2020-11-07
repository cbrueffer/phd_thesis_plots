#!/usr/bin/env Rscript

#
# Flow chart for the SCAN-B dUTP strand-specific RNA-seq library prep.
#

# Inspiration:
# https://mikeyharper.uk/flowcharts-in-r-using-diagrammer/
# https://github.com/dr-harper/blog/blob/master/content/post/2018-05-01-flowcharts-in-r-using-diagrammer/planningGrouping.gv

library(magrittr)
library(DiagrammeR)
library(DiagrammeRsvg)
library(rsvg)

#DiagrammeR::grViz("snv_classification.gv")

export_svg(DiagrammeR::grViz("snv_classification.gv")) %>%
   charToRaw %>%
   rsvg_pdf("sv_classification.pdf")
