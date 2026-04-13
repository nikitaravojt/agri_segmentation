
## Result_6 13/04/26. Baseline + kfold + cosineLR + augmentations (geometric + colour jitter) + 0.4 dropout for 50 epochs
K-Fold Results:
IoU      | bg: 0.989 crop: 0.710 weed: 0.683
Accuracy | bg: 0.996 crop: 0.830 weed: 0.775
BFScore  | bg: 0.892 crop: 0.719 weed: 0.753
Notes:
- Dropout as extra regularisation hurts slightly. Will remove.

## Result_5 13/04/26. Baseline + kfold + cosineLR + augmentations (geometric + colour jitter) for 50 epochs
K-Fold Results:
IoU      | bg: 0.987 crop: 0.676 weed: 0.621
Accuracy | bg: 0.996 crop: 0.813 weed: 0.704
BFScore  | bg: 0.859 crop: 0.671 weed: 0.665

Notes:
- Actually slightly worse than R3. Maybe colour jitter degrades the image too much?
- Let's run geometric augmentations only and see what happens.
Geometric only:
K-Fold Results:
IoU      | bg: 0.989 crop: 0.721 weed: 0.695
Accuracy | bg: 0.995 crop: 0.816 weed: 0.798
BFScore  | bg: 0.892 crop: 0.726 weed: 0.744

- Definitely better, matching and slightly beating cosineLR-only run.

## Result_4 13/04/26. Baseline + kfold + cosineLR + raw weighted CE for 50 epochs
K-Fold Results:
IoU      | bg: 0.961 crop: 0.663 weed: 0.489
Accuracy | bg: 0.962 crop: 0.946 weed: 0.899
BFScore  | bg: 0.570 crop: 0.635 weed: 0.457

Notes:
- Worse output. Likely due to overly aggressive imbalance handling.
- Will remove weighted CE for now and perhaps explore it later.

## Result_3 10/04/26. Basline + k-fold (k=5) w/ CosineAnnealingLR (init LR=1e-3) for 30 epochs
K-Fold Results:
IoU      | bg: 0.988 crop: 0.722 weed: 0.678
Accuracy | bg: 0.995 crop: 0.843 weed: 0.787
BFScore  | bg: 0.884 crop: 0.724 weed: 0.710

Notes:
- Significant crop improvement over baseline

Raw out:
Fold 1/5
  Epoch 01 | Train Loss: 0.7715 | Val Loss: 0.8774 | IoU crop: 0.000 weed: 0.000 | LR: 0.000997
  Epoch 02 | Train Loss: 0.5224 | Val Loss: 0.5744 | IoU crop: 0.000 weed: 0.000 | LR: 0.000989
  Epoch 03 | Train Loss: 0.4100 | Val Loss: 0.3868 | IoU crop: 0.000 weed: 0.000 | LR: 0.000976
  Epoch 04 | Train Loss: 0.3329 | Val Loss: 0.3298 | IoU crop: 0.000 weed: 0.000 | LR: 0.000957
  Epoch 05 | Train Loss: 0.2790 | Val Loss: 0.2545 | IoU crop: 0.000 weed: 0.048 | LR: 0.000933
  Epoch 06 | Train Loss: 0.2405 | Val Loss: 0.2648 | IoU crop: 0.000 weed: 0.252 | LR: 0.000905
  Epoch 07 | Train Loss: 0.2082 | Val Loss: 0.2046 | IoU crop: 0.090 weed: 0.478 | LR: 0.000872
  Epoch 08 | Train Loss: 0.1775 | Val Loss: 0.1637 | IoU crop: 0.561 weed: 0.580 | LR: 0.000835
  Epoch 09 | Train Loss: 0.1631 | Val Loss: 0.1644 | IoU crop: 0.021 weed: 0.537 | LR: 0.000794
  Epoch 10 | Train Loss: 0.1519 | Val Loss: 0.1415 | IoU crop: 0.000 weed: 0.537 | LR: 0.000750
  Epoch 11 | Train Loss: 0.1351 | Val Loss: 0.1237 | IoU crop: 0.461 weed: 0.356 | LR: 0.000704
  Epoch 12 | Train Loss: 0.1261 | Val Loss: 0.0922 | IoU crop: 0.744 weed: 0.687 | LR: 0.000655
  Epoch 13 | Train Loss: 0.1147 | Val Loss: 0.1027 | IoU crop: 0.749 weed: 0.722 | LR: 0.000604
  Epoch 14 | Train Loss: 0.1106 | Val Loss: 0.0776 | IoU crop: 0.694 weed: 0.697 | LR: 0.000553
  Epoch 15 | Train Loss: 0.1048 | Val Loss: 0.0877 | IoU crop: 0.394 weed: 0.633 | LR: 0.000501
  Epoch 16 | Train Loss: 0.0987 | Val Loss: 0.0821 | IoU crop: 0.763 weed: 0.730 | LR: 0.000448
  Epoch 17 | Train Loss: 0.0933 | Val Loss: 0.0796 | IoU crop: 0.756 weed: 0.729 | LR: 0.000397
  Epoch 18 | Train Loss: 0.0906 | Val Loss: 0.0624 | IoU crop: 0.785 weed: 0.754 | LR: 0.000346
  Epoch 19 | Train Loss: 0.0881 | Val Loss: 0.0687 | IoU crop: 0.785 weed: 0.741 | LR: 0.000297
  Epoch 20 | Train Loss: 0.0864 | Val Loss: 0.0651 | IoU crop: 0.723 weed: 0.688 | LR: 0.000251
  Epoch 21 | Train Loss: 0.0850 | Val Loss: 0.0661 | IoU crop: 0.786 weed: 0.745 | LR: 0.000207
  Epoch 22 | Train Loss: 0.0804 | Val Loss: 0.0746 | IoU crop: 0.155 weed: 0.587 | LR: 0.000166
  Epoch 23 | Train Loss: 0.0768 | Val Loss: 0.0604 | IoU crop: 0.718 weed: 0.696 | LR: 0.000129
  Epoch 24 | Train Loss: 0.0786 | Val Loss: 0.0599 | IoU crop: 0.762 weed: 0.742 | LR: 0.000096
  Epoch 25 | Train Loss: 0.0768 | Val Loss: 0.0706 | IoU crop: 0.305 weed: 0.627 | LR: 0.000068
  Epoch 26 | Train Loss: 0.0782 | Val Loss: 0.0590 | IoU crop: 0.762 weed: 0.736 | LR: 0.000044
  Epoch 27 | Train Loss: 0.0758 | Val Loss: 0.0564 | IoU crop: 0.796 weed: 0.762 | LR: 0.000025
  Epoch 28 | Train Loss: 0.0775 | Val Loss: 0.0574 | IoU crop: 0.781 weed: 0.760 | LR: 0.000012
  Epoch 29 | Train Loss: 0.0748 | Val Loss: 0.0575 | IoU crop: 0.779 weed: 0.760 | LR: 0.000004
  Epoch 30 | Train Loss: 0.0732 | Val Loss: 0.0575 | IoU crop: 0.781 weed: 0.760 | LR: 0.000001
  Best epoch 27 | IoU crop: 0.796 weed: 0.762

