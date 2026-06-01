# Internal working of python
# immutable data tyoes
- when we alocate a memory to a value then a refcount is alwaus associated with it which is diff to trace

eg: 
```
import sys
sys.getrefcount('5657')
```

- it gives the sme value if i change the ip in this it will give the same value

- there is exception in case garbage collection with respect to 
 # numbers
 # string

 - garbage collector wait for some time when the ref is free 

 ### Before any arithmatic calc the value of the ref automaticaly comes first

 ```
 n=[1,2,3]
 m=n
 m==n -->True
 m is n -->True
 m=[1,2,3]
 m==n -->True
 m is n -->False
 ```