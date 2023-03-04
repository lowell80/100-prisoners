# 100 Prisoners Problem

Some code I threw together to simulate the loop length theory.
First run showed the 31% success rate expected for 100 prisoners.


## Example output:


```
     |    0   1   2   3   4   5   6   7   8   9
  -- | ----------------------------------------
   0 |   55  81  62  85  89  94  32  31  46  21
  10 |   97  11  83  36  71  22  57  14  33   0
  20 |   40  88  23  95  43  56  65   1  76   5
  30 |   87   2  80   3  82  29  67  27  30  93
  40 |    6  59  24  99  69  52  73  70  84  18
  50 |   86  39  72  98  92  41  53  17  16  78
  60 |   37  45  34  48  49  61  91  15  54  13
  70 |   63  19   7  35  90  28  38  47  79   4
  80 |   74  25  26  50  12  20   9  66  77  68
  90 |   64  42  10  75  96  58  60  44  51   8

Loop 1:  Found 1 entries.   Loop=[11]
Loop 2:  Found 12 entries.   Loop=[62, 34, 82, 26, 65, 61, 45, 52, 72, 7, 31, 2]
Loop 3:  Found 13 entries.   Loop=[21, 88, 77, 47, 70, 63, 48, 84, 12, 83, 50, 86, 9]
Loop 4:  Found 13 entries.   Loop=[85, 20, 40, 6, 32, 80, 74, 90, 64, 49, 18, 33, 3]
Loop 5:  Found 29 entries.   Loop=[55, 41, 59, 78, 79, 4, 89, 68, 54, 92, 10, 97, 44, 69, 13, 36, 67, 15, 22, 23, 95, 58, 16, 57, 17, 14, 71, 19, 0]
Loop 6:  Found 32 entries.   Loop=[81, 25, 56, 53, 98, 51, 39, 93, 75, 28, 76, 38, 30, 87, 66, 91, 42, 24, 43, 99, 8, 46, 73, 35, 29, 5, 94, 96, 60, 37, 27, 1]
Total games 1000.   Won 31.0%
```

## Reference
* [Veritasium: The Riddle That Seems Impossible Even If You Know The Answer](https://www.youtube.com/watch?v=iSNsgj1OCLA)
* https://en.wikipedia.org/wiki/100_prisoners_problem
