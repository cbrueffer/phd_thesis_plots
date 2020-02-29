#!/usr/bin/env Rscript

#
# Plots a general confusion matrix similar to the one in
# https://en.wikipedia.org/wiki/Confusion_matrix
#
# Inspired by:
# https://stackoverflow.com/questions/23891140/r-how-to-visualize-confusion-matrix-using-the-caret-package


plot_confusion <- function() {
    # basic layout
    layout(matrix(c(1,1,2)))
    par(mar=c(2,2,2,2), bty='n')
    plot(c(100, 345), c(350, 500), type = "n", xlab="", ylab="", xaxt='n', yaxt='n')

    sweden.blue = rgb(0, 106, 168, max = 255, alpha = 255, names = "sweden.blue")
    sweden.yellow = rgb(254, 205, 0, max = 255, alpha = 255, names = "sweden.yellow")

    true.color = "#ccffcc"
    false.color = "#eedddd"
    class.color = 'grey94'
    # true.color = sweden.blue
    # false.color = sweden.yellow

    # outer labels
    text(120, 410, 'Predicted class', cex=2, srt=90, font=2)
    text(240, 500, 'Actual class', cex=2, font=2)

    # create the matrix
    rect(150, 470, 240, 410, col=true.color)  # upper left
    rect(240, 470, 330, 410, col=false.color)  # upper right
    rect(150, 350, 240, 410, col=false.color)  # lower left
    rect(240, 350, 330, 410, col=true.color)  # lower right

    # upper class boxes
    rect(150, 470, 240, 490, col=class.color)
    rect(240, 470, 330, 490, col=class.color)
    text(195, 480, "Class 1", cex=1.6, font=2)
    text(285, 480, "Class 2", cex=1.6, font=2)

    # left class boxes
    rect(130, 470, 150, 410, col=class.color)
    rect(130, 350, 150, 410, col=class.color)
    text(140, 440, "Class 1", cex=1.6, srt=90, font=2)
    text(140, 380, "Class 2", cex=1.6, srt=90, font=2)

    # add cell content
    text(195, 440, "True Positive\n(TP)", cex=2, font=2, col='black')
    text(195, 380, "False Negative\n(FN)", cex=2, font=2, col="black")
    text(285, 440, "False Positive\n(FP)", cex=2, font=2, col='black')
    text(285, 380, "True Negative\n(TN)", cex=2, font=2, col='black')
}


pdf(file="confusion-matrix.pdf", useDingbats = F)
plot_confusion()
dev.off()