Fold 2/5
  Epoch 01 | Train Loss: 0.7910 | Val Loss: 1.0202 | IoU crop: 0.000 weed: 0.026 | LR: 0.000997
  Epoch 02 | Train Loss: 0.5260 | Val Loss: 1.8777 | IoU crop: 0.023 weed: 0.025 | LR: 0.000989
  Epoch 03 | Train Loss: 0.4243 | Val Loss: 0.4770 | IoU crop: 0.000 weed: 0.000 | LR: 0.000976
  Epoch 04 | Train Loss: 0.3540 | Val Loss: 0.4170 | IoU crop: 0.000 weed: 0.000 | LR: 0.000957
  Epoch 05 | Train Loss: 0.3013 | Val Loss: 0.3497 | IoU crop: 0.000 weed: 0.000 | LR: 0.000933
  Epoch 06 | Train Loss: 0.2620 | Val Loss: 0.2610 | IoU crop: 0.021 weed: 0.024 | LR: 0.000905
  Epoch 07 | Train Loss: 0.2298 | Val Loss: 0.2378 | IoU crop: 0.009 weed: 0.221 | LR: 0.000872
  Epoch 08 | Train Loss: 0.1956 | Val Loss: 0.2126 | IoU crop: 0.000 weed: 0.287 | LR: 0.000835
  Epoch 09 | Train Loss: 0.1744 | Val Loss: 0.1635 | IoU crop: 0.577 weed: 0.440 | LR: 0.000794
  Epoch 10 | Train Loss: 0.1601 | Val Loss: 0.2006 | IoU crop: 0.000 weed: 0.373 | LR: 0.000750
  Epoch 11 | Train Loss: 0.1446 | Val Loss: 0.1579 | IoU crop: 0.171 weed: 0.390 | LR: 0.000704
  Epoch 12 | Train Loss: 0.1321 | Val Loss: 0.1312 | IoU crop: 0.821 weed: 0.565 | LR: 0.000655
  Epoch 13 | Train Loss: 0.1225 | Val Loss: 0.1193 | IoU crop: 0.811 weed: 0.572 | LR: 0.000604
  Epoch 14 | Train Loss: 0.1142 | Val Loss: 0.1246 | IoU crop: 0.249 weed: 0.418 | LR: 0.000553
  Epoch 15 | Train Loss: 0.1128 | Val Loss: 0.1197 | IoU crop: 0.715 weed: 0.505 | LR: 0.000501
  Epoch 16 | Train Loss: 0.1102 | Val Loss: 0.1013 | IoU crop: 0.666 weed: 0.521 | LR: 0.000448
  Epoch 17 | Train Loss: 0.0984 | Val Loss: 0.1068 | IoU crop: 0.756 weed: 0.556 | LR: 0.000397
  Epoch 18 | Train Loss: 0.0987 | Val Loss: 0.0900 | IoU crop: 0.839 weed: 0.599 | LR: 0.000346
  Epoch 19 | Train Loss: 0.0930 | Val Loss: 0.0929 | IoU crop: 0.836 weed: 0.564 | LR: 0.000297
  Epoch 20 | Train Loss: 0.0934 | Val Loss: 0.0933 | IoU crop: 0.705 weed: 0.548 | LR: 0.000251
  Epoch 21 | Train Loss: 0.0897 | Val Loss: 0.0838 | IoU crop: 0.837 weed: 0.599 | LR: 0.000207
  Epoch 22 | Train Loss: 0.0847 | Val Loss: 0.0874 | IoU crop: 0.769 weed: 0.583 | LR: 0.000166
  Epoch 23 | Train Loss: 0.0824 | Val Loss: 0.0861 | IoU crop: 0.826 weed: 0.601 | LR: 0.000129
  Epoch 24 | Train Loss: 0.0834 | Val Loss: 0.0847 | IoU crop: 0.811 weed: 0.593 | LR: 0.000096
  Epoch 25 | Train Loss: 0.0795 | Val Loss: 0.0833 | IoU crop: 0.808 weed: 0.588 | LR: 0.000068
  Epoch 26 | Train Loss: 0.0799 | Val Loss: 0.0839 | IoU crop: 0.811 weed: 0.592 | LR: 0.000044
  Epoch 27 | Train Loss: 0.0785 | Val Loss: 0.0855 | IoU crop: 0.801 weed: 0.595 | LR: 0.000025
  Epoch 28 | Train Loss: 0.0795 | Val Loss: 0.0834 | IoU crop: 0.821 weed: 0.599 | LR: 0.000012
  Epoch 29 | Train Loss: 0.0791 | Val Loss: 0.0824 | IoU crop: 0.834 weed: 0.605 | LR: 0.000004
  Epoch 30 | Train Loss: 0.0788 | Val Loss: 0.0828 | IoU crop: 0.836 weed: 0.605 | LR: 0.000001
  Best epoch 29 | IoU crop: 0.834 weed: 0.605

