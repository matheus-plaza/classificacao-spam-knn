# **OUTPUTS**



### **Executando spambase-train:**



#### **k = 1**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 1 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    3220**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 1 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.28 seconds**



**=== Summary ===**



**Correctly Classified Instances        1226               88.7762 %**

**Incorrectly Classified Instances       155               11.2238 %**

**Kappa statistic                          0.7658**

**Mean absolute error                      0.1125**

**Root mean squared error                  0.3349**

**Relative absolute error                 23.5502 %**

**Root relative squared error             68.544  %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,901    0,132    0,913      0,901    0,907      0,766    0,888     0,890     0**

&#x20;                **0,868    0,099    0,850      0,868    0,859      0,766    0,888     0,793     1**

**Weighted Avg.    0,888    0,119    0,888      0,888    0,888      0,766    0,888     0,852**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**754  83 |   a = 0**

&#x20; **72 472 |   b = 1**





#### **k = 3**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 3 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    3220**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 3 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.28 seconds**



**=== Summary ===**



**Correctly Classified Instances        1224               88.6314 %**

**Incorrectly Classified Instances       157               11.3686 %**

**Kappa statistic                          0.7612**

**Mean absolute error                      0.1386**

**Root mean squared error                  0.2993**

**Relative absolute error                 29.0272 %**

**Root relative squared error             61.2511 %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,912    0,153    0,902      0,912    0,907      0,761    0,932     0,932     0**

&#x20;                **0,847    0,088    0,862      0,847    0,854      0,761    0,932     0,881     1**

**Weighted Avg.    0,886    0,127    0,886      0,886    0,886      0,761    0,932     0,912**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**763  74 |   a = 0**

&#x20; **83 461 |   b = 1**





#### **k = 5**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 5 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    3220**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 5 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.3 seconds**



**=== Summary ===**



**Correctly Classified Instances        1238               89.6452 %**

**Incorrectly Classified Instances       143               10.3548 %**

**Kappa statistic                          0.7828**

**Mean absolute error                      0.1488**

**Root mean squared error                  0.2896**

**Relative absolute error                 31.1692 %**

**Root relative squared error             59.2655 %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,918    0,136    0,912      0,918    0,915      0,783    0,943     0,945     0**

&#x20;                **0,864    0,082    0,872      0,864    0,868      0,783    0,943     0,905     1**

**Weighted Avg.    0,896    0,115    0,896      0,896    0,896      0,783    0,943     0,929**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**768  69 |   a = 0**

&#x20; **74 470 |   b = 1**





#### **k = 7**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 7 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    3220**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 7 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.32 seconds**



**=== Summary ===**



**Correctly Classified Instances        1228               88.9211 %**

**Incorrectly Classified Instances       153               11.0789 %**

**Kappa statistic                          0.7672**

**Mean absolute error                      0.1622**

**Root mean squared error                  0.2892**

**Relative absolute error                 33.9608 %**

**Root relative squared error             59.193  %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,915    0,151    0,903      0,915    0,909      0,767    0,948     0,953     0**

&#x20;                **0,849    0,085    0,867      0,849    0,858      0,767    0,948     0,916     1**

**Weighted Avg.    0,889    0,125    0,889      0,889    0,889      0,767    0,948     0,938**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**766  71 |   a = 0**

&#x20; **82 462 |   b = 1**





#### **k = 9**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 9 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    3220**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 9 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.33 seconds**



**=== Summary ===**



**Correctly Classified Instances        1237               89.5728 %**

**Incorrectly Classified Instances       144               10.4272 %**

**Kappa statistic                          0.7799**

**Mean absolute error                      0.1661**

**Root mean squared error                  0.2875**

**Relative absolute error                 34.7793 %**

**Root relative squared error             58.8388 %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,928    0,154    0,902      0,928    0,915      0,780    0,950     0,957     0**

&#x20;                **0,846    0,072    0,885      0,846    0,865      0,780    0,950     0,920     1**

**Weighted Avg.    0,896    0,122    0,895      0,896    0,895      0,780    0,950     0,943**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**777  60 |   a = 0**

&#x20; **84 460 |   b = 1**





### **Executando spambase-train-1-4-5:**



