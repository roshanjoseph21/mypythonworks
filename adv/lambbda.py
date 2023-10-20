add=lambda n,n2: n+n2
sub=lambda n,n2: n-n2
min_two=lambda n,n2: n if n<n2 else n2
max_two=lambda n,n2: n if n>n2 else n2
odd_even=lambda n:"even" if n%2==0 else"odd"
print(odd_even(4))