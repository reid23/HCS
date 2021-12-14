#%%
print('using this for testing random stuff')
# %%
def foo(bar):
    bar+=5

foo(5)

print(bar)

#see, the linter even catches it
#scope
# %%
bar=1
def foo(baz):
    global bar
    bar+=baz

foo(5)

print(bar)


#%%
bar=1
def foo(bar, baz):
    return bar+baz

bar=foo(bar, 5)

print(bar)
# %%