#### **k = 1**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 1 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 1 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.07 seconds



=== Summary ===



Correctly Classified Instances        1136               82.2592 %

Incorrectly Classified Instances       245               17.7408 %

Kappa statistic                          0.6295

Mean absolute error                      0.1816

Root mean squared error                  0.4213

Relative absolute error                 37.835  %

Root relative squared error             86.2036 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,848    0,217    0,857      0,848    0,853      0,630    0,814     0,816     0

&#x20;                0,783    0,152    0,770      0,783    0,777      0,630    0,814     0,696     1

Weighted Avg.    0,823    0,191    0,823      0,823    0,823      0,630    0,814     0,769     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;710 127 |   a = 0

&#x20;118 426 |   b = 1





#### **k = 3**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 3 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 3 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.09 seconds



=== Summary ===



Correctly Classified Instances        1201               86.966  %

Incorrectly Classified Instances       180               13.034  %

Kappa statistic                          0.7246

Mean absolute error                      0.1913

Root mean squared error                  0.3319

Relative absolute error                 39.8623 %

Root relative squared error             67.913  %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,909    0,191    0,880      0,909    0,894      0,725    0,906     0,903     0

&#x20;                0,809    0,091    0,853      0,809    0,830      0,725    0,906     0,840     1

Weighted Avg.    0,870    0,152    0,869      0,870    0,869      0,725    0,906     0,878     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;761  76 |   a = 0

&#x20;104 440 |   b = 1





#### **k = 5**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 5 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 5 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.09 seconds



=== Summary ===



Correctly Classified Instances        1212               87.7625 %

Incorrectly Classified Instances       169               12.2375 %

Kappa statistic                          0.7401

Mean absolute error                      0.2069

Root mean squared error                  0.3211

Relative absolute error                 43.1206 %

Root relative squared error             65.6924 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,925    0,195    0,880      0,925    0,902      0,742    0,920     0,919     0

&#x20;                0,805    0,075    0,874      0,805    0,838      0,742    0,920     0,873     1

Weighted Avg.    0,878    0,148    0,877      0,878    0,877      0,742    0,920     0,901     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;774  63 |   a = 0

&#x20;106 438 |   b = 1





#### **k = 7**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 7 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 7 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.1 seconds



=== Summary ===



Correctly Classified Instances        1203               87.1108 %

Incorrectly Classified Instances       178               12.8892 %

Kappa statistic                          0.7246

Mean absolute error                      0.2145

Root mean squared error                  0.3178

Relative absolute error                 44.7013 %

Root relative squared error             65.0312 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,931    0,221    0,867      0,931    0,897      0,728    0,925     0,927     0

&#x20;                0,779    0,069    0,880      0,779    0,827      0,728    0,925     0,887     1

Weighted Avg.    0,871    0,161    0,872      0,871    0,870      0,728    0,925     0,911     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;779  58 |   a = 0

&#x20;120 424 |   b = 1





#### **k = 9**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 9 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    805**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 9 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.1 seconds**



**=== Summary ===**



**Correctly Classified Instances        1206               87.328  %**

**Incorrectly Classified Instances       175               12.672  %**

**Kappa statistic                          0.7291**

**Mean absolute error                      0.221** 

**Root mean squared error                  0.3186**

**Relative absolute error                 46.0626 %**

**Root relative squared error             65.1782 %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,933    0,219    0,868      0,933    0,899      0,733    0,925     0,928     0**

&#x20;                **0,781    0,067    0,884      0,781    0,829      0,733    0,925     0,890     1**

**Weighted Avg.    0,873    0,159    0,874      0,873    0,872      0,733    0,925     0,913**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**781  56 |   a = 0**

&#x20;**119 425 |   b = 1**





### **Executando spambase-train-1-4-10:**



#### **k = 1**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 1 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 1 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.08 seconds



=== Summary ===



Correctly Classified Instances        1109               80.3041 %

Incorrectly Classified Instances       272               19.6959 %

Kappa statistic                          0.5894

Mean absolute error                      0.2034

Root mean squared error                  0.4452

Relative absolute error                 42.1954 %

Root relative squared error             91.0219 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,829    0,237    0,843      0,829    0,836      0,589    0,796     0,801     0

