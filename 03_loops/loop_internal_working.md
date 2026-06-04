## Iteration Tool
- for,comprehension ```([x for x in range(10)])```

## Iterable Objects
- list,file ``` file itself has its own iter tool```

## Response
- __next__

Iterable tool query with iterable objects to apply the loop on the object so it sends a itr method--> ```itr()```

so in response objects sends ```__next__``` value

### Iterable objects always points to the starting emmory of the object do not give the complete object

geting ```__next__``` in response means we can still apply the looop on the object. more value exist in the memory

```stop iteration exception``` this exception is raised when the pointer reaches to last element of the object

### ** we can make an object iterable or non iterable based on the next property whether it is present or not