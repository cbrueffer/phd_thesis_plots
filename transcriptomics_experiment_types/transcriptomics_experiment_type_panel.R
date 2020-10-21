#!/usr/bin/env Rscript

library(magick)
library(ggplot2)
library(cowplot)

img.bulk = "bulk.jpeg"
img.singlecell = "singlecell.jpeg"
img.spatial = "spatial.jpeg"
img.original = "original.jpeg"

scale = 0.9
p1 <- cowplot::ggdraw() +
    cowplot::draw_image(img.bulk, scale = scale)
p2 <- cowplot::ggdraw() +
    cowplot::draw_image(img.singlecell, scale = scale)
p3 <- cowplot::ggdraw() +
    cowplot::draw_image(img.spatial, scale = scale)
p4 <- cowplot::ggdraw() +
    cowplot::draw_image(img.original, scale = scale)
cowplot::plot_grid(p1, p2, p3, p4,
                   nrow=2, ncol=2,
                   labels = c("Bulk RNA-seq", "Single-cell RNA-seq", "Spatial Transcriptomics", "Original Organ"),
                   label_x = c(0, 0, 0, 0),
                   hjust = c(-0.43, -0.18, -0.06, -0.42),
                   label_size=16)

ggsave2("transcriptomics_experiment_types.png")