&#x20;                0,763    0,171    0,744      0,763    0,753      0,589    0,796     0,670     1

Weighted Avg.    0,803    0,211    0,804      0,803    0,803      0,589    0,796     0,749     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;694 143 |   a = 0

&#x20;129 415 |   b = 1





#### **k = 3**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 3 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 3 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.09 seconds



=== Summary ===



Correctly Classified Instances        1176               85.1557 %

Incorrectly Classified Instances       205               14.8443 %

Kappa statistic                          0.6876

Mean absolute error                      0.2162

Root mean squared error                  0.3454

Relative absolute error                 44.8495 %

Root relative squared error             70.6317 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,886    0,202    0,871      0,886    0,879      0,688    0,895     0,892     0

&#x20;                0,798    0,114    0,820      0,798    0,809      0,688    0,895     0,831     1

Weighted Avg.    0,852    0,167    0,851      0,852    0,851      0,688    0,895     0,868     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;742  95 |   a = 0

&#x20;110 434 |   b = 1





#### **k = 5**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 5 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 5 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.09 seconds



=== Summary ===



Correctly Classified Instances        1188               86.0246 %

Incorrectly Classified Instances       193               13.9754 %

Kappa statistic                          0.7034

Mean absolute error                      0.2314

Root mean squared error                  0.3318

Relative absolute error                 48.0141 %

Root relative squared error             67.8481 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,909    0,215    0,867      0,909    0,887      0,705    0,916     0,917     0

&#x20;                0,785    0,091    0,849      0,785    0,816      0,705    0,916     0,865     1

Weighted Avg.    0,860    0,166    0,860      0,860    0,859      0,705    0,916     0,897     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;761  76 |   a = 0

&#x20;117 427 |   b = 1





#### **k = 7**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 7 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 7 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.11 seconds



=== Summary ===



Correctly Classified Instances        1182               85.5902 %

Incorrectly Classified Instances       199               14.4098 %

Kappa statistic                          0.6918

Mean absolute error                      0.2427

Root mean squared error                  0.3289

Relative absolute error                 50.3612 %

Root relative squared error             67.2481 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,920    0,243    0,854      0,920    0,886      0,695    0,921     0,924     0

&#x20;                0,757    0,080    0,860      0,757    0,805      0,695    0,921     0,882     1

Weighted Avg.    0,856    0,179    0,856      0,856    0,854      0,695    0,921     0,908     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;770  67 |   a = 0

&#x20;132 412 |   b = 1





#### **k = 9**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 9 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    805**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 9 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.1 seconds**



**=== Summary ===**



**Correctly Classified Instances        1194               86.4591 %**

**Incorrectly Classified Instances       187               13.5409 %**

**Kappa statistic                          0.7088**

**Mean absolute error                      0.2515**

**Root mean squared error                  0.3306**

**Relative absolute error                 52.1831 %**

**Root relative squared error             67.6023 %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,937    0,246    0,854      0,937    0,893      0,715    0,920     0,923     0**

&#x20;                **0,754    0,063    0,886      0,754    0,814      0,715    0,920     0,887     1**

**Weighted Avg.    0,865    0,174    0,866      0,865    0,862      0,715    0,920     0,909**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**784  53 |   a = 0**

&#x20;**134 410 |   b = 1**





### **Executando spambase-train-1-4-20:**



#### **k = 1**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 1 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 1 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.08 seconds



=== Summary ===



Correctly Classified Instances        1000               72.4113 %

Incorrectly Classified Instances       381               27.5887 %

Kappa statistic                          0.4372

Mean absolute error                      0.2842

Root mean squared error                  0.5259

Relative absolute error                 58.423  %

Root relative squared error            107.2323 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,723    0,274    0,802      0,723    0,761      0,441    0,725     0,746     0

&#x20;                0,726    0,277    0,630      0,726    0,675      0,441    0,725     0,577     1

Weighted Avg.    0,724    0,275    0,734      0,724    0,727      0,441    0,725     0,679     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;605 232 |   a = 0

&#x20;149 395 |   b = 1





#### **k = 3**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 3 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 3 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.09 seconds



=== Summary ===



Correctly Classified Instances        1071               77.5525 %