Fold 3/5
  Epoch 01 | Train Loss: 0.9286 | Val Loss: 1.0104 | IoU crop: 0.000 weed: 0.057 | LR: 0.000997
  Epoch 02 | Train Loss: 0.6259 | Val Loss: 0.6804 | IoU crop: 0.000 weed: 0.000 | LR: 0.000989
  Epoch 03 | Train Loss: 0.5009 | Val Loss: 0.5400 | IoU crop: 0.000 weed: 0.000 | LR: 0.000976
  Epoch 04 | Train Loss: 0.4211 | Val Loss: 0.4441 | IoU crop: 0.000 weed: 0.002 | LR: 0.000957
  Epoch 05 | Train Loss: 0.3579 | Val Loss: 0.3513 | IoU crop: 0.000 weed: 0.020 | LR: 0.000933
  Epoch 06 | Train Loss: 0.3120 | Val Loss: 0.3225 | IoU crop: 0.000 weed: 0.070 | LR: 0.000905
  Epoch 07 | Train Loss: 0.2708 | Val Loss: 0.2858 | IoU crop: 0.002 weed: 0.116 | LR: 0.000872
  Epoch 08 | Train Loss: 0.2370 | Val Loss: 0.2347 | IoU crop: 0.024 weed: 0.148 | LR: 0.000835
  Epoch 09 | Train Loss: 0.2175 | Val Loss: 0.1987 | IoU crop: 0.768 weed: 0.442 | LR: 0.000794
  Epoch 10 | Train Loss: 0.2001 | Val Loss: 0.1861 | IoU crop: 0.314 weed: 0.348 | LR: 0.000750
  Epoch 11 | Train Loss: 0.1747 | Val Loss: 0.1827 | IoU crop: 0.182 weed: 0.291 | LR: 0.000704
  Epoch 12 | Train Loss: 0.1604 | Val Loss: 0.1520 | IoU crop: 0.627 weed: 0.448 | LR: 0.000655
  Epoch 13 | Train Loss: 0.1454 | Val Loss: 0.1416 | IoU crop: 0.503 weed: 0.406 | LR: 0.000604
  Epoch 14 | Train Loss: 0.1374 | Val Loss: 0.1273 | IoU crop: 0.822 weed: 0.536 | LR: 0.000553
  Epoch 15 | Train Loss: 0.1262 | Val Loss: 0.1375 | IoU crop: 0.355 weed: 0.355 | LR: 0.000501
  Epoch 16 | Train Loss: 0.1215 | Val Loss: 0.1111 | IoU crop: 0.717 weed: 0.496 | LR: 0.000448
  Epoch 17 | Train Loss: 0.1174 | Val Loss: 0.1122 | IoU crop: 0.840 weed: 0.582 | LR: 0.000397
  Epoch 18 | Train Loss: 0.1113 | Val Loss: 0.1638 | IoU crop: 0.000 weed: 0.284 | LR: 0.000346
  Epoch 19 | Train Loss: 0.1100 | Val Loss: 0.0990 | IoU crop: 0.847 weed: 0.568 | LR: 0.000297
  Epoch 20 | Train Loss: 0.1054 | Val Loss: 0.1386 | IoU crop: 0.042 weed: 0.303 | LR: 0.000251
  Epoch 21 | Train Loss: 0.0998 | Val Loss: 0.0957 | IoU crop: 0.831 weed: 0.578 | LR: 0.000207
  Epoch 22 | Train Loss: 0.0985 | Val Loss: 0.0936 | IoU crop: 0.853 weed: 0.602 | LR: 0.000166
  Epoch 23 | Train Loss: 0.0935 | Val Loss: 0.1055 | IoU crop: 0.571 weed: 0.452 | LR: 0.000129
  Epoch 24 | Train Loss: 0.0987 | Val Loss: 0.0928 | IoU crop: 0.832 weed: 0.564 | LR: 0.000096
  Epoch 25 | Train Loss: 0.0962 | Val Loss: 0.0891 | IoU crop: 0.809 weed: 0.583 | LR: 0.000068
  Epoch 26 | Train Loss: 0.0922 | Val Loss: 0.1099 | IoU crop: 0.341 weed: 0.381 | LR: 0.000044
  Epoch 27 | Train Loss: 0.0916 | Val Loss: 0.1007 | IoU crop: 0.572 weed: 0.453 | LR: 0.000025
  Epoch 28 | Train Loss: 0.0912 | Val Loss: 0.0900 | IoU crop: 0.799 weed: 0.559 | LR: 0.000012
  Epoch 29 | Train Loss: 0.0897 | Val Loss: 0.0910 | IoU crop: 0.780 weed: 0.552 | LR: 0.000004
  Epoch 30 | Train Loss: 0.0903 | Val Loss: 0.0909 | IoU crop: 0.769 weed: 0.545 | LR: 0.000001
  Best epoch 25 | IoU crop: 0.809 weed: 0.583

