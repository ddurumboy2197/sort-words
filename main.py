def list_alphabetical_sort(lst):
    return sorted(lst)

# Misol:
sozlar = ["apple", "banana", "cherry", "date", "elderberry"]
print(list_alphabetical_sort(sozlar))
```

```python
def list_alphabetical_sort(lst):
    return sorted(lst, key=str.lower)

# Misol:
sozlar = ["Apple", "banana", "Cherry", "date", "elderberry"]
print(list_alphabetical_sort(sozlar))