Incorrectly Classified Instances       310               22.4475 %

Kappa statistic                          0.535 

Mean absolute error                      0.2982

Root mean squared error                  0.4094

Relative absolute error                 61.3037 %

Root relative squared error             83.4747 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,795    0,254    0,828      0,795    0,811      0,536    0,822     0,827     0

&#x20;                0,746    0,205    0,702      0,746    0,724      0,536    0,822     0,728     1

Weighted Avg.    0,776    0,235    0,779      0,776    0,777      0,536    0,822     0,788     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;665 172 |   a = 0

&#x20;138 406 |   b = 1





#### **k = 5**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 5 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 5 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.1 seconds



=== Summary ===



Correctly Classified Instances        1110               80.3765 %

Incorrectly Classified Instances       271               19.6235 %

Kappa statistic                          0.5897

Mean absolute error                      0.3041

Root mean squared error                  0.387 

Relative absolute error                 62.5108 %

Root relative squared error             78.9079 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,835    0,244    0,840      0,835    0,838      0,590    0,854     0,862     0

&#x20;                0,756    0,165    0,749      0,756    0,752      0,590    0,854     0,778     1

Weighted Avg.    0,804    0,213    0,804      0,804    0,804      0,590    0,854     0,829     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;699 138 |   a = 0

&#x20;133 411 |   b = 1





#### **k = 7**

=== Run information ===



Scheme:       weka.classifiers.lazy.IBk -K 7 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""

Relation:     spambase

Instances:    805

Attributes:   58

&#x20;             atributo\_1

&#x20;             atributo\_2

&#x20;             atributo\_3

&#x20;             atributo\_4

&#x20;             atributo\_5

&#x20;             atributo\_6

&#x20;             atributo\_7

&#x20;             atributo\_8

&#x20;             atributo\_9

&#x20;             atributo\_10

&#x20;             atributo\_11

&#x20;             atributo\_12

&#x20;             atributo\_13

&#x20;             atributo\_14

&#x20;             atributo\_15

&#x20;             atributo\_16

&#x20;             atributo\_17

&#x20;             atributo\_18

&#x20;             atributo\_19

&#x20;             atributo\_20

&#x20;             atributo\_21

&#x20;             atributo\_22

&#x20;             atributo\_23

&#x20;             atributo\_24

&#x20;             atributo\_25

&#x20;             atributo\_26

&#x20;             atributo\_27

&#x20;             atributo\_28

&#x20;             atributo\_29

&#x20;             atributo\_30

&#x20;             atributo\_31

&#x20;             atributo\_32

&#x20;             atributo\_33

&#x20;             atributo\_34

&#x20;             atributo\_35

&#x20;             atributo\_36

&#x20;             atributo\_37

&#x20;             atributo\_38

&#x20;             atributo\_39

&#x20;             atributo\_40

&#x20;             atributo\_41

&#x20;             atributo\_42

&#x20;             atributo\_43

&#x20;             atributo\_44

&#x20;             atributo\_45

&#x20;             atributo\_46

&#x20;             atributo\_47

&#x20;             atributo\_48

&#x20;             atributo\_49

&#x20;             atributo\_50

&#x20;             atributo\_51

&#x20;             atributo\_52

&#x20;             atributo\_53

&#x20;             atributo\_54

&#x20;             atributo\_55

&#x20;             atributo\_56

&#x20;             atributo\_57

&#x20;             class

Test mode:    user supplied test set:  size unknown (reading incrementally)



=== Classifier model (full training set) ===



IB1 instance-based classifier

using 7 nearest neighbour(s) for classification





Time taken to build model: 0 seconds



=== Evaluation on test set ===



Time taken to test model on supplied test set: 0.1 seconds



=== Summary ===



Correctly Classified Instances        1131               81.8972 %

Incorrectly Classified Instances       250               18.1028 %

Kappa statistic                          0.6177

Mean absolute error                      0.3134

Root mean squared error                  0.3784

Relative absolute error                 64.4277 %

Root relative squared error             77.1545 %

Total Number of Instances             1381     



=== Detailed Accuracy By Class ===



&#x20;                TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class

&#x20;                0,866    0,254    0,840      0,866    0,853      0,618    0,869     0,874     0