Fold 4/5
  Epoch 01 | Train Loss: 0.9880 | Val Loss: 1.1898 | IoU crop: 0.009 weed: 0.002 | LR: 0.000997
  Epoch 02 | Train Loss: 0.6803 | Val Loss: 0.8199 | IoU crop: 0.000 weed: 0.000 | LR: 0.000989
  Epoch 03 | Train Loss: 0.5632 | Val Loss: 0.6610 | IoU crop: 0.000 weed: 0.000 | LR: 0.000976
  Epoch 04 | Train Loss: 0.4714 | Val Loss: 0.6233 | IoU crop: 0.000 weed: 0.000 | LR: 0.000957
  Epoch 05 | Train Loss: 0.3969 | Val Loss: 0.4908 | IoU crop: 0.000 weed: 0.010 | LR: 0.000933
  Epoch 06 | Train Loss: 0.3379 | Val Loss: 0.4080 | IoU crop: 0.000 weed: 0.077 | LR: 0.000905
  Epoch 07 | Train Loss: 0.2871 | Val Loss: 0.3274 | IoU crop: 0.000 weed: 0.415 | LR: 0.000872
  Epoch 08 | Train Loss: 0.2508 | Val Loss: 0.3067 | IoU crop: 0.397 weed: 0.552 | LR: 0.000835
  Epoch 09 | Train Loss: 0.2231 | Val Loss: 0.2329 | IoU crop: 0.097 weed: 0.656 | LR: 0.000794
  Epoch 10 | Train Loss: 0.1976 | Val Loss: 0.2034 | IoU crop: 0.079 weed: 0.662 | LR: 0.000750
  Epoch 11 | Train Loss: 0.1787 | Val Loss: 0.1964 | IoU crop: 0.555 weed: 0.693 | LR: 0.000704
  Epoch 12 | Train Loss: 0.1654 | Val Loss: 0.1602 | IoU crop: 0.556 weed: 0.697 | LR: 0.000655
  Epoch 13 | Train Loss: 0.1490 | Val Loss: 0.2043 | IoU crop: 0.478 weed: 0.638 | LR: 0.000604
  Epoch 14 | Train Loss: 0.1423 | Val Loss: 0.1481 | IoU crop: 0.551 weed: 0.709 | LR: 0.000553
  Epoch 15 | Train Loss: 0.1299 | Val Loss: 0.2093 | IoU crop: 0.232 weed: 0.362 | LR: 0.000501
  Epoch 16 | Train Loss: 0.1219 | Val Loss: 0.1358 | IoU crop: 0.537 weed: 0.700 | LR: 0.000448
  Epoch 17 | Train Loss: 0.1165 | Val Loss: 0.1260 | IoU crop: 0.571 weed: 0.711 | LR: 0.000397
  Epoch 18 | Train Loss: 0.1149 | Val Loss: 0.2039 | IoU crop: 0.240 weed: 0.401 | LR: 0.000346
  Epoch 19 | Train Loss: 0.1131 | Val Loss: 0.1284 | IoU crop: 0.600 weed: 0.708 | LR: 0.000297
  Epoch 20 | Train Loss: 0.1050 | Val Loss: 0.1208 | IoU crop: 0.577 weed: 0.714 | LR: 0.000251
  Epoch 21 | Train Loss: 0.1006 | Val Loss: 0.1172 | IoU crop: 0.540 weed: 0.719 | LR: 0.000207
  Epoch 22 | Train Loss: 0.1009 | Val Loss: 0.1146 | IoU crop: 0.611 weed: 0.709 | LR: 0.000166
  Epoch 23 | Train Loss: 0.0965 | Val Loss: 0.1113 | IoU crop: 0.617 weed: 0.709 | LR: 0.000129
  Epoch 24 | Train Loss: 0.0946 | Val Loss: 0.1121 | IoU crop: 0.634 weed: 0.720 | LR: 0.000096
  Epoch 25 | Train Loss: 0.0948 | Val Loss: 0.1103 | IoU crop: 0.635 weed: 0.720 | LR: 0.000068
  Epoch 26 | Train Loss: 0.0904 | Val Loss: 0.1103 | IoU crop: 0.638 weed: 0.716 | LR: 0.000044
  Epoch 27 | Train Loss: 0.0916 | Val Loss: 0.1115 | IoU crop: 0.632 weed: 0.715 | LR: 0.000025
  Epoch 28 | Train Loss: 0.0927 | Val Loss: 0.1106 | IoU crop: 0.630 weed: 0.715 | LR: 0.000012
  Epoch 29 | Train Loss: 0.0907 | Val Loss: 0.1102 | IoU crop: 0.631 weed: 0.716 | LR: 0.000004
  Epoch 30 | Train Loss: 0.0921 | Val Loss: 0.1110 | IoU crop: 0.632 weed: 0.715 | LR: 0.000001
  Best epoch 29 | IoU crop: 0.631 weed: 0.716

Fold 5/5
  Epoch 01 | Train Loss: 0.8353 | Val Loss: 0.9974 | IoU crop: 0.000 weed: 0.001 | LR: 0.000997
  Epoch 02 | Train Loss: 0.5646 | Val Loss: 0.8342 | IoU crop: 0.000 weed: 0.001 | LR: 0.000989
  Epoch 03 | Train Loss: 0.4608 | Val Loss: 0.5293 | IoU crop: 0.000 weed: 0.000 | LR: 0.000976
  Epoch 04 | Train Loss: 0.3772 | Val Loss: 0.4426 | IoU crop: 0.000 weed: 0.000 | LR: 0.000957
  Epoch 05 | Train Loss: 0.3155 | Val Loss: 0.3845 | IoU crop: 0.000 weed: 0.017 | LR: 0.000933
  Epoch 06 | Train Loss: 0.2665 | Val Loss: 0.3356 | IoU crop: 0.000 weed: 0.259 | LR: 0.000905
  Epoch 07 | Train Loss: 0.2288 | Val Loss: 0.2747 | IoU crop: 0.000 weed: 0.607 | LR: 0.000872
  Epoch 08 | Train Loss: 0.1978 | Val Loss: 0.2291 | IoU crop: 0.000 weed: 0.679 | LR: 0.000835
  Epoch 09 | Train Loss: 0.1761 | Val Loss: 0.2271 | IoU crop: 0.248 weed: 0.411 | LR: 0.000794
  Epoch 10 | Train Loss: 0.1587 | Val Loss: 0.1777 | IoU crop: 0.294 weed: 0.679 | LR: 0.000750
  Epoch 11 | Train Loss: 0.1449 | Val Loss: 0.1633 | IoU crop: 0.121 weed: 0.675 | LR: 0.000704
  Epoch 12 | Train Loss: 0.1327 | Val Loss: 0.6483 | IoU crop: 0.153 weed: 0.046 | LR: 0.000655
  Epoch 13 | Train Loss: 0.1275 | Val Loss: 0.1597 | IoU crop: 0.337 weed: 0.544 | LR: 0.000604
  Epoch 14 | Train Loss: 0.1214 | Val Loss: 0.1444 | IoU crop: 0.433 weed: 0.642 | LR: 0.000553
  Epoch 15 | Train Loss: 0.1147 | Val Loss: 0.1277 | IoU crop: 0.444 weed: 0.645 | LR: 0.000501
  Epoch 16 | Train Loss: 0.1049 | Val Loss: 0.1395 | IoU crop: 0.486 weed: 0.693 | LR: 0.000448
  Epoch 17 | Train Loss: 0.1000 | Val Loss: 0.1330 | IoU crop: 0.370 weed: 0.548 | LR: 0.000397
  Epoch 18 | Train Loss: 0.0944 | Val Loss: 0.1096 | IoU crop: 0.535 weed: 0.700 | LR: 0.000346
  Epoch 19 | Train Loss: 0.0908 | Val Loss: 0.1032 | IoU crop: 0.555 weed: 0.715 | LR: 0.000297
  Epoch 20 | Train Loss: 0.0899 | Val Loss: 0.1495 | IoU crop: 0.300 weed: 0.439 | LR: 0.000251
  Epoch 21 | Train Loss: 0.0860 | Val Loss: 0.1051 | IoU crop: 0.145 weed: 0.693 | LR: 0.000207
  Epoch 22 | Train Loss: 0.0828 | Val Loss: 0.1214 | IoU crop: 0.421 weed: 0.608 | LR: 0.000166
  Epoch 23 | Train Loss: 0.0826 | Val Loss: 0.1055 | IoU crop: 0.539 weed: 0.701 | LR: 0.000129
  Epoch 24 | Train Loss: 0.0801 | Val Loss: 0.0971 | IoU crop: 0.572 weed: 0.725 | LR: 0.000096
  Epoch 25 | Train Loss: 0.0794 | Val Loss: 0.1278 | IoU crop: 0.387 weed: 0.571 | LR: 0.000068
  Epoch 26 | Train Loss: 0.0785 | Val Loss: 0.0949 | IoU crop: 0.517 weed: 0.725 | LR: 0.000044
  Epoch 27 | Train Loss: 0.0818 | Val Loss: 0.0947 | IoU crop: 0.537 weed: 0.722 | LR: 0.000025
  Epoch 28 | Train Loss: 0.0791 | Val Loss: 0.0976 | IoU crop: 0.577 weed: 0.719 | LR: 0.000012
  Epoch 29 | Train Loss: 0.0814 | Val Loss: 0.1002 | IoU crop: 0.567 weed: 0.713 | LR: 0.000004
  Epoch 30 | Train Loss: 0.0796 | Val Loss: 0.0982 | IoU crop: 0.570 weed: 0.717 | LR: 0.000001
  Best epoch 27 | IoU crop: 0.537 weed: 0.722