&#x20;                0,746    0,134    0,784      0,746    0,765      0,618    0,869     0,811     1

Weighted Avg.    0,819    0,206    0,818      0,819    0,818      0,618    0,869     0,849     



=== Confusion Matrix ===



&#x20;  a   b   <-- classified as

&#x20;725 112 |   a = 0

&#x20;138 406 |   b = 1





#### **k = 9**

**=== Run information ===**



**Scheme:       weka.classifiers.lazy.IBk -K 9 -W 0 -A "weka.core.neighboursearch.LinearNNSearch -A \\"weka.core.EuclideanDistance -R first-last\\""**

**Relation:     spambase**

**Instances:    805**

**Attributes:   58**

&#x20;             **atributo\_1**

&#x20;             **atributo\_2**

&#x20;             **atributo\_3**

&#x20;             **atributo\_4**

&#x20;             **atributo\_5**

&#x20;             **atributo\_6**

&#x20;             **atributo\_7**

&#x20;             **atributo\_8**

&#x20;             **atributo\_9**

&#x20;             **atributo\_10**

&#x20;             **atributo\_11**

&#x20;             **atributo\_12**

&#x20;             **atributo\_13**

&#x20;             **atributo\_14**

&#x20;             **atributo\_15**

&#x20;             **atributo\_16**

&#x20;             **atributo\_17**

&#x20;             **atributo\_18**

&#x20;             **atributo\_19**

&#x20;             **atributo\_20**

&#x20;             **atributo\_21**

&#x20;             **atributo\_22**

&#x20;             **atributo\_23**

&#x20;             **atributo\_24**

&#x20;             **atributo\_25**

&#x20;             **atributo\_26**

&#x20;             **atributo\_27**

&#x20;             **atributo\_28**

&#x20;             **atributo\_29**

&#x20;             **atributo\_30**

&#x20;             **atributo\_31**

&#x20;             **atributo\_32**

&#x20;             **atributo\_33**

&#x20;             **atributo\_34**

&#x20;             **atributo\_35**

&#x20;             **atributo\_36**

&#x20;             **atributo\_37**

&#x20;             **atributo\_38**

&#x20;             **atributo\_39**

&#x20;             **atributo\_40**

&#x20;             **atributo\_41**

&#x20;             **atributo\_42**

&#x20;             **atributo\_43**

&#x20;             **atributo\_44**

&#x20;             **atributo\_45**

&#x20;             **atributo\_46**

&#x20;             **atributo\_47**

&#x20;             **atributo\_48**

&#x20;             **atributo\_49**

&#x20;             **atributo\_50**

&#x20;             **atributo\_51**

&#x20;             **atributo\_52**

&#x20;             **atributo\_53**

&#x20;             **atributo\_54**

&#x20;             **atributo\_55**

&#x20;             **atributo\_56**

&#x20;             **atributo\_57**

&#x20;             **class**

**Test mode:    user supplied test set:  size unknown (reading incrementally)**



**=== Classifier model (full training set) ===**



**IB1 instance-based classifier**

**using 9 nearest neighbour(s) for classification**





**Time taken to build model: 0 seconds**



**=== Evaluation on test set ===**



**Time taken to test model on supplied test set: 0.1 seconds**



**=== Summary ===**



**Correctly Classified Instances        1137               82.3316 %**

**Incorrectly Classified Instances       244               17.6684 %**

**Kappa statistic                          0.6254**

**Mean absolute error                      0.3171**

**Root mean squared error                  0.3726**

**Relative absolute error                 65.1832 %**

**Root relative squared error             75.9771 %**

**Total Number of Instances             1381**     



**=== Detailed Accuracy By Class ===**



&#x20;                **TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class**

&#x20;                **0,877    0,259    0,839      0,877    0,857      0,626    0,881     0,886     0**

&#x20;                **0,741    0,123    0,796      0,741    0,768      0,626    0,881     0,835     1**

**Weighted Avg.    0,823    0,206    0,822      0,823    0,822      0,626    0,881     0,866**     



**=== Confusion Matrix ===**



&#x20;  **a   b   <-- classified as**

&#x20;**734 103 |   a = 0**

&#x20;**141 403 |   b = 1**