## Result_2 09/04/26. Baseline (k=5 but only ran on one fold; tried ReduceLROnPlateau but did nothing)
Fold 1/5
  Epoch 01 | Train Loss: 1.0270 | Val Loss: 1.0497 | IoU crop: 0.000 weed: 0.027 | LR: 0.000500
  Epoch 02 | Train Loss: 0.7780 | Val Loss: 0.8416 | IoU crop: 0.000 weed: 0.000 | LR: 0.000500
  Epoch 03 | Train Loss: 0.6853 | Val Loss: 0.7034 | IoU crop: 0.000 weed: 0.000 | LR: 0.000500
  Epoch 04 | Train Loss: 0.6263 | Val Loss: 0.6199 | IoU crop: 0.000 weed: 0.000 | LR: 0.000500
  Epoch 05 | Train Loss: 0.5703 | Val Loss: 0.5541 | IoU crop: 0.000 weed: 0.002 | LR: 0.000500
  Epoch 06 | Train Loss: 0.5234 | Val Loss: 0.4796 | IoU crop: 0.000 weed: 0.187 | LR: 0.000500
  Epoch 07 | Train Loss: 0.4797 | Val Loss: 0.4496 | IoU crop: 0.007 weed: 0.300 | LR: 0.000500
  Epoch 08 | Train Loss: 0.4395 | Val Loss: 0.3852 | IoU crop: 0.063 weed: 0.515 | LR: 0.000500
  Epoch 09 | Train Loss: 0.4056 | Val Loss: 0.3573 | IoU crop: 0.006 weed: 0.505 | LR: 0.000500
  Epoch 10 | Train Loss: 0.3719 | Val Loss: 0.3322 | IoU crop: 0.633 weed: 0.623 | LR: 0.000500
  Epoch 11 | Train Loss: 0.3437 | Val Loss: 0.2990 | IoU crop: 0.412 weed: 0.612 | LR: 0.000500
  Epoch 12 | Train Loss: 0.3172 | Val Loss: 0.2808 | IoU crop: 0.395 weed: 0.188 | LR: 0.000500
  Epoch 13 | Train Loss: 0.2921 | Val Loss: 0.2360 | IoU crop: 0.381 weed: 0.614 | LR: 0.000500
  Epoch 14 | Train Loss: 0.2681 | Val Loss: 0.2350 | IoU crop: 0.733 weed: 0.708 | LR: 0.000500
  Epoch 15 | Train Loss: 0.2471 | Val Loss: 0.2241 | IoU crop: 0.763 weed: 0.720 | LR: 0.000500
  Epoch 16 | Train Loss: 0.2277 | Val Loss: 0.2015 | IoU crop: 0.282 weed: 0.607 | LR: 0.000500
  Epoch 17 | Train Loss: 0.2137 | Val Loss: 0.2061 | IoU crop: 0.563 weed: 0.538 | LR: 0.000500
  Epoch 18 | Train Loss: 0.2076 | Val Loss: 0.2308 | IoU crop: 0.344 weed: 0.122 | LR: 0.000500
  Epoch 19 | Train Loss: 0.1942 | Val Loss: 0.1439 | IoU crop: 0.711 weed: 0.700 | LR: 0.000500
  Epoch 20 | Train Loss: 0.1813 | Val Loss: 0.1689 | IoU crop: 0.690 weed: 0.701 | LR: 0.000500
  Epoch 21 | Train Loss: 0.1680 | Val Loss: 0.1438 | IoU crop: 0.700 weed: 0.697 | LR: 0.000500
  Epoch 22 | Train Loss: 0.1590 | Val Loss: 0.1536 | IoU crop: 0.030 weed: 0.564 | LR: 0.000500
  Epoch 23 | Train Loss: 0.1478 | Val Loss: 0.1405 | IoU crop: 0.544 weed: 0.509 | LR: 0.000500
  Epoch 24 | Train Loss: 0.1391 | Val Loss: 0.1370 | IoU crop: 0.006 weed: 0.550 | LR: 0.000500
  Epoch 25 | Train Loss: 0.1417 | Val Loss: 0.1750 | IoU crop: 0.331 weed: 0.154 | LR: 0.000500
  Epoch 26 | Train Loss: 0.1310 | Val Loss: 0.1055 | IoU crop: 0.454 weed: 0.659 | LR: 0.000500
  Epoch 27 | Train Loss: 0.1240 | Val Loss: 0.1055 | IoU crop: 0.675 weed: 0.713 | LR: 0.000500
  Epoch 28 | Train Loss: 0.1206 | Val Loss: 0.1089 | IoU crop: 0.004 weed: 0.560 | LR: 0.000500
  Epoch 29 | Train Loss: 0.1142 | Val Loss: 0.0973 | IoU crop: 0.346 weed: 0.630 | LR: 0.000500
  Epoch 30 | Train Loss: 0.1064 | Val Loss: 0.1573 | IoU crop: 0.359 weed: 0.151 | LR: 0.000500
  Best epoch 29 | IoU crop: 0.346 weed: 0.630

Notes:
- Init LR set to 5e-4 here instead of 1e-3.
- LR scheduler did nothing since patience didn't trigger (no plateau here, not even spike-and-recover pattern from before)
- Much better training stability (stable reduction of val loss), at least this fold, even though performance is worse.
- Next will try CosineAnnealingLR to simply gradually reduce LR regardless of whats going on.
- To address jumpy IoU in adjacent epochs, will need to implement weighted crossentropy and augmentation, since there are only
10 test images containing very few crop pixels. The model's borderline confident on whether its a crop or background constantly.
- Will add early stopping if keeping cosine LR, since in later epochs very little learning will take place (small LR, decreasing further),
so to avoid wasting training time this could be worthwhile.



## Result_1 09/04/26. Baseline (k=5 k-fold CV, no improvements yet)
IoU      | crop: 0.644  weed: 0.659
Accuracy | crop: 0.719  weed: 0.766
BFScore  | crop: 0.624  weed: 0.686
Notes:
- Crop IoU across folds: 0.758, 0.776, 0.767, 0.471, 0.446.
- Perhaps fold4 and fold5 contain hard or unrepresentative examples -> poorer performance.
- Training instability observed: adjacent epochs catastrophically overshoot and then recover. Clear sign of LR too high.
- Need to implement early stoppage to halt training and weight degradation due to training into overfit. Must stop on val loss plateau.

Raw results:
Fold 1/5
  Epoch 01 | Train Loss: 0.7750 | Val Loss: 1.1585 | IoU crop: 0.014 weed: 0.029
  Epoch 02 | Train Loss: 0.5281 | Val Loss: 0.5847 | IoU crop: 0.000 weed: 0.000
  Epoch 03 | Train Loss: 0.4291 | Val Loss: 0.4853 | IoU crop: 0.000 weed: 0.000
  Epoch 04 | Train Loss: 0.3621 | Val Loss: 0.3666 | IoU crop: 0.000 weed: 0.000
  Epoch 05 | Train Loss: 0.3044 | Val Loss: 0.3325 | IoU crop: 0.000 weed: 0.256
  Epoch 06 | Train Loss: 0.2553 | Val Loss: 0.2579 | IoU crop: 0.000 weed: 0.447
  Epoch 07 | Train Loss: 0.2189 | Val Loss: 0.2102 | IoU crop: 0.197 weed: 0.558
  Epoch 08 | Train Loss: 0.1938 | Val Loss: 0.1548 | IoU crop: 0.473 weed: 0.466
  Epoch 09 | Train Loss: 0.1712 | Val Loss: 0.1739 | IoU crop: 0.501 weed: 0.478
  Epoch 10 | Train Loss: 0.1471 | Val Loss: 0.1136 | IoU crop: 0.624 weed: 0.679
  Epoch 11 | Train Loss: 0.1369 | Val Loss: 0.1271 | IoU crop: 0.471 weed: 0.389
  Epoch 12 | Train Loss: 0.1262 | Val Loss: 0.1153 | IoU crop: 0.695 weed: 0.702
  Epoch 13 | Train Loss: 0.1172 | Val Loss: 0.1563 | IoU crop: 0.334 weed: 0.168
  Epoch 14 | Train Loss: 0.1108 | Val Loss: 0.1630 | IoU crop: 0.324 weed: 0.180
  Epoch 15 | Train Loss: 0.0993 | Val Loss: 0.0893 | IoU crop: 0.528 weed: 0.540
  Epoch 16 | Train Loss: 0.0958 | Val Loss: 0.0745 | IoU crop: 0.023 weed: 0.557
  Epoch 17 | Train Loss: 0.0895 | Val Loss: 0.0797 | IoU crop: 0.478 weed: 0.369
  Epoch 18 | Train Loss: 0.0857 | Val Loss: 0.0650 | IoU crop: 0.594 weed: 0.620
  Epoch 19 | Train Loss: 0.0873 | Val Loss: 0.0580 | IoU crop: 0.713 weed: 0.704
  Epoch 20 | Train Loss: 0.0780 | Val Loss: 0.0570 | IoU crop: 0.758 weed: 0.734
  Best epoch 20 | IoU crop: 0.758 weed: 0.734

Fold 2/5
  Epoch 01 | Train Loss: 0.7216 | Val Loss: 0.9575 | IoU crop: 0.000 weed: 0.000
  Epoch 02 | Train Loss: 0.4848 | Val Loss: 0.5072 | IoU crop: 0.000 weed: 0.000
  Epoch 03 | Train Loss: 0.3946 | Val Loss: 0.4352 | IoU crop: 0.000 weed: 0.000
  Epoch 04 | Train Loss: 0.3263 | Val Loss: 0.3906 | IoU crop: 0.000 weed: 0.000
  Epoch 05 | Train Loss: 0.2738 | Val Loss: 0.3166 | IoU crop: 0.000 weed: 0.000
  Epoch 06 | Train Loss: 0.2305 | Val Loss: 0.2719 | IoU crop: 0.008 weed: 0.033
  Epoch 07 | Train Loss: 0.2051 | Val Loss: 0.2579 | IoU crop: 0.000 weed: 0.279
  Epoch 08 | Train Loss: 0.1824 | Val Loss: 0.1843 | IoU crop: 0.324 weed: 0.292
  Epoch 09 | Train Loss: 0.1595 | Val Loss: 0.1813 | IoU crop: 0.684 weed: 0.523
  Epoch 10 | Train Loss: 0.1415 | Val Loss: 0.1274 | IoU crop: 0.593 weed: 0.493
  Epoch 11 | Train Loss: 0.1286 | Val Loss: 0.1458 | IoU crop: 0.507 weed: 0.136
  Epoch 12 | Train Loss: 0.1162 | Val Loss: 0.1041 | IoU crop: 0.700 weed: 0.300
  Epoch 13 | Train Loss: 0.1086 | Val Loss: 0.0973 | IoU crop: 0.818 weed: 0.565
  Epoch 14 | Train Loss: 0.0971 | Val Loss: 0.1317 | IoU crop: 0.024 weed: 0.348
  Epoch 15 | Train Loss: 0.0902 | Val Loss: 0.0942 | IoU crop: 0.596 weed: 0.222
  Epoch 16 | Train Loss: 0.0860 | Val Loss: 0.1022 | IoU crop: 0.659 weed: 0.199
  Epoch 17 | Train Loss: 0.0805 | Val Loss: 0.0733 | IoU crop: 0.829 weed: 0.592
  Epoch 18 | Train Loss: 0.0748 | Val Loss: 0.0740 | IoU crop: 0.774 weed: 0.538
  Epoch 19 | Train Loss: 0.0732 | Val Loss: 0.0675 | IoU crop: 0.776 weed: 0.574
  Epoch 20 | Train Loss: 0.0696 | Val Loss: 0.0892 | IoU crop: 0.112 weed: 0.414
  Best epoch 19 | IoU crop: 0.776 weed: 0.574

Fold 3/5
  Epoch 01 | Train Loss: 1.0342 | Val Loss: 1.0885 | IoU crop: 0.027 weed: 0.000
  Epoch 02 | Train Loss: 0.7468 | Val Loss: 1.6864 | IoU crop: 0.025 weed: 0.000
  Epoch 03 | Train Loss: 0.6387 | Val Loss: 0.6139 | IoU crop: 0.000 weed: 0.000
  Epoch 04 | Train Loss: 0.5511 | Val Loss: 0.4954 | IoU crop: 0.000 weed: 0.000
  Epoch 05 | Train Loss: 0.4638 | Val Loss: 0.4805 | IoU crop: 0.000 weed: 0.000
  Epoch 06 | Train Loss: 0.3918 | Val Loss: 0.4454 | IoU crop: 0.000 weed: 0.021
  Epoch 07 | Train Loss: 0.3337 | Val Loss: 0.3738 | IoU crop: 0.276 weed: 0.082
  Epoch 08 | Train Loss: 0.2912 | Val Loss: 0.3064 | IoU crop: 0.012 weed: 0.217
  Epoch 09 | Train Loss: 0.2448 | Val Loss: 0.2625 | IoU crop: 0.076 weed: 0.259
  Epoch 10 | Train Loss: 0.2148 | Val Loss: 0.1754 | IoU crop: 0.808 weed: 0.529
  Epoch 11 | Train Loss: 0.1851 | Val Loss: 0.2161 | IoU crop: 0.122 weed: 0.312
  Epoch 12 | Train Loss: 0.1688 | Val Loss: 0.2738 | IoU crop: 0.451 weed: 0.121
  Epoch 13 | Train Loss: 0.1506 | Val Loss: 0.1621 | IoU crop: 0.230 weed: 0.333
  Epoch 14 | Train Loss: 0.1407 | Val Loss: 0.1295 | IoU crop: 0.825 weed: 0.444
  Epoch 15 | Train Loss: 0.1238 | Val Loss: 0.1595 | IoU crop: 0.009 weed: 0.281
  Epoch 16 | Train Loss: 0.1143 | Val Loss: 0.1429 | IoU crop: 0.094 weed: 0.320
  Epoch 17 | Train Loss: 0.1063 | Val Loss: 0.1289 | IoU crop: 0.264 weed: 0.343
  Epoch 18 | Train Loss: 0.0988 | Val Loss: 0.0899 | IoU crop: 0.767 weed: 0.550
  Epoch 19 | Train Loss: 0.1042 | Val Loss: 0.0945 | IoU crop: 0.677 weed: 0.498
  Epoch 20 | Train Loss: 0.0923 | Val Loss: 0.1163 | IoU crop: 0.414 weed: 0.345
  Best epoch 18 | IoU crop: 0.767 weed: 0.550

Fold 4/5
  Epoch 01 | Train Loss: 0.8378 | Val Loss: 0.9917 | IoU crop: 0.000 weed: 0.000
  Epoch 02 | Train Loss: 0.5756 | Val Loss: 0.6758 | IoU crop: 0.000 weed: 0.000
  Epoch 03 | Train Loss: 0.4695 | Val Loss: 0.5457 | IoU crop: 0.000 weed: 0.000
  Epoch 04 | Train Loss: 0.3861 | Val Loss: 0.4429 | IoU crop: 0.000 weed: 0.000
  Epoch 05 | Train Loss: 0.3209 | Val Loss: 0.4251 | IoU crop: 0.000 weed: 0.001
  Epoch 06 | Train Loss: 0.2647 | Val Loss: 0.3732 | IoU crop: 0.000 weed: 0.016
  Epoch 07 | Train Loss: 0.2251 | Val Loss: 0.2807 | IoU crop: 0.001 weed: 0.257
  Epoch 08 | Train Loss: 0.1913 | Val Loss: 0.2391 | IoU crop: 0.271 weed: 0.288
  Epoch 09 | Train Loss: 0.1717 | Val Loss: 0.1765 | IoU crop: 0.445 weed: 0.632
  Epoch 10 | Train Loss: 0.1472 | Val Loss: 0.1573 | IoU crop: 0.233 weed: 0.665
  Epoch 11 | Train Loss: 0.1344 | Val Loss: 0.1704 | IoU crop: 0.451 weed: 0.632
  Epoch 12 | Train Loss: 0.1222 | Val Loss: 0.1257 | IoU crop: 0.506 weed: 0.645
  Epoch 13 | Train Loss: 0.1136 | Val Loss: 0.1338 | IoU crop: 0.455 weed: 0.589
  Epoch 14 | Train Loss: 0.1049 | Val Loss: 0.1343 | IoU crop: 0.545 weed: 0.633
  Epoch 15 | Train Loss: 0.0943 | Val Loss: 0.1094 | IoU crop: 0.600 weed: 0.684
  Epoch 16 | Train Loss: 0.0902 | Val Loss: 0.1794 | IoU crop: 0.201 weed: 0.220
  Epoch 17 | Train Loss: 0.0866 | Val Loss: 0.1199 | IoU crop: 0.014 weed: 0.664
  Epoch 18 | Train Loss: 0.0802 | Val Loss: 0.1056 | IoU crop: 0.488 weed: 0.620
  Epoch 19 | Train Loss: 0.0735 | Val Loss: 0.0845 | IoU crop: 0.471 weed: 0.710
  Epoch 20 | Train Loss: 0.0719 | Val Loss: 0.1079 | IoU crop: 0.573 weed: 0.689
  Best epoch 19 | IoU crop: 0.471 weed: 0.710

Fold 5/5
  Epoch 01 | Train Loss: 0.7128 | Val Loss: 0.9250 | IoU crop: 0.000 weed: 0.000
  Epoch 02 | Train Loss: 0.4704 | Val Loss: 0.6253 | IoU crop: 0.000 weed: 0.000
  Epoch 03 | Train Loss: 0.3788 | Val Loss: 0.4926 | IoU crop: 0.000 weed: 0.001
  Epoch 04 | Train Loss: 0.3145 | Val Loss: 0.3995 | IoU crop: 0.000 weed: 0.000
  Epoch 05 | Train Loss: 0.2644 | Val Loss: 0.3671 | IoU crop: 0.000 weed: 0.007
  Epoch 06 | Train Loss: 0.2232 | Val Loss: 0.3281 | IoU crop: 0.002 weed: 0.045
  Epoch 07 | Train Loss: 0.2016 | Val Loss: 0.2155 | IoU crop: 0.059 weed: 0.606
  Epoch 08 | Train Loss: 0.1702 | Val Loss: 0.1870 | IoU crop: 0.049 weed: 0.667
  Epoch 09 | Train Loss: 0.1519 | Val Loss: 0.1598 | IoU crop: 0.409 weed: 0.636
  Epoch 10 | Train Loss: 0.1373 | Val Loss: 0.1391 | IoU crop: 0.524 weed: 0.698
  Epoch 11 | Train Loss: 0.1194 | Val Loss: 0.3145 | IoU crop: 0.168 weed: 0.082
  Epoch 12 | Train Loss: 0.1134 | Val Loss: 0.1371 | IoU crop: 0.429 weed: 0.612
  Epoch 02 | Train Loss: 0.4704 | Val Loss: 0.6253 | IoU crop: 0.000 weed: 0.000
  Epoch 03 | Train Loss: 0.3788 | Val Loss: 0.4926 | IoU crop: 0.000 weed: 0.001
  Epoch 04 | Train Loss: 0.3145 | Val Loss: 0.3995 | IoU crop: 0.000 weed: 0.000
  Epoch 05 | Train Loss: 0.2644 | Val Loss: 0.3671 | IoU crop: 0.000 weed: 0.007
  Epoch 06 | Train Loss: 0.2232 | Val Loss: 0.3281 | IoU crop: 0.002 weed: 0.045
  Epoch 07 | Train Loss: 0.2016 | Val Loss: 0.2155 | IoU crop: 0.059 weed: 0.606
  Epoch 08 | Train Loss: 0.1702 | Val Loss: 0.1870 | IoU crop: 0.049 weed: 0.667
  Epoch 09 | Train Loss: 0.1519 | Val Loss: 0.1598 | IoU crop: 0.409 weed: 0.636
  Epoch 10 | Train Loss: 0.1373 | Val Loss: 0.1391 | IoU crop: 0.524 weed: 0.698
  Epoch 11 | Train Loss: 0.1194 | Val Loss: 0.3145 | IoU crop: 0.168 weed: 0.082
  Epoch 12 | Train Loss: 0.1134 | Val Loss: 0.1371 | IoU crop: 0.429 weed: 0.612
  Epoch 04 | Train Loss: 0.3145 | Val Loss: 0.3995 | IoU crop: 0.000 weed: 0.000
  Epoch 05 | Train Loss: 0.2644 | Val Loss: 0.3671 | IoU crop: 0.000 weed: 0.007
  Epoch 06 | Train Loss: 0.2232 | Val Loss: 0.3281 | IoU crop: 0.002 weed: 0.045
  Epoch 07 | Train Loss: 0.2016 | Val Loss: 0.2155 | IoU crop: 0.059 weed: 0.606
  Epoch 08 | Train Loss: 0.1702 | Val Loss: 0.1870 | IoU crop: 0.049 weed: 0.667
  Epoch 09 | Train Loss: 0.1519 | Val Loss: 0.1598 | IoU crop: 0.409 weed: 0.636
  Epoch 10 | Train Loss: 0.1373 | Val Loss: 0.1391 | IoU crop: 0.524 weed: 0.698
  Epoch 11 | Train Loss: 0.1194 | Val Loss: 0.3145 | IoU crop: 0.168 weed: 0.082
  Epoch 12 | Train Loss: 0.1134 | Val Loss: 0.1371 | IoU crop: 0.429 weed: 0.612
  Epoch 07 | Train Loss: 0.2016 | Val Loss: 0.2155 | IoU crop: 0.059 weed: 0.606
  Epoch 08 | Train Loss: 0.1702 | Val Loss: 0.1870 | IoU crop: 0.049 weed: 0.667
  Epoch 09 | Train Loss: 0.1519 | Val Loss: 0.1598 | IoU crop: 0.409 weed: 0.636
  Epoch 10 | Train Loss: 0.1373 | Val Loss: 0.1391 | IoU crop: 0.524 weed: 0.698
  Epoch 11 | Train Loss: 0.1194 | Val Loss: 0.3145 | IoU crop: 0.168 weed: 0.082
  Epoch 12 | Train Loss: 0.1134 | Val Loss: 0.1371 | IoU crop: 0.429 weed: 0.612
  Epoch 12 | Train Loss: 0.1134 | Val Loss: 0.1371 | IoU crop: 0.429 weed: 0.612
  Epoch 13 | Train Loss: 0.0972 | Val Loss: 0.1077 | IoU crop: 0.296 weed: 0.709
  Epoch 14 | Train Loss: 0.0971 | Val Loss: 0.4534 | IoU crop: 0.151 weed: 0.078
  Epoch 15 | Train Loss: 0.0875 | Val Loss: 0.1288 | IoU crop: 0.388 weed: 0.585
  Epoch 16 | Train Loss: 0.0833 | Val Loss: 0.1380 | IoU crop: 0.421 weed: 0.613
  Epoch 17 | Train Loss: 0.0802 | Val Loss: 0.0950 | IoU crop: 0.482 weed: 0.660
  Epoch 18 | Train Loss: 0.0747 | Val Loss: 0.5651 | IoU crop: 0.153 weed: 0.041
  Epoch 19 | Train Loss: 0.0726 | Val Loss: 0.1081 | IoU crop: 0.420 weed: 0.611
  Epoch 20 | Train Loss: 0.0678 | Val Loss: 0.0793 | IoU crop: 0.446 weed: 0.727
  Best epoch 20 | IoU crop: 0.446 weed: 0.